"""
Template context for the community pages: everything outside
``conf/<city>/<year>/``.

The community pages use the conference design (see ``_templates/layout.html``).
Their header menu, banner photos, front page hero and tiles, and list of
upcoming conferences live in ``_data/community.yaml``. This module loads that
file once, checks that the photos and icons it names exist, and works out per
page which banner to show and which menu item is current.
"""

import os
import re
import zlib

from sphinx.errors import ConfigError
from sphinx.util import logging

from .button import docname_year
from .utils import load_yaml

DATA_FILE = '_data/community.yaml'

logger = logging.getLogger(__name__)


def load_community_data(context, srcdir='.'):
    """
    Load ``_data/community.yaml``, expanding the upcoming conferences, the
    menu entry that lists them, and the front page.

    ``context`` is ``html_context`` from conf.py, which fills in placeholders
    like ``{slack_members}`` in the front page's text and links.
    """
    data = load_yaml(os.path.join(srcdir, DATA_FILE))
    data['home'] = front_page(data['home'], context, srcdir)
    data['upcoming_conferences'] = [
        upcoming_conference(slug, srcdir) for slug in data['upcoming_conferences']
    ]
    for item in data['nav']:
        children = []
        for child in item.get('children', []):
            if child.get('upcoming_conferences'):
                children.extend(
                    {'text': conf['title'], 'link': conf['url']}
                    for conf in data['upcoming_conferences']
                )
            else:
                children.append(child)
        item['children'] = children
    return data


def front_page(home, context, srcdir='.'):
    """
    Fill in the placeholders in the front page's hero and tiles, and keep the
    tiles whose ``when`` holds.
    """
    survey_open = context['salary_survey']['open']
    conditions = {'salary_survey_open': survey_open, 'salary_survey_closed': not survey_open}

    def fill(item, where):
        filled = {}
        for key, value in item.items():
            try:
                filled[key] = value.format_map(context) if isinstance(value, str) else value
            except (KeyError, IndexError) as error:
                raise ConfigError(f'{DATA_FILE}: unknown placeholder {error} in {where}') from None
        return filled

    hero = fill(home['hero'], 'home.hero')
    hero['buttons'] = [fill(button, 'home.hero.buttons') for button in home['hero']['buttons']]
    tiles = []
    for tile in home['tiles']:
        where = f'the {tile["title"]!r} tile'
        when = tile.get('when')
        if when is not None and when not in conditions:
            raise ConfigError(
                f'{DATA_FILE}: {where} has when: {when!r}; use one of {sorted(conditions)}')
        icon = os.path.join(srcdir, '_templates', 'community', 'icons', f'{tile["icon"]}.svg')
        if not os.path.exists(icon):
            raise ConfigError(f'{DATA_FILE}: {where} names an icon that does not exist: {icon}')
        if when is None or conditions[when]:
            tiles.append(fill(tile, where))
    return {'hero': hero, 'tiles': tiles}


def upcoming_conference(slug, srcdir='.'):
    """
    Summarize a conference for the front page and conference lists, from
    ``_data/<slug>-config.yaml``.
    """
    config_file = os.path.join(srcdir, '_data', f'{slug}-config.yaml')
    if not os.path.exists(config_file):
        raise ConfigError(
            f'{DATA_FILE} lists the upcoming conference {slug!r}, '
            f'but there is no {config_file}')
    config = load_yaml(config_file)
    year = config['year']
    shortcode = config['shortcode']
    # "**December 3-4, 2026**" -> "December 3-4"
    dates = re.sub(r',\s*\d{4}$', '', config['date']['main'].replace('*', '').strip())
    logo = f'_static/conf/images/logos/{shortcode}{year}.png'
    return {
        'name': config['name'],
        'year': year,
        'title': f"{config['name']} {year}",
        'docname': f'conf/{shortcode}/{year}/index',
        'url': f'/conf/{shortcode}/{year}/',
        'dates': dates,
        'location': f"{config['city']}, {config['local_area']}",
        # The logo shown on the front page, if the conference has one yet.
        'logo': logo if os.path.exists(os.path.join(srcdir, logo)) else None,
    }


def check_banners(app):
    """Fail the build early if a banner in community.yaml doesn't exist."""
    banners = app.config.html_context['community']['banners']
    paths = [banners['home'], *banners['sections'].values(), *banners['default']]
    missing = sorted({p for p in paths if not os.path.exists(os.path.join(app.srcdir, p))})
    if missing:
        raise ConfigError(f'{DATA_FILE} names banner photos that do not exist: {missing}')


def page_banner(community, pagename, meta):
    """The photo behind a page's title."""
    if meta and meta.get('banner'):
        return meta['banner']
    banners = community['banners']
    if pagename == 'index':
        return banners['home']
    section = pagename.split('/')[0]
    if section in banners['sections']:
        return banners['sections'][section]
    # crc32 rather than hash(), which changes between Python processes.
    default = banners['default']
    return default[zlib.crc32(pagename.encode()) % len(default)]


def link_matches(link, pagename):
    """Whether a site-relative menu link (``/guide/``) covers this page."""
    if not link.startswith('/'):
        return False
    return f"/{pagename.removesuffix('/index')}/".startswith(link)


def page_nav(community, pagename):
    """The header menu, with the item that covers this page marked current."""
    return [
        {**item, 'current': any(
            link_matches(link, pagename)
            for link in [item['link'], *(child['link'] for child in item['children'])]
        )}
        for item in community['nav']
    ]


def add_page_context(app, pagename, templatename, context, doctree):
    """Add ``community_banner`` and ``community_nav`` to every page's context."""
    community = context['community']
    banner = page_banner(community, pagename, context.get('meta'))
    # Conference pages have their own templates and don't show this banner.
    if docname_year(pagename) is None and not os.path.exists(os.path.join(app.srcdir, banner)):
        logger.warning('banner photo %s does not exist', banner, location=pagename)
    context['community_banner'] = banner
    context['community_nav'] = page_nav(community, pagename)


def setup(app):
    app.connect('builder-inited', check_banners)
    app.connect('html-page-context', add_page_context)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
