# By Gareth Rees
# http://gareth-rees.livejournal.com/27148.html

import html5lib
import html5lib.serializer
import html5lib.treewalkers
import urlparse

# List of (ELEMENT, ATTRIBUTE) for HTML5 attributes which contain URLs.
# Based on the list at http://www.feedparser.org/docs/resolving-relative-links.html
url_attributes = [
    ('a', 'href'),
    ('applet', 'codebase'),
    ('area', 'href'),
    ('blockquote', 'cite'),
    ('body', 'background'),
    ('del', 'cite'),
    ('form', 'action'),
    ('frame', 'longdesc'),
    ('frame', 'src'),
    ('iframe', 'longdesc'),
    ('iframe', 'src'),
    ('head', 'profile'),
    ('img', 'longdesc'),
    ('img', 'src'),
    ('img', 'usemap'),
    ('input', 'src'),
    ('input', 'usemap'),
    ('ins', 'cite'),
    ('link', 'href'),
    ('object', 'classid'),
    ('object', 'codebase'),
    ('object', 'data'),
    ('object', 'usemap'),
    ('q', 'cite'),
    ('script', 'src')]

def absolutify(src, base_url):
    """absolutify(SRC, BASE_URL): Resolve relative URLs in SRC.
SRC is a string containing HTML. All URLs in SRC are resolved relative
to BASE_URL. Return the body of the result as HTML."""

    # Parse SRC as HTML.
    tree_builder = html5lib.treebuilders.getTreeBuilder('dom')
    parser = html5lib.html5parser.HTMLParser(tree = tree_builder)
    dom = parser.parse(src)

    # Handle <BASE> if any.
    head = dom.getElementsByTagName('head')[0]
    for b in head.getElementsByTagName('base'):
        u = b.getAttribute('href')
        if u:
            base_url = urlparse.urljoin(base_url, u)
            # HTML5 4.2.3 "if there are multiple base elements with href
            # attributes, all but the first are ignored."
            break

    # Change all relative URLs to absolute URLs by resolving them
    # relative to BASE_URL. Note that we need to do this even for URLs
    # that consist only of a fragment identifier, because Google Reader
    # changes href=#foo to href=http://site/#foo
    for tag, attr in url_attributes:
        for e in dom.getElementsByTagName(tag):
            u = e.getAttribute(attr)
            if u:
                e.setAttribute(attr, urlparse.urljoin(base_url, u))

    # Return the HTML5 serialization of the <BODY> of the result (we don't
    # want the <HEAD>: this breaks feed readers).
    body = dom.getElementsByTagName('body')[0]
    tree_walker = html5lib.treewalkers.getTreeWalker('dom')
    html_serializer = html5lib.serializer.htmlserializer.HTMLSerializer()
    return u''.join(html_serializer.serialize(tree_walker(body)))
    

# Alternative option, from http://stackoverflow.com/questions/589833/how-to-find-a-relative-url-and-translate-it-to-an-absolute-url-in-python/589939#589939
# 
# import re, urlparse
# 
# find_re = re.compile(r'\bhref\s*=\s*("[^"]*"|\'[^\']*\'|[^"\'<>=\s]+)')
# 
# def fix_urls(document, base_url):
#     ret = []
#     last_end = 0
#     for match in find_re.finditer(document):
#         url = match.group(1)
#         if url[0] in "\"'":
#             url = url.strip(url[0])
#         parsed = urlparse.urlparse(url)
#         if parsed.scheme == parsed.netloc == '': #relative to domain
#             url = urlparse.urljoin(base_url, url)
#             ret.append(document[last_end:match.start(1)])
#             ret.append('"%s"' % (url,))
#             last_end = match.end(1)
#     ret.append(document[last_end:])
#     return ''.join(ret)
