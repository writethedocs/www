"""
Template context for the community pages: everything outside
``conf/<city>/<year>/``.

The community pages use the conference design (see ``_templates/layout.html``).
Their header menu, default banner photos, front page hero and tiles, and
list of upcoming conferences live in ``_data/community.yaml``. This module
loads that file once, checks that the photos and icons it names exist, and
works out per page which banner to show (for conference pages too) and which
menu item is current.
"""

import os
import re
import zlib
from collections import defaultdict
from functools import partial

from sphinx.errors import ConfigError
from sphinx.util import logging

from .utils import conference_config_path, load_yaml

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
        upcoming_conference(tag, srcdir) for tag in data['upcoming_conferences']
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


def conference_summary(shortcode, year, srcdir='.'):
    """
    A conference's public name and pages, from its config file, or None if
    there is no such conference.
    """
    config_file = os.path.join(srcdir, conference_config_path(shortcode, year))
    if not os.path.exists(config_file):
        return None
    config = load_yaml(config_file)
    root = f'conf/{shortcode}/{year}'
    news = f'{root}/news/index'
    if not any(os.path.exists(os.path.join(srcdir, news + ext)) for ext in ('.rst', '.md')):
        news = f'{root}/index'
    return {
        'config': config,
        'title': f"Write the Docs {config['name']} {year}",
        # The tag on the conference's news posts.
        'tag': f'{shortcode}-{year}',
        'docname': f'{root}/index',
        'url': f'/{root}/',
        'news_docname': news,
    }


def upcoming_conference(tag, srcdir='.'):
    """
    Summarize a conference for the front page and conference lists, from its
    ``<shortcode>-<year>`` in community.yaml.
    """
    shortcode, year = tag.rsplit('-', 1)
    conference = conference_summary(shortcode, year, srcdir)
    if conference is None:
        raise ConfigError(
            f'{DATA_FILE} lists the upcoming conference {tag!r}, '
            f'but there is no {conference_config_path(shortcode, year)}')
    config = conference.pop('config')
    logo = f'_static/conf/images/logos/{shortcode}{year}.png'
    return {
        **conference,
        'name': config['name'],
        'year': config['year'],
        'dates': config['date']['short'],
        'location': f"{config['city']}, {config['local_area']}",
        # The logo shown on the front page, if the conference has one yet.
        'logo': logo if os.path.exists(os.path.join(srcdir, logo)) else None,
    }


def check_default_banners(app):
    """Fail the build early if a default banner in community.yaml doesn't exist."""
    paths = app.config.html_context['community']['photos']['default']
    missing = sorted(p for p in paths if not os.path.exists(os.path.join(app.srcdir, p)))
    if missing:
        raise ConfigError(f'{DATA_FILE} names banner photos that do not exist: {missing}')


def page_banner(pagename, meta, defaults):
    """
    The photo behind a page's title: the page's own ``banner`` field, or one
    of ``defaults``, picked by the page name so it doesn't change between
    builds.
    """
    if meta and meta.get('banner'):
        return meta['banner']
    if isinstance(defaults, str):
        return defaults
    # crc32 rather than hash(), which changes between Python processes.
    return defaults[zlib.crc32(pagename.encode()) % len(defaults)]


def link_matches(link, pagename):
    """Whether a site-relative menu link (``/guide/``) covers this page."""
    if not link.startswith('/'):
        return False
    return f"/{pagename.removesuffix('/index')}/".startswith(link)


def toctree_ancestors(relations, pagename):
    """The pages above this one in the toctree, nearest first."""
    ancestors = []
    parent = relations.get(pagename, [None])[0]
    while parent and parent not in ancestors:
        ancestors.append(parent)
        parent = relations.get(parent, [None])[0]
    return ancestors


def page_nav(community, pagename, ancestors=()):
    """
    The header menu, with the item that covers this page marked current: the
    item whose links cover the page, or a page above it in the toctree, such
    as its section's page.
    """
    pages = [pagename, *ancestors]
    return [
        {**item, 'current': any(
            link_matches(link, page)
            for link in [item['link'], *(child['link'] for child in item['children'])]
            for page in pages
        )}
        for item in community['nav']
    ]


# Newsletter issues are named blog/newsletter-<month>-<year>.
NEWSLETTER_ISSUE = re.compile(r'blog/newsletter-[a-z]+-\d{4}')


def blog_listing(blog, community, srcdir='.'):
    """
    Split the blog's posts into its three kinds:

    - ``newsletter``: the newsletter's issues, by year. The newsletter page
      lists them all.
    - ``upcoming_conferences`` and ``earlier_conferences``: conference news,
      grouped by the conference's ``<shortcode>-<year>`` tag, the same tag
      its news page lists. The upcoming conferences in community.yaml come
      first, then the rest, latest news first.
    - ``updates``: the rest of the posts outside ``conf/``, by year, such as
      community board updates and yearly reports. The blog page lists them.
    """
    newsletter = defaultdict(list)
    updates = defaultdict(list)
    conferences = {}
    for post in blog.posts:  # newest first
        if not post.published:
            continue
        if NEWSLETTER_ISSUE.fullmatch(post.docname):
            newsletter[post.date.year].append(post)
        elif not post.docname.startswith('conf/'):
            updates[post.date.year].append(post)
        for tag in map(str, post.tags):
            if tag not in conferences:
                match = re.fullmatch(r'([a-z]+)-(\d{4})', tag)
                conferences[tag] = match and conference_summary(*match.groups(), srcdir)
            if conferences[tag]:
                conferences[tag].setdefault('posts', []).append(post)

    def listing(conference, posts):
        return {'title': conference['title'], 'docname': conference['news_docname'], 'posts': posts}

    upcoming = [
        listing(c, (conferences.pop(c['tag'], None) or {}).get('posts', []))
        for c in community['upcoming_conferences']
    ]
    return {
        'newsletter': sorted(newsletter.items(), reverse=True),
        'updates': sorted(updates.items(), reverse=True),
        'upcoming_conferences': upcoming,
        'earlier_conferences': [listing(c, c['posts']) for c in conferences.values() if c],
    }


# Sections in every newsletter issue, left out of the list of its topics.
NEWSLETTER_REGULARS = {
    'events coming up', 'featured job posts', 'from our sponsor', 'write the docs resources',
}


def newsletter_issues(blog, env, count=3):
    """
    The latest newsletter issues, for the cards on the newsletter and blog
    pages, each with the topics it covers: its section titles, less the
    regular ones.
    """
    issues = []
    for post in blog.posts:  # newest first
        if not (post.published and NEWSLETTER_ISSUE.fullmatch(post.docname)):
            continue
        toc = env.tocs[post.docname]
        sections = toc[0][1] if len(toc) and len(toc[0]) > 1 else []
        topics = [item[0].astext() for item in sections]
        issues.append({
            'post': post,
            'topics': [t for t in topics if t.strip().lower() not in NEWSLETTER_REGULARS],
        })
        if len(issues) == count:
            break
    return issues


def add_page_context(app, pagename, templatename, context, doctree):
    """
    Add ``page_banner`` and ``community_nav`` to every page's context, and the
    functions the blog and newsletter templates call for their posts.

    Conference pages pick their default banners from ``photos.default`` in
    their config, which core.py adds to the context; community pages from
    ``photos.default`` in community.yaml.
    """
    community = context['community']
    photos = context.get('photos') or {}
    defaults = photos.get('default') or community['photos']['default']
    banner = page_banner(pagename, context.get('meta'), defaults)
    if not os.path.exists(os.path.join(app.srcdir, banner)):
        logger.warning('banner photo %s does not exist', banner, location=pagename)
    context['page_banner'] = banner
    ancestors = toctree_ancestors(getattr(app.builder, 'relations', {}), pagename)
    context['community_nav'] = page_nav(community, pagename, ancestors)
    # Called by community/blog.html and community/newsletter.html, once the
    # posts of every page are known.
    context['blog_listing'] = partial(blog_listing, context['ablog'], community, app.srcdir)
    context['newsletter_issues'] = partial(newsletter_issues, context['ablog'], app.env)


def setup(app):
    app.connect('builder-inited', check_default_banners)
    # After core.py's handler, which adds a conference's config to the context.
    app.connect('html-page-context', add_page_context, priority=600)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
