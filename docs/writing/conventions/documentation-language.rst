#############################
Choose documentation language
#############################

Recommendation:

* Analyze documentation usage
* Choose a language for the documentation
* If the language choice isn't obvious, write the choice and the reason in the
  documentation

Keep in mind that the language of the documentation is related to documentation
usage: who does read it? Who does write it?


********************************************
English is standard for software development
********************************************

**English is recommended for technical documentations related to software**,
because it's the standard in software industry. Programming languages and code
are written in English. So should be their documentation.


**********************************************
Guidelines for non English-speaking developers
**********************************************

A common scenario in countries where English is not a natural language:

* a team develops software
* some team members don't speak English, or at least not well enough to be
  efficient with English.

So English doesn't sound natural to this team... Let's consider other points
of interest, so that you can base your choice on pragmatic values.

How much is English a useful skill to develop software?
=======================================================

Since most software documentations, articles, tutorials are written in English,
learning English is truly useful. For developers, English language is valuable.

So the question is: in the context of the project, can the team learn English?
If the answer is "yes", then English remains a good choice.
Some helpers:

* do team members actually are interested in learning English?
* compare estimated learning cost to estimated benefits of English skill.

Notice that, if some developers speak English, they can help others while
doing code review or pair programming.

How many foreign-speaking developers contribute to the software?
================================================================

Think about collaboration and maintenance. May external developers contribute
to the project? Which languages could be used for communications?

The documentation language should be one in the list of possibilities.

Notice that, as a universal communication language, English has chances to be
in the list. The more "international" or "open" is your project, the more
English is a good choice.

How much would be a translation?
================================

Whatever the language choice, you may have to translate the documentation one
day. So, if you are not sure about the suitable language, consider the cost of
translation.

If the cost is low, you may try a language now, and wonder about languages
later, when necessary. Just make sure you defined "when necessary".

As an example, if your documentation is about 200 words, you'd better
write it now and translate it later, if necessary, rather than learn English
then write the docs. But, the question should be asked again if the
documentation reaches 5.000 words.


******************
Multiple languages
******************

If only you have to
===================

Support multiple languages if only you have to.

One use case where you have to support multiple languages is a end-user
documentation of an international service:

* you provide a service or product in multiple languages.
* users speak several languages.
* you provide support for this product in multiple languages.
* so the end-user documentation is written in multiple languages.

Then here is an example where multiple languages are not required... You
provide a service to developers. Since your service is world-famous, users
speak various languages. But your interface is user-friendly and most
developers are used to English... so you don't have to localize the end-user
documentation.

If only you can
===============

Support multiple languages if only you can.

Keep in mind that supporting several languages means lot of work: translations,
coordination of translation teams, maintenance.

As an example, if you often release original documentation, you have to
translate often, or translations would be obsolete. And obsolete (i.e. wrong
or incomplete) documentation is generally more harmful than untranslated one.

Sometimes, you can't support multiple languages yourself, but commmunity can.
As an example, `the PHP documentation`_ is available in several languages.
The original documentation is English, then translated in several languages. In
that case, the community is big enough to support the translation process.
In fact, here, original documentation and its translations are managed as
distinct products.

As separated documentations
===========================

When you have to support multiple languages, you'd better create distinct
products (documentations) which are linked, instead of a big product which
contains it all.

Several reasons:

* separate maintenance: if a documentation is broken, it doesn't block others.
* separate contributors: original authors create the reference, then
  translators translate. You shouldn't block the release of original content
  because a translation is missing.


**********
References
**********

.. target-notes::

.. _`the PHP documentation`: http://php.net/docs.php
