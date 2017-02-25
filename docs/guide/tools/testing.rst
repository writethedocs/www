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

* `Travis CI <http://travis-ci.org>`_ (GitHub only, free for open source)
* `AppVeyor <https://www.appveyor.com/>`_ (Windows support, free for open source)

Build Errors
------------

The easiest automated check to do is to make sure your documentation builds
properly. This requires simply running your documentation tool, and checking
that it has properly built your documentation.

Most tools will return an *error code* of 0 if the process is successful. This
means you should just be able to do a normal build of your tool, and your
testing tool will know if it is successful or not.

If your build tool has a *picky* mode that flags warnings that *might* be
problematic as well as errors, it might make sense to switch it on, but you'll
want to make sure that your documentation is in good shape before you do.

* Sphinx has `nitpicky mode <http://www.sphinx-doc.org/en/stable/config.html#confval-nitpicky>`_.
* Jekyll has `strict mode <https://jekyllrb.com/docs/configuration/#liquid-options>`_.

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

HTMLProofer
~~~~~~~~~~~

`HTMLProofer <https://github.com/gjtorikian/html-proofer>`_ checks links in
HTML, as well as images, titles and tag validity.

Style Guide Checking and Linting
----------------------------------

Linters are tools that automatically verify specific rules against your code or
documentation. This is useful for enforcing a style guide,or for catching
commonly mitaken branding issues.

Here are a few links that might be interesting:

* https://www.mapbox.com/blog/retext-mapbox-standard/
* https://krausefx.com/blog/writing-automated-tests-for-your-documentation


Write Good
----------

"Naive linter for English prose for developers who can't write good and wanna
learn to do other stuff good too."

https://github.com/btford/write-good

This linter is a prose linter for English.
It has a number of checks for things like:

* Passive voice
* Lexical illusions
* Weasel words

It works as a command line interface or a JavaScript library.
