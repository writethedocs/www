#!/usr/bin/env python3
"""
Use like::

python make-email.py http://www.writethedocs.org/conf/na/2016/news/thanks-for-coming/

Requires a `pip install pyquery`

On OS X you can do::

python make-email.py http://www.writethedocs.org/conf/na/2016/news/thanks-for-coming/ |pbcopy

To copy things into the clip board

"""
from __future__ import print_function
import re
import sys
from pyquery import PyQuery as pq

url = sys.argv[1]
# print "Getting blog %s" % url


d = pq(url=url)
content = d('.col-content').html()
# import ipdb; ipdb.set_trace();
if not content:
    content = d('.body').html()
    # Remove page title
    d = pq(content)
    d.find('span').remove()
    d.find('h1').remove()
    # Convert images
    for img_obj in d('img'):
        img = pq(img_obj)
        if '../../' in img.attr('src'):
            src = img.attr('src')
            src = src.replace('../../', 'http://www.writethedocs.org/', 1)
            img.attr('src', src)

    content = d.html()
# Remove header links
try:
    content = re.sub(r'<a class="headerlink" .+</a>', '', content)
except:
    pass


print(content)
