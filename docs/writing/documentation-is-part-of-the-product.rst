####################################
Documentation is part of the product
####################################

Consider the documentation as a component of your product, i.e. don't package
it as an external product or as an option.

In software development, your "product" is usually made of the software, which
itself is usually based on source code.


********************************************
Include documentation in production workflow
********************************************

* Add it to the definition of done (see `scrum development method`_)
* Package and release documentation with code
* A problem in documentation is called a bug, as any problem in code
* Changes in documentation can be prioritized as any feature
* A new version of documentation implies a new version of the product.


**********************************
Synchronize code and documentation
**********************************

Make sure that, for a given version of your product, you can get the adequate
version of the documentation, and vice-versa.

Easiest way to do so is to manage documentation and code in the same version
control repository.

Otherwise, at least create releases of documentation when you create releases
of the product. And you should automate this task.


****************************************************
In release-based workflows, use static documentation
****************************************************

.. note::

   This recommendation may not apply if your production workflow doesn't
   include releases.

Several platforms, such as Github, propose a wiki service. It's a true
temptation to use a wiki to host documentation:

* it's collaborative,
* it can be versionned,
* it's a good place to receive contributions. It's visible and easy to use.

So it seems suitable to serve documentation, but:

* it's easier to synchronize versions and branches of documentation and code
  when they live in the same repository. Will you create a branch or version
  of wiki for each branch or version of code?

* wiki is a kind of "live" content. It's meant to receive continuous and
  spontaneous contributions. It is not meant to be included in a development
  workflow with tickets, commits, code reviews, merges, releases and support.

So, for documentation of release-based products, use tools like `Sphinx`_
rather than wiki services.

On the contrary, wikis may be more suitable than static documentation for
use cases where "live content" or "community-made content" are most valuable
features:

* encyclopedia
* community articles about a web application which is live (only current
  production version matters).


**********
References
**********

.. target-notes::

.. _`scrum development method`:
   https://en.wikipedia.org/wiki/Scrum_%28development%29
.. _`Sphinx`: http://sphinx.pocoo.org
