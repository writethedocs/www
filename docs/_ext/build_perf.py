"""
Build-speed fixes for the site's Sphinx build.

Profiling a full build showed that the parts of Sphinx we lean on were
doing a lot of repeated work. Each fix below is self-contained; delete the
whole module and the build still works, only slower.

1. Doctrees no longer embed the whole build environment.
   MyST's ``eval-rst`` blocks parse into a temporary document whose settings
   still point at the Sphinx environment. Nodes moved out of that document
   keep pointing at it, so pickling the page doctree also pickled the ~20MB
   environment. Re-pointing every node at its real document before pickling
   shrinks a 16MB doctree to a few KB.

2. ablog is marked safe for parallel reading.
   ablog declares ``parallel_read_safe = False``, and that alone forces Sphinx
   to read every document serially. All it keeps on the environment is
   per-document post info, so we supply the merge, keep the environment each
   reader sends back small, and flip the flag.

3. ``datatemplate`` directives parse YAML with libyaml.
   sphinxcontrib-datatemplates calls ``yaml.safe_load``, which uses PyYAML's
   pure Python parser even when the C one is installed. Pointing PyYAML's
   ``SafeLoader`` at the C implementation makes every ``safe_load`` in the
   build about ten times faster.
"""

import os

import yaml
from docutils import nodes

# --- 1. doctree slimming ------------------------------------------------------

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


# --- 2. ablog parallel reading ------------------------------------------------

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

    if getattr(yaml, '__with_libyaml__', False):
        yaml.SafeLoader = yaml.CSafeLoader

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
