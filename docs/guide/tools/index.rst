================================
Tools for documentation writing
================================

Writing documentation requires good tools. This section covers documentation tools recommended by the Write the Docs community, with a focus on tools widely used for technical documentation.

Sphinx
------

Sphinx is a documentation generator widely used in the Python ecosystem and beyond. It converts reStructuredText (and Markdown via MyST Parser) into HTML, PDF, and other formats. Sphinx excels at technical documentation with features like code introspection, cross-referencing, and multiple output formats.

See the following pages for Sphinx guidance:

.. toctree::
   :maxdepth: 2

   sphinx
   sphinx-themes
   sphinx-community

Other documentation tools
-------------------------

While this section currently focuses on Sphinx, the Write the Docs community uses many documentation tools depending on project needs:

- **MkDocs**: Markdown-focused static site generator with live preview
- **Docusaurus**: React-based tool by Meta with built-in versioning and i18n
- **Jekyll**: Ruby-based static site generator, popular for GitHub Pages
- **Hugo**: Extremely fast Go-based generator for content sites

See the main :doc:`/guide/index` for broader documentation guidance applicable across tools.

Testing and quality
-------------------

.. toctree::
   :maxdepth: 2

   testing
