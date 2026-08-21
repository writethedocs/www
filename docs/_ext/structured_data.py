"""Schema.org structured data (JSON-LD) for topic pages.

Generates ``CollectionPage``, ``ItemList``, and ``BreadcrumbList`` markup for
every page under ``topics/`` by reading the page's own content. Curated
resources added to a topic page therefore show up in its structured data with
no extra authoring work, which keeps the topic pages maintainable by hand.

The JSON-LD is appended to the page's ``metatags`` so that it renders inside
``<head>``.
"""

import json
import re
from html import unescape
from urllib.parse import urljoin

from docutils import nodes


#: Links we treat as curated resources: newsletter articles and conference talks.
NEWSLETTER_PREFIX = '/blog/'
VIDEO_HOSTS = ('youtube.com', 'youtu.be')

#: ``/blog/newsletter-july-2025/#anchor`` -> ``2025-07``
NEWSLETTER_DATE_RE = re.compile(r'/blog/newsletter-([a-z]+)-(\d{4})/')

MONTHS = {
    'january': '01', 'february': '02', 'march': '03', 'april': '04',
    'may': '05', 'june': '06', 'july': '07', 'august': '08',
    'september': '09', 'october': '10', 'november': '11', 'december': '12',
}


def _is_resource(uri):
    """Is this link one of our curated resources, rather than page navigation?"""
    return uri.startswith(NEWSLETTER_PREFIX) or any(h in uri for h in VIDEO_HOSTS)


def _published_date(uri):
    """Derive an ISO date from a newsletter URL, so we don't hand-maintain dates."""
    match = NEWSLETTER_DATE_RE.search(uri)
    if not match:
        return None
    month = MONTHS.get(match.group(1))
    return '{}-{}'.format(match.group(2), month) if month else None


def _resources(doctree):
    """Yield ``(title, uri)`` for each curated resource linked in a list item."""
    for item in doctree.findall(nodes.list_item):
        for ref in item.findall(nodes.reference):
            uri = ref.get('refuri', '')
            if _is_resource(uri):
                yield ref.astext().strip(), uri
            # Only the first link in a bullet describes that resource.
            break


def _item_list(doctree, base_url):
    elements = []
    for position, (title, uri) in enumerate(_resources(doctree), start=1):
        element = {
            '@type': 'ListItem',
            'position': position,
            'name': title,
            'url': urljoin(base_url, uri),
        }
        published = _published_date(uri)
        if published:
            element['datePublished'] = published
        elements.append(element)
    return elements


def _meta_description(metatags):
    """Reuse the page's own meta description, whatever attribute order it uses."""
    for tag in re.findall(r'<meta[^>]*>', metatags or ''):
        if re.search(r'name=["\']description["\']', tag, re.IGNORECASE):
            content = re.search(r'content=["\']([^"\']*)["\']', tag, re.IGNORECASE)
            if content:
                return unescape(content.group(1))
    return ''


def _breadcrumbs(context, page_url, title, base_url):
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': base_url}]
    for parent in context.get('parents', []):
        crumbs.append({
            '@type': 'ListItem',
            'position': len(crumbs) + 1,
            'name': parent['title'],
            'item': urljoin(page_url, parent['link']),
        })
    crumbs.append({
        '@type': 'ListItem',
        'position': len(crumbs) + 1,
        'name': title,
        'item': page_url,
    })
    return crumbs


def add_topic_structured_data(app, pagename, templatename, context, doctree):
    """Attach JSON-LD to topic pages describing the topic and its resources."""
    if doctree is None or not pagename.startswith('topics/'):
        return

    base_url = app.config.html_baseurl
    if not base_url.endswith('/'):
        base_url += '/'
    page_url = urljoin(base_url, app.builder.get_target_uri(pagename))

    title = context.get('title') or pagename
    description = _meta_description(context.get('metatags'))

    collection_page = {
        '@type': 'CollectionPage',
        'name': title,
        'url': page_url,
        'isPartOf': {
            '@type': 'WebSite',
            'name': app.config.ogp_site_name,
            'url': base_url,
        },
    }
    if description:
        collection_page['description'] = description

    elements = _item_list(doctree, base_url)
    if elements:
        collection_page['mainEntity'] = {
            '@type': 'ItemList',
            'numberOfItems': len(elements),
            'itemListElement': elements,
        }

    graph = {
        '@context': 'https://schema.org',
        '@graph': [
            collection_page,
            {
                '@type': 'BreadcrumbList',
                'itemListElement': _breadcrumbs(context, page_url, title, base_url),
            },
        ],
    }

    script = '<script type="application/ld+json">{}</script>'.format(
        json.dumps(graph, indent=2)
    )
    context['metatags'] = context.get('metatags', '') + '\n' + script
