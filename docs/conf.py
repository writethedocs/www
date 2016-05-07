# -*- coding: utf-8 -*-
#
import sys, os
extensions = ['sphinx.ext.doctest']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Write the Docs Guide'
copyright = """
<a rel="license"
   href="http://creativecommons.org/licenses/by/3.0/"
   style="float:right;height:3em;line-height:3em;padding:10px 0 0 1em;">
    <img alt="Creative Commons License" style="border-width:0"
         src="http://i.creativecommons.org/l/by/3.0/88x31.png" />
</a>
2016, Write the Docs Community
<br />
This work is licensed under a
<br />
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/">
    Creative Commons Attribution 3.0 Unported License
</a>
"""
version = '1.0'
release = '1.0'
exclude_patterns = [
  '_build', 
  'conference',
  '2014',
  'includes',
]
pygments_style = 'sphinx'

import alabaster

html_theme_path = [alabaster.get_path()]
extensions = ['alabaster']
html_theme = 'alabaster'
html_sidebars = {
   '**': [
       'about.html', 'navigation.html', 'searchbox.html', 
   ]
}
html_theme_options = {
   'logo': 'sticker-wtd-colors.png',
   'github_user': 'writethedocs',
   'github_repo': 'docs',
}

html_static_path = ['_static', 'img']
html_sidebars = {
    '**': [
           'about.html',
           'links.html',
           'localtoc.html',
           #'relations.html',
           #'sourcelink.html',
           #'searchbox.html',
           ],
}

htmlhelp_basename = 'WritetheDocsdoc'

latex_documents = [
  ('index', 'WritetheDocs.tex', u'Write the Docs Documentation',
   u'Eric Holscher, Troy Howard', 'manual'),
]

texinfo_documents = [
  ('index', 'WritetheDocs', u'Write the Docs Documentation',
   u'Eric Holscher, Troy Howard', 'WritetheDocs', 'One line description of project.',
   'Miscellaneous'),
]

rst_epilog = """
.. |wtd| replace:: Write the Docs

"""
