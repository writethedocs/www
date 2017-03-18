"""
Use like::

python make-email.py http://www.writethedocs.org/conf/na/2016/news/thanks-for-coming/

Requires a `pip install pyquery`

On OS X you can do::

python make-email.py http://www.writethedocs.org/conf/na/2016/news/thanks-for-coming/ |pbcopy

To copy things into the clip board

"""
import re
import sys
from pyquery import PyQuery as pq

url = sys.argv[1]
# print "Getting blog %s" % url


d = pq(url=url)
content = d('.col-content').html()
if not content:
    content = d('.body').html()
    # Remove page title
    d = pq(content)
    d.find('span').remove()
    d.find('h1').remove()
    content = d.html()
# Remove header links
content = re.sub(r'<a class="headerlink" .+</a>', '', content)


print content
