Testing your Documentation
==========================

:author: Eric Holscher
:last-updated: February 13, 2017

Testing your documentation allows you to make sure it is in a consistent state.
Doing this gives your users a better experience,
and reduces stress around common issues as a writer.

Continuous Integration
----------------------

The most useful tests are run on each commit of your project.
This is called **Continuous Integration**,
and is a common practice in the software development world.

We recommend checking out the following tools to get started:

* Travis CI (GitHub only, free for open source)
* AppVeyor (Windows support, free for open source)
* Jenkins (Install yourself)

Build Errors
------------

The easiest automated check to do is to make sure your documentation builds properly.
This requires simply running your documentation tool,
and checking that it has properly built your documentation.

Most tools will return an *error code* of 0 if the process is successful.
This means you should just be able to do a normal build of your tool,
and your testing tool will know if it is successful or not.

Link Testing
------------

Making sure all the hyperlinks in your docs are working is a really great place to start.
This makes sure your users don't hit dead ends,
and is quite simple in terms of automation.

You can either:

* Use a tool provided with your documentation tools
* Treat your rendered documentation as a normal website, and use a website link checker

These are the tools we know with proper link checking:

Sphinx
~~~~~~

Sphinx ships with a ``linkcheck`` `builder <http://www.sphinx-doc.org/en/stable/builders.html>`_ as a default.
You can run it with a simple::

    make linkcheck

It's output looks something like this:

.. image:: /_static/img/guide/sphinx-linkcheck.png

Jekyll
~~~~~~

Jekyll has a few plugins that support link checking:

* https://github.com/endymion/link-checker
* https://github.com/fastly/jekyll-sanity-checker

Style Guide Checking
--------------------

Another common thing is to use testing to enforce your style guide.
Here are a few links that might be interesting:

* https://www.mapbox.com/blog/retext-mapbox-standard/
* https://krausefx.com/blog/writing-automated-tests-for-your-documentation

