How to write software documentation
====================================

There is a magical feeling that comes from releasing code.
The feeling is a mix of terror and excitement.
You're eager to tell the world about your new project but despair at where to start. Even professional writers 
know the mixed emotions caused by a blank page.

Good software documentation helps relieve that fear. So, have no fear! Use this guide to document your first open-source project for 
public release. 

.. _why:

Why write software documentation?
---------------------------------------

Understand your code in 6 months
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your code from 6 months ago looks like code that someone else wrote.
Things once obvious are now unclear and you now empathize with potential 
users who need good documentation.

Get people to use your code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just like code comments explain the *why* and not the *how*, software documentation states the *why* behind the code.
Good documentation solves a few 
common reasons people won't use your code:

* They don't know why your project exists or how it meets their needs.
* They can't find how to install your code.
* They can't see how to use your code.

Few people will source dive to use code, but most 
people will use properly documented code.
Therefore, if you love your project, document it so others can use it.

Increase contributions to your code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Potential contributors need help through documentation. Documentation also provides another way for people to contribute and, for people who have never contributed, documentation changes may be easier than code changes.
Overall, without documentation, you impede or even lose contributors.

Improve your code
~~~~~~~~~~~~~~~~~~

The process of creating documentation requires focused thought that improves code design.
Writing out API and design decisions allows you to formally think about them.
Documentation also allows people to contribute code that follows your original intentions.

Improve your technical writing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Technical writing is a useful skill for programmers, but it requires different writing skills than most people have naturally.
Writing documentation makes you a better technical writer. Technical writing becomes easier over time so maintain your writing skill by documenting your projects.

Start simple to achieve the best results.

.. _write:

What to include in software documentation
------------------------------------------

Give users the information they need, but not too much.

First, know which of these common audiences you're writing for:

* Users - want to use your code and don't care how it works.
* Developers - want to contribute to your code.

Show what problem your code solves
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People use your docs to learn about your project. 
Perhaps they will hear about your project from others or will find it from a search engine. 
Regardless, clearly state what your project does and why. 

Fabric_ does a great job of this.

.. _Fabric: http://docs.fabfile.org/

Provide a small code example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show a common example use case for your project. 

Requests_ is a great example.

.. _Requests: https://requests.kennethreitz.org/en/master/

Link to your code and issue tracker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People sometimes browse the code. They might want to file bugs for issues they've found, 
so make your code easy to contribute. 

The `Python Guide`_ does a good job of this.

.. _Python Guide: http://docs.python-guide.org/en/latest/index.html

Create frequently asked questions (FAQs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many people have the same problems. If certain issues happen often, fix your documentation or the code 
to resolve the issues. However, there are always questions about your project, things that can't be changed, etc. 
Document those in an FAQ and **keep them up to date**. 

FAQs get outdated fast but are a great resource when done well. 

Tastypie_ did a great job of this with their "Cookbook" concept.

.. _Tastypie: http://django-tastypie.readthedocs.org/en/latest/cookbook.html

Tell how to get support
~~~~~~~~~~~~~~~~~~~~~~~~

Whether from a mailing list or IRC Channel, document how to get help and interact with the community. 

Django_ does a great job at this.

.. _Django: https://docs.djangoproject.com/en/1.8/faq/help

Show how to contribute
~~~~~~~~~~~~~~~~~~~~~~~

People have their own expectations of how to contribute. Document your contribution process so that contributions follow the standards for your project. 

`Open Comparison`_ does a great job of this.

.. _Open Comparison: https://packaginator.readthedocs.io/en/latest/contributing.html

Provide installation instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once people decide to use your code, they need to install and run it. Keep your install instructions to a couple of lines for the basic case. Link to a page with more information and any caveats. 

`Read the Docs`_ does a good job with this.

.. _Read the Docs: http://read-the-docs.readthedocs.org/en/latest/install.html

State your project's license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BSD? MIT? GPL? A project's license might not matter to you, but the people who want to use your code will care. Think about what you want to accomplish with your license and only pick one standard license.

.. _template:

Next steps for software documentation
--------------------------------------

After following this guide,
we know your code is ready for success!
But, if you'd like to learn more,
see `how to maintain an open source project`_.

.. _how to maintain an open source project: https://medium.com/p/aaa2a5437d3a

Tools for writing software documentation
-----------------------------------------

Programmers live in a world of plain text.
Their documentation tooling and workflows should function similarly while being powerful and easy to use.
Writing tools should turn plain text into pretty HTML and track changes to files.

A basic markup example
~~~~~~~~~~~~~~~~~~~~~~~

::

	Resources
	---------

	* Online documentation: http://docs.writethedocs.org/
	* Conference: http://conf.writethedocs.org/

This will render a nice HTML header and a list with automatically hyperlinked URLs.
It's easy to write and still makes sense as plain text.

.. _markup_languages:

.. sidebar:: Sidebar on markup languages.

   The examples in this document are both valid `Markdown`_ and `reStructuredText`_.
   reStructuredText is a bit harder to use,
   but is more powerful. Check them both out.

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Markdown: http://daringfireball.net/projects/markdown/


README template
~~~~~~~~~~~~~~~~

Your project's README is often the first time users interact with your project. Therefore, having a solid README is key.
Code hosting services automatically render your README into HTML if you provide the proper extension.

Some people even `start a project with a README`_.

.. _start a project with a README: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html

Below is a simple ``README`` template to start with.
Name the file ``README.md`` to use markdown,
or ``README.rst`` to use reStructuredText.

::

	$project
	========

	$project solves the problem of where to start with documentation
	by providing a basic explanation of how to do it easily:

	    import project
	    # Get your stuff done
	    project.do_stuff()

	Features
	--------

	- Be awesome
	- Make things faster

	Installation
	------------

	Install $project by running:

	    install project

	Contribute
	----------

	- Issue Tracker: github.com/$project/$project/issues
	- Source Code: github.com/$project/$project

	Support
	-------

	Let us know if you have issues.
	See our mailing list at: project@google-groups.com

	License
	-------

	The project is licensed under the BSD license.
