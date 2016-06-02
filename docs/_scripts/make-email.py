"""
Use like:

python make-email.py http://www.writethedocs.org/conf/na/2016/news/thanks-for-coming/

Requires a `pip install pyquery`
"""
import re
import sys
from pyquery import PyQuery as pq

url = sys.argv[1]
# print "Getting blog %s" % url


d = pq(url=url)
content = d('.section').html()

# Remove header links
content = re.sub(r'<a class="headerlink" .+</a>', '', content)

# Remove page title
d = pq(content)
d.find('span').remove()
d.find('h1').remove()
content = d.html()

print content