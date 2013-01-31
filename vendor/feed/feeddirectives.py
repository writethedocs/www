# -*- coding: utf-8 -*-
"""
    sphinxcontrib.feed.feeddirectives
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2007-2011 the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
    
    Latest is based on sphinx.directives.other.TocTree
"""

import os

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from sphinx.util.nodes import explicit_title_re, set_source_info
from sphinx.util import url_re, docname_join
from sphinx.util.matching import patfilter

from feednodes import latest

class Latest(Directive):
    """
    Directive to notify Sphinx about the hierarchical structure of the docs,
    and to include a table-of-contents-like tree in the current document.
    
    Used to be subclassed of TocTree, but now modified from it, to avoid
    tedious bugs from TocTree's rather special role, and depending upon
    private Sphinx APIs.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    
    option_spec = {
        # 'maxdepth': int,
        'glob': directives.flag,
        # 'hidden': directives.flag,
        # 'numbered': int_or_nothing,
        'titlesonly': directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env
        suffix = env.config.source_suffix
        glob = 'glob' in self.options
                
        # (title, ref) pairs, where ref may only be a document
        # external links are forbidden, since we have no way of dating them
        # and title may be None if the document's title is to be used
        entries = []
        includefiles = []
        
        all_docnames = env.found_docs.copy()
        # don't add the currently visited file in catch-all patterns
        all_docnames.remove(env.docname)
        
        ret = []
        
        for entry in self.content:
            if not entry:
                continue
            if not glob:
                # look for explicit titles ("Some Title <document>")
                m = explicit_title_re.match(entry)
                if m:
                    ref = m.group(2)
                    title = m.group(1)
                    docname = ref
                else:
                    ref = docname = entry
                    title = None
                # remove suffixes (backwards compatibility)
                if docname.endswith(suffix):
                    docname = docname[:-len(suffix)]
                # absolutize filenames
                docname = docname_join(env.docname, docname)
                if url_re.match(ref) or ref == 'self':
                    entries.append((title, ref))
                elif docname not in env.found_docs:
                    ret.append(self.state.document.reporter.warning(
                        'toctree contains reference to nonexisting '
                        'document %r' % docname, line=self.lineno))
                    env.note_reread()
                else:
                    entries.append((title, docname))
                    includefiles.append(docname)
            else:
                patname = docname_join(env.docname, entry)
                docnames = patfilter(all_docnames, patname)
                for docname in docnames:
                    all_docnames.remove(docname) # don't include it again
                    entries.append((None, docname))
                    includefiles.append(docname)
                if not docnames:
                    ret.append(self.state.document.reporter.warning(
                        'latest list glob pattern %r didn\'t match any documents'
                        % entry, line=self.lineno))
        
        subnode = latest()
        subnode['parent'] = env.docname
        # entries contains all entries (self references, external links etc.)
        subnode['entries'] = entries
        # includefiles only entries that are documents
        subnode['includefiles'] = includefiles
        subnode['maxdepth'] = self.options.get('maxdepth', -1)
        subnode['glob'] = glob
        subnode['titlesonly'] = 'titlesonly' in self.options
        #what does this do?
        set_source_info(self, subnode)
        wrappernode = nodes.compound(classes=['feed-latest-wrapper'])
        wrappernode.append(subnode)
        ret.append(wrappernode)
        return ret
