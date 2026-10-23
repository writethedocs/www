Testing your documentation
==========================

Testing your documentation allows you to make sure it is in a consistent state.
Doing this gives your users a better experience,
and reduces stress around common issues as a writer.

This `article <https://opensource.com/business/15/7/continuous-integration-and-continuous-delivery-documentation>`_ by Anne Gentle is a good place to start to understand this concept.

Continuous integration
----------------------

The most useful tests are run on each commit of your project.
This is called **Continuous Integration**,
and is a common practice in the software development world.

We recommend checking out the following tools to get started:

* `GitHub Actions <https://docs.github.com/en/actions>`_ (built into GitHub, free for public repositories)
* `GitLab CI/CD <https://docs.gitlab.com/ci/>`_ (built into GitLab)

Build errors
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

* Sphinx has `nitpicky mode <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpicky>`_.
* Jekyll has `strict mode <https://jekyllrb.com/docs/configuration/#liquid-options>`_.

Link testing
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

Sphinx ships with a ``linkcheck`` `builder <https://www.sphinx-doc.org/en/master/usage/builders/index.html>`_ as a default.
You can run it with a simple::

    make linkcheck

Its output looks something like this:

.. image:: /_static/img/guide/sphinx-linkcheck.png

HTMLProofer
~~~~~~~~~~~

`HTMLProofer <https://github.com/gjtorikian/html-proofer>`_ checks links in
HTML, as well as images, titles and tag validity.
It works with the output of any static site generator, including Jekyll.
This site uses it in CI.

Style guide checking and linting
----------------------------------

Linters are tools that automatically verify specific rules against your code or
documentation. This is useful for enforcing a style guide, or for catching
commonly mistaken branding issues.

Here are a few links that might be interesting:

* https://blog.mapbox.com/regulating-english-with-retext-mapbox-standard-d79a8158f251
* https://krausefx.com/blog/writing-automated-tests-for-your-documentation


Vale
----

Vale is a syntax-aware linter for prose built for speed and extensibility.

* `Vale website <https://vale.sh/>`_
* `Vale documentation <https://vale.sh/docs/>`_

Vale doesn't ship with any styles.
Instead, you add ready-made packages from the `Vale Package Hub <https://vale.sh/explorer>`_,
including implementations of the Microsoft Writing Style Guide, the Google Developer Documentation Style Guide,
Proselint, Write-good, and Joblint.

To get started, follow the `installation instructions <https://vale.sh/docs/install>`_ for your platform.

Then add a ``.vale.ini`` configuration file. For some examples, see:

* https://github.com/writethedocs/www/blob/main/vale/vale.ini
* https://github.com/cockroachdb/docs/blob/master/.vale.ini
* https://github.com/linode/docs/blob/develop/.vale.ini

The configuration file can live anywhere, but the root of your repository
is usually the most convenient place, since Vale finds it automatically.

Once configured, run ``vale sync`` to download the packages listed in your configuration,
and ``vale ls-config`` to confirm Vale picked up your settings.

You can then apply Vale as a grammar linter directly to your source files, with
a command like::

    vale /path/to/someText.md

Hint: Vale even works with XML files, such as those in DocBook and DITA, as long
as you've included `*.xml` in the Vale configuration file.

.. seealso::

   Browse talks and newsletter articles about :ref:`automation <topics:Automation>` in our content archive.
