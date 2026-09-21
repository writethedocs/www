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
   reader sends back small, and flip the flag. Written against ablog 0.11.13;
   re-check it when ablog is upgraded.

4. YAML is parsed with libyaml.
   PyYAML only uses its C parser when asked, and ``yaml.safe_load`` looks up
   ``yaml.SafeLoader`` at call time, so pointing that name at the C loader
   speeds up every ``safe_load`` in the build, ours and datatemplates' alike.
   This is deliberately process-wide.

Fix 1 patches two private Sphinx functions, so it is installed defensively:
if the Sphinx being built against does not look like the one this was written
for, the patch is skipped and the build is merely slower.
"""

import os

import sphinx
import yaml
from docutils import nodes
from sphinx.environment.adapters import toctree as toctree_adapter
from sphinx.util import logging

logger = logging.getLogger(__name__)

# The Sphinx major versions whose toctree internals this module was written
# against and tested with.
_SUPPORTED_SPHINX_MAJOR = (8,)

# --- 1. toctree cache ---------------------------------------------------------

_original_entries_from_toctree = None
_original_toctree_add_classes = None

# Set on a cached entry node so _mark_current can recognise it. Node copies do
# not carry arbitrary attributes, so this cannot leak into a rendered page.
_CACHE_ATTR = 'wtd_cached_toctree'


class _CachedToctree:
    """A resolved toctree, shared by every page that renders it."""

    __slots__ = ('entry', 'refs_by_docname', 'marked')

    def __init__(self, entry):
        self.entry = entry
        # Every reference in the tree, by the document it points at, so the
        # "current" markers for a page can be placed without walking the tree.
        self.refs_by_docname = {}
        for ref in entry.findall(nodes.reference):
            if not ref['anchorname']:
                self.refs_by_docname.setdefault(ref['refuri'], []).append(ref)
        # Nodes that carry a "current" class for the page rendered last.
        self.marked = []

    def unmark(self):
        for node in self.marked:
            node['classes'].remove('current')
        self.marked.clear()


_toctree_cache = {}    # cache key -> _CachedToctree


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
    args = (
        env, prune, titles_only, collapse, includehidden, tags,
        toctree_ancestors, included, excluded, toctreenode, parents, subtree,
    )
    # Only the toctrees declared in the root document are resolved repeatedly,
    # once per page for the sidebar. A toctree in a page body is resolved for
    # that page alone, so caching it would only cost memory.
    if subtree or collapse or toctreenode.get('parent') != env.config.root_doc:
        return _original_entries_from_toctree(*args)

    # The only page-specific input is the set of ancestors that override
    # ``tocdepth``; everything else in the resolved tree is the same for
    # every page.
    tocdepth_ancestors = frozenset(
        ancestor for ancestor in toctree_ancestors
        if env.metadata.get(ancestor, {}).get('tocdepth', 0) > 0
    )
    key = (
        toctreenode.get('parent'),
        tuple(toctreenode['entries']),
        prune, titles_only, includehidden, tocdepth_ancestors,
    )

    cached = _toctree_cache.get(key)
    if cached is not None:
        cached.unmark()
        return [cached.entry]

    entries = _original_entries_from_toctree(*args)

    # Sphinx adds the ``toctree-l<n>`` depth classes on every page. They never
    # change, so add them once here; _mark_current then only has to add the
    # page-specific ``current`` markers. Depth 2 on the bullet list is what
    # Sphinx's own depth 1 on the wrapping paragraph works out to.
    _original_toctree_add_classes(entries[0], 2, None)
    cached = _CachedToctree(entries[0])
    setattr(cached.entry, _CACHE_ATTR, cached)
    _toctree_cache[key] = cached
    return entries


def _mark_current(node, depth, docname):
    """
    Drop-in replacement for ``sphinx.environment.adapters.toctree._toctree_add_classes``.

    For a cached tree, add the ``current`` class to the branch of every
    reference to *docname*, exactly as Sphinx does, but by lookup instead of
    a walk over the whole tree. Sphinx also flags the branch with
    ``iscurrent``; that only matters for ``collapse=True``, which never uses
    the cache. Anything else falls through to Sphinx.

    Marking mutates the shared cached tree in place. That is safe because
    ``_resolve_toctree`` deep-copies the tree immediately after this returns,
    and ``unmark`` runs before the tree is handed out again.
    """
    # Sphinx only ever passes a whole resolved toctree at depth 1; deeper
    # calls are its own recursion, which reaches this name through the patch.
    if depth == 1:
        for child in node.children:
            cached = getattr(child, _CACHE_ATTR, None)
            if cached is not None:
                for ref in cached.refs_by_docname.get(docname, ()):
                    branch = ref
                    while branch:
                        branch['classes'].append('current')
                        cached.marked.append(branch)
                        branch = branch.parent
                return
    _original_toctree_add_classes(node, depth, docname)


def _clear_toctree_cache(app):
    _toctree_cache.clear()


def _install_toctree_cache():
    """Patch Sphinx's toctree resolution, or leave it alone and say why."""
    global _original_entries_from_toctree, _original_toctree_add_classes

    original_entries = getattr(toctree_adapter, '_entries_from_toctree', None)
    original_classes = getattr(toctree_adapter, '_toctree_add_classes', None)
    if sphinx.version_info[0] not in _SUPPORTED_SPHINX_MAJOR or None in (
        original_entries, original_classes
    ):
        # Deliberately not a warning: the build is correct either way, and
        # -W would turn a Sphinx upgrade into a failed build rather than a
        # slow one, which is the opposite of the point.
        logger.info(
            'build_perf: not caching the sidebar toctree, because Sphinx %s '
            'is not a version this was written against. The build is correct '
            'but slower. Re-check _ext/build_perf.py against the new toctree '
            'internals.',
            sphinx.__display_version__,
        )
        return False

    _original_entries_from_toctree = original_entries
    _original_toctree_add_classes = original_classes
    toctree_adapter._entries_from_toctree = _cached_entries_from_toctree
    toctree_adapter._toctree_add_classes = _mark_current
    return True


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

# The process that owns the posts currently on the environment. A forked
# reader inherits the parent's posts along with this value, notices the
# mismatch, and starts from empty.
_posts_owner_pid = None


def _drop_inherited_ablog_posts(app, doctree):
    """
    In a parallel-read worker, forget the posts inherited at fork time.

    Sphinx forks each reader from the main process, so a worker starts with
    every post merged so far, and sends the whole environment back when it
    finishes. Only the posts for the documents this worker read are merged,
    so the inherited ones just make each environment transfer bigger and
    slower to unpickle. Runs once per worker, before ablog stores anything.
    """
    global _posts_owner_pid
    pid = os.getpid()
    if pid != _posts_owner_pid:
        _posts_owner_pid = pid
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
    global _posts_owner_pid
    _posts_owner_pid = os.getpid()

    if getattr(yaml, '__with_libyaml__', False):
        yaml.SafeLoader = yaml.CSafeLoader

    if _install_toctree_cache():
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
