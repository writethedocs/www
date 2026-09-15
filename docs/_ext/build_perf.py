"""
Build-speed fixes for the site's Sphinx build.

Profiling a full build showed that the parts of Sphinx we lean on were
doing a lot of repeated work. Each fix below is self-contained; delete the
whole module and the build still works, only slower.

1. ``toctree()`` in the sidebar is resolved once, not once per page.
   ``_templates/navigation.html`` calls ``toctree(collapse=False)``. Sphinx
   resolves the *entire* site toctree (thousands of nodes) for every page
   and only then prunes it to the top level. With ``collapse=False`` the
   resolved tree is identical for every page, so we cache it per process.

2. Doctrees no longer embed the whole build environment.
   MyST's ``eval-rst`` blocks parse into a temporary document whose settings
   still point at the Sphinx environment. Nodes moved out of that document
   keep pointing at it, so pickling the page doctree also pickled the ~20MB
   environment. Re-pointing every node at its real document before pickling
   shrinks a 16MB doctree to a few KB.

3. ablog is marked safe for parallel reading.
   ablog declares ``parallel_read_safe = False``, and that alone forces Sphinx
   to read every document serially. All it keeps on the environment is
   per-document post info, so we supply the merge, keep the environment each
   reader sends back small, and flip the flag.
"""

import os

from docutils import nodes
from sphinx.environment.adapters import toctree as toctree_adapter

# --- 1. toctree cache ---------------------------------------------------------

_original_entries_from_toctree = toctree_adapter._entries_from_toctree
_toctree_entries_cache = {}


def _reset_toctree_marks(node):
    """
    Undo the per-page changes Sphinx makes while resolving a toctree.

    ``_toctree_add_classes`` appends ``toctree-l<n>`` and ``current`` classes
    and sets ``iscurrent`` in place, so the cached tree has to be cleaned
    before it is reused for the next page.
    """
    for subnode in node.findall(nodes.Element):
        classes = subnode['classes']
        if classes:
            subnode['classes'] = [
                c for c in classes if c != 'current' and not c.startswith('toctree-l')
            ]
        subnode.attributes.pop('iscurrent', None)


def _cached_entries_from_toctree(
    env, prune, titles_only, collapse, includehidden, tags,
    toctree_ancestors, included, excluded, toctreenode, parents, subtree=False,
):
    """
    Drop-in replacement for ``sphinx.environment.adapters.toctree._entries_from_toctree``.

    Only the top-level, non-collapsing call is cached. With ``collapse=True``
    the result depends on which page is being rendered, and nested calls are
    already covered by caching their top-level caller.
    """
    if subtree or collapse:
        return _original_entries_from_toctree(
            env, prune, titles_only, collapse, includehidden, tags,
            toctree_ancestors, included, excluded, toctreenode, parents, subtree,
        )

    # The only page-specific input is the set of ancestors that override
    # ``tocdepth``; everything else in the resolved tree is the same for
    # every page.
    tocdepth_ancestors = frozenset(
        ancestor for ancestor in toctree_ancestors
        if env.metadata.get(ancestor, {}).get('tocdepth', 0) > 0
    )
    try:
        key = (
            toctreenode.get('parent'),
            tuple(toctreenode['entries']),
            prune, titles_only, includehidden, tocdepth_ancestors,
        )
        hash(key)
    except TypeError:
        return _original_entries_from_toctree(
            env, prune, titles_only, collapse, includehidden, tags,
            toctree_ancestors, included, excluded, toctreenode, parents, subtree,
        )

    entries = _toctree_entries_cache.get(key)
    if entries is None:
        entries = _original_entries_from_toctree(
            env, prune, titles_only, collapse, includehidden, tags,
            toctree_ancestors, included, excluded, toctreenode, parents, subtree,
        )
        _toctree_entries_cache[key] = entries
    else:
        for entry in entries:
            _reset_toctree_marks(entry)
    return entries


def _clear_toctree_cache(app):
    _toctree_entries_cache.clear()


# --- 2. doctree slimming ------------------------------------------------------

def _reattach_nested_documents(app, doctree):
    """
    Point every node at the doctree it actually lives in.

    Runs on ``doctree-read``, before Sphinx pickles the doctree, so nodes
    parsed inside a temporary document (MyST ``eval-rst``) stop dragging that
    document, and the environment hanging off its settings, into the pickle.
    """
    for node in doctree.findall():
        if node.document is not doctree:
            node.document = doctree


# --- 3. ablog parallel reading ------------------------------------------------

_main_pid = None
_worker_posts_dropped = False


def _drop_inherited_ablog_posts(app, doctree):
    """
    In a parallel-read worker, forget the posts inherited at fork time.

    Sphinx forks each reader from the main process, so a worker starts with
    every post merged so far, and sends the whole environment back when it
    finishes. Only the posts for the documents this worker read are merged,
    so the inherited ones just make each environment transfer bigger and
    slower to unpickle. Runs once per worker, before ablog stores anything.
    """
    global _worker_posts_dropped
    if _worker_posts_dropped or os.getpid() == _main_pid:
        return
    _worker_posts_dropped = True
    if hasattr(app.env, 'ablog_posts'):
        app.env.ablog_posts = {}


def _detach_ablog_post_copies(app, doctree):
    """
    Cut the link from ablog's stored post copies back to the build environment.

    ablog keeps a deep copy of each post's document on the environment. The
    copy shares the original document's settings object, which still points
    at the environment (Sphinx only clears ``env`` on the settings copy it
    gives the real doctree). Harmless in a serial read, but in a parallel
    read every merged worker environment stays reachable through these
    copies, so the environment each successive worker sends back grows
    without bound.
    """
    env = app.env
    for postinfo in getattr(env, 'ablog_posts', {}).get(env.docname, ()):
        copy = postinfo.get('doctree')
        if isinstance(copy, nodes.document) and getattr(copy.settings, 'env', None) is not None:
            copy.settings = copy.settings.copy()
            copy.settings.env = None


def _merge_ablog_posts(app, env, docnames, other):
    """Merge the post info a parallel reader collected into the main environment."""
    other_posts = getattr(other, 'ablog_posts', None)
    if not other_posts:
        return
    if not hasattr(env, 'ablog_posts'):
        env.ablog_posts = {}
    for docname in docnames:
        if docname in other_posts:
            env.ablog_posts[docname] = other_posts[docname]


def _register_ablog_posts(app, env):
    """
    Register posts with ablog as soon as reading finishes.

    In a serial read ablog registers its collections as a side effect of
    reading each post, so by the time pages are written every ``:ref:`` to a
    tag or archive resolves. Parallel readers do that work in child
    processes, so do it here in the main process instead. ablog itself skips
    registration later if it has already happened.
    """
    from ablog.blog import Blog
    from ablog.post import register_posts

    if not Blog(app):
        register_posts(app)


def setup(app):
    global _main_pid
    _main_pid = os.getpid()

    toctree_adapter._entries_from_toctree = _cached_entries_from_toctree
    app.connect('builder-inited', _clear_toctree_cache)

    # Priority 100 so this runs before ablog's doctree-read handler copies post
    # sections into the environment. Copies made before the fix would still
    # point at MyST's temporary documents, and in a parallel read every merged
    # worker environment would then stay reachable through them.
    app.connect('doctree-read', _reattach_nested_documents, priority=100)

    ablog_ext = app.extensions.get('ablog')
    if ablog_ext is not None and not ablog_ext.parallel_read_safe:
        # Priority 100: before ablog's doctree-read handler (500) stores a post.
        app.connect('doctree-read', _drop_inherited_ablog_posts, priority=100)
        # Priority 999: after ablog's own doctree-read handler has made its copies.
        app.connect('doctree-read', _detach_ablog_post_copies, priority=999)
        app.connect('env-merge-info', _merge_ablog_posts)
        app.connect('env-updated', _register_ablog_posts)
        ablog_ext.parallel_read_safe = True

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
