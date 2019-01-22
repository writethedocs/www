from __future__ import unicode_literals

import os.path

from lxml import etree, html
from six.moves.urllib.parse import urljoin
from sphinx.util import logging


logger = logging.getLogger(__name__)

TAGS = [
    'newsletter',
    'portland',
    'prague',
    'australia',
]


def rewrite_atom_feed(app, exception):
    """
    Rewrites the atom feed content elements to use absolute instead of relative links
    Applies to <a> and <img>
    """
    if exception:
        logger.info('Skipping atom feed link rewrite due to errors...')
    else:
        logger.info('Rewriting atom feed...')

    for tag in TAGS:
        _rewrite_feed(app, tag)


def _rewrite_feed(app, tag):
    feed_url = urljoin(app.config.blog_baseurl, 'archive/atom.xml')

    feed_path = os.path.join(app.outdir, 'blog/archive/tag/{tag}/atom.xml'.format(tag=tag))
    rewritten_feed_path = os.path.join(
        app.outdir, 'blog/archive/tag/{tag}/atom_absolute.xml'.format(tag=tag)
    )

    if not os.path.isfile(feed_path):
        logger.error('Atom feed does not exist at: {}'.format(feed_path))
        return

    doc = etree.parse(feed_path)
    root = doc.getroot()

    # Rewrite the namespace map to not be Null
    namespace = list(root.nsmap.values())[0]
    nsmap = {'atom': namespace}

    # Convert the content nodes to use absolute links
    for content in root.xpath('//atom:entry/atom:content', namespaces=nsmap):
        html_content = html.fromstring(content.text)
        html_content.make_links_absolute(feed_url)
        content.text = html.tostring(html_content)

    with open(rewritten_feed_path, 'wb') as fd:
        doc.write(fd)
        logger.info('Wrote absolute atom feed to {}'.format(rewritten_feed_path))
