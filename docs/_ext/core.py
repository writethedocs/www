from __future__ import print_function

from future import standard_library
from yaml import YAMLError

from .utils import load_yaml

standard_library.install_aliases()

import logging

try:
    from pathlib import PurePath
except ImportError:
    from pathlib2 import PurePath

log = logging.getLogger(__name__)


def load_conference_page_context(app, page):
    """
    Get conference specific YAML data and add it to the context.

    Returns an empty dict if it isn't run on a proper conference page.
    """
    data = {}
    if page.startswith('conf'):
        p = PurePath(page)
        try:
            year = int(p.parts[2])
        except (ValueError, IndexError):
            # If the second part is not the year, this is a document
            # about sponsorship or similar generic pages, that need
            # no conference-specific context.
            return data
        if year >= 2018:
            if year < 2020:
                yaml_file = '_data/config-' + p.parts[1] + '-' + p.parts[2] + '.yaml'
            else:
                yaml_file = '_data/' + p.parts[1] + '-' + p.parts[2] + '-config.yaml'
            try:
                yaml_config = load_yaml(yaml_file)
                data.update(yaml_config)
            except (YAMLError, OSError) as error:
                log.warning('Unable to process conference YAML file %s while rendering %s: %s', yaml_file, page, error)
    return data


def render_rst_with_jinja(app, docname, source):
    """
    Pass our RST files through the jinja parser.
    This allows us to use all jinja features in all RST templates
    """
    if app.builder.format != 'html':
        return

    # For post-2018 pages, pass the document through the jinja renderer
    # with the appropriate context (jinja filters have been added already)
    context = load_conference_page_context(app, docname)
    context.update(app.config.html_context)
    if docname.startswith(('about/', 'conf/', 'guide/', 'videos/by-year', 'videos/by-series')):
        src = source[0]
        rendered = app.builder.templates.render_string(src, context)
        source[0] = rendered


def override_template_load_context(app, pagename, templatename, context, doctree):
    """
    Set the template to use when rendering the page.

    If a string is returned from this function,
    it will be the template used to render this page.
    Example::

        :template: 2018/conf.html

        Page title
        ==========

        Content
    """
    page_context = load_conference_page_context(app, pagename)
    context.update(page_context)

    # Markdown
    if (context and
            'page_source_suffix' in context and
            context['page_source_suffix'] == '.md'):
        txt = doctree[0].astext()
        if txt.startswith(':template:'):
            context['body'] = context['body'].replace(txt, '')
            return txt.split(':')[2].strip()
    # rst
    try:  # Sphinx was throwing a weird error here, and this is a workaround
        if (context and
                'meta' in context and
                'template' in context.get('meta', {})):
            return context['meta']['template']
    except TypeError:
        pass


def set_html_context(app, docname, source):
    # Store old context
    page_context = load_conference_page_context(app, docname)
    if page_context:
        app.config.old_html_context = app.config.html_context.copy()
        app.config.html_context.update(page_context)


def unset_html_context(app, doctree):
    if hasattr(app.config, 'old_html_context'):
        app.config.html_context = app.config.old_html_context.copy()
        del app.config.old_html_context
