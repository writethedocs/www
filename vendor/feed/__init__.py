from fsdict import FSDict
import feedgenerator
from urllib import quote_plus
import os.path
from feeddirectives import Latest
from feednodes import latest
from sphinx.addnodes import toctree
from docutils import nodes


#global
feed_entries = None

#constant unlikely to occur in a docname and legal as a filename
MAGIC_SEPARATOR = '---###---'

def parse_date(datestring):
    try:
        parser = parse_date.parser
    except AttributeError:
        import dateutil.parser
        parser = dateutil.parser.parser()
        parse_date.parser = parser
    return parser.parse(datestring)
    
def setup(app):
    """
    see: http://sphinx.pocoo.org/ext/appapi.html
    this is the primary extension point for Sphinx
    """
    from sphinx.application import Sphinx
    if not isinstance(app, Sphinx): return
    
    app.add_config_value('feed_title', '', 'html')
    app.add_config_value('feed_base_url', '', 'html')
    app.add_config_value('feed_description', '', 'html')
    app.add_config_value('feed_filename', 'rss.xml', 'html')
    
    app.add_directive('latest', Latest)
    app.add_node(latest)
    
    app.connect('build-finished', emit_feed)
    app.connect('builder-inited', create_feed_container)
    app.connect('env-purge-doc', remove_dead_feed_item)
    app.connect('env-purge-doc', purge_dates)
    #I would like to parse dates here, but we aren't supplied the document name in the handler, so it's pointless
    #app.connect('doctree-read', parse_article_date)
    app.connect('html-page-context', create_feed_item)
    app.connect('doctree-resolved', process_latest_toc)

def purge_dates(app, env, docname):
    if not hasattr(env, 'feed_pub_dates'):
        return
    try:
        del(env.feed_pub_dates[docname])
    except KeyError:
        pass

def process_latest_toc(app, doctree, fromdocname):
    """We traverse the doctree looking for publication dates to build the
    date-based ToC here. Since the order in whicih documents are processed is
    ill-defined, from our perspective, we parse all of them each time, but
    cache them in the environment"""

    env = app.builder.env
    cache_article_dates(env)
        
    feed_pub_dates = getattr(env, 'feed_pub_dates', {})
    
    for node in doctree.traverse(latest):
        entries = node['entries']
        includefiles = node['includefiles']
        
        decorated_entries = [
          (feed_pub_dates.get(doc), title, doc)
          for title, doc in entries
          if doc in feed_pub_dates]
        decorated_entries.sort(reverse=True)
        
        latest_list = nodes.bullet_list('',
          classes=['feed-latest-articles'])
        
        for date, title, docname in decorated_entries:
            para = nodes.paragraph()
            list_item = nodes.list_item('', para,
              classes=['feed-dated-article'])
            
            if title is None:
                title = env.titles.get(docname)
                if title:
                    title = title[0] #.astext()

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = title #nodes.emphasis(title, title)
            newnode['refdocname'] = docname
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, docname)
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(' ', ' ')
            stringdate = date.strftime('%Y/%m/%d')
            date_wrapper = nodes.container(classes=['feed-article-date'])
            date_wrapper += nodes.Text(stringdate, stringdate)
            para += date_wrapper

            # Insert into the latestlist
            latest_list.append(list_item)

        node.replace_self(latest_list)

def create_feed_container(app):
    """
    create lazy filesystem stash for keeping RSS entry fragments, since we
    don't want to store the entire site in the environment (in fact, even if
    we did, it wasn't persisting for some reason.)
    """
    global feed_entries
    rss_fragment_path = os.path.realpath(os.path.join(app.outdir, '..', 'rss_entry_fragments'))
    feed_entries = FSDict(work_dir=rss_fragment_path)
    app.builder.env.feed_url = app.config.feed_base_url + '/' + \
        app.config.feed_filename

def cache_article_dates(env):
    # This should only be run once, although currently it is run many times,
    # wasting CPU cycles.
    
    if not hasattr(env, 'feed_pub_dates'):
        env.feed_pub_dates = {}

    feed_pub_dates = env.feed_pub_dates
    
    for docname, doc_metadata in env.metadata.iteritems():
        doc_metadata = env.metadata.get(docname, {})
        if 'date' not in doc_metadata:
            continue #don't index dateless articles
        try:
            pub_date = parse_date(doc_metadata['date'])
            feed_pub_dates[docname] = pub_date
        except ValueError, exc:
            #probably a nonsensical date
            app.builder.warn('date parse error: ' + str(exc) + ' in ' + docname)

def get_date_for_article(env, docname):
    feed_pub_dates = env.feed_pub_dates

    if docname in feed_pub_dates:
        return feed_pub_dates[docname]
  
def create_feed_item(app, docname, templatename, ctx, doctree):
    """
    Here we have access to nice HTML fragments to use in, say, an RSS feed.
    We serialize them to disk so that we get them preserved across builds.
    
    We also inject useful metadata into the context here.
    """
    global feed_entries
    from absolutify_urls import absolutify
    env = app.builder.env
    metadata = env.metadata.get(docname, {})
    pub_date = get_date_for_article(env, docname)
    if not pub_date:
        return
    # RSS item attributes, w/defaults:
    #     title, link, description, author_email=None,
    #     author_name=None, author_link=None, pubdate=None, comments=None,
    #     unique_id=None, enclosure=None, categories=(), item_copyright=None,
    #     ttl=None,
    link = app.config.feed_base_url + '/' + ctx['current_page_name'] + ctx['file_suffix']
    item = {
      'title': ctx.get('title'),
      'link': link,
      'unique_id': link,
      'description': absolutify(ctx.get('body'), link),
      'pubdate': pub_date
    }
    if 'author' in metadata:
        item['author'] = metadata['author']
        
    feed_entries[dated_name(docname, pub_date)] = item
    
    #Now, useful variables to keep in context
    ctx['rss_link'] = app.builder.env.feed_url 
    ctx['pub_date'] = pub_date

def remove_dead_feed_item(app, env, docname):
    """
    TODO:
    purge unwanted crap
    """
    global feed_entries
    munged_name = ''.join([MAGIC_SEPARATOR,quote_plus(docname)])
    for name in feed_entries:
        if name.endswith(munged_name):
            del(feed_entries[name])

def emit_feed(app, exc):
    global feed_entries
    import os.path
    
    title = app.config.feed_title
    if not title:
        title = app.config.project

    feed_dict = {
      'title': title,
      'link': app.config.feed_base_url,
      'feed_url': app.config.feed_base_url,
      'description': app.config.feed_description
    }
    if app.config.language:
        feed_dict['language'] = app.config.language
    if app.config.copyright:
        feed_dict['feed_copyright'] = app.config.copyright
    feed = feedgenerator.Rss201rev2Feed(**feed_dict)
    app.builder.env.feed_feed = feed
    ordered_keys = feed_entries.keys()
    ordered_keys.sort(reverse=True)
    for key in ordered_keys:
        feed.add_item(**feed_entries[key])     
    outfilename = os.path.join(app.builder.outdir,
      app.config.feed_filename)
    fp = open(outfilename, 'w')
    feed.write(fp, 'utf-8')
    fp.close()

def dated_name(docname, date):
    """
    we need convenient filenames which incorporate dates for ease of sorting
    and guid for uniqueness, plus will work in the FS without inconvenient
    characters. NB, at the moment, hour of publication is ignored.
    """
    return quote_plus(MAGIC_SEPARATOR.join([date.isoformat(), docname]))
