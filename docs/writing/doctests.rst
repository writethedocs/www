############
Use doctests
############

Documentation often holds examples, but what if examples are wrong?
**Doctests are a way to check that examples actually work, and help you maintain
documentation along with your project.**


*********
The story
*********

Here is a common fail pattern:

* Implement some feature in your project.

* Write down an example in documentation.

* [success] => users can follow the example to use the feature.

* Later, the feature is being updated...
* ... but, for some reason (usually omission), the documentation isn't.

* [fail] => the example in documentation is broken. Users think the feature is
  broken too.

* [fail] => you are not told about the issue, except if an user reports it.
  The issue could live silently long time.

Here is how doctests help:

* Implement some feature in your project.

* Write down an example in documentation, and turn it into a doctest.

* [success] => users can follow the example to use the feature.

* Later, the feature is being updated...

* ... but, for some reason (usually omission), the documentation isn't.

* [alert] => your are warned that the doctest fails

* The example is updated so that the doctest pass.

* [success] => users can follow the example to use the feature.


*****
Tools
*****

For `Sphinx`_ users, `Sphinx doctest extension`_ allows you to create doctests
using `Python`_ code.


*******
Example
*******

Here is an example using `Sphinx doctest extension`_ (this documentation is
using Sphinx).

Here, we simply assert that running ``1 + 1`` in Python returns ``2``.

.. doctest::

   >>> 1 + 1
   2


**********
References
**********

.. target-notes::

.. _`Sphinx`: http://sphinx-doc.org/
.. _`Sphinx doctest extension`: http://sphinx-doc.org/ext/doctest.html
.. _`Python`: http://python.org
