.. meta::
   :description: A series of events for technical writers,
                 documentarians,
                 and all those who write the docs.
   :author: Write the Docs
   :geo.placename: Worldwide

Welcome to our community!
=========================

**Write the Docs** is a global community of people who care about documentation.

We consider everyone who cares about communication, documentation, and
their users to be a member of our community. This can be programmers,
tech writers, developer advocates, customer support, marketers, and anyone else who wants
people to have great experiences with software.

Upcoming conferences
--------------------

.. container:: home-next

   .. include:: /include/conf/current.rst
      :start-after: current-conferences-list

See all :doc:`our conferences </conf/index>` from past years.

Get involved
------------

.. raw:: html

   <ul class="home-doors">
     <li><strong><a href="/slack/">Join our Slack network</a></strong>
         <p>Over {{ slack_members }} people hanging out and chatting about documentation.</p></li>
     <li><strong><a href="/newsletter/">Read the newsletter</a></strong>
         <p>A monthly roundup of what our community is talking about, for over {{ newsletter_subs }} subscribers.</p></li>
     <li><strong><a href="/topics/">Browse by topic</a></strong>
         <p>Over 700 talks and newsletter articles, on everything from API docs to getting hired.</p></li>
     <li><strong><a href="/meetups/">Find a local meetup</a></strong>
         <p>Local and virtual groups in over {{ meetup_cities }} cities, run by volunteers.</p></li>
{% if salary_survey.open %}     <li><strong><a href="{{ salary_survey.url }}">Take the salary survey</a></strong>
         <p>Anonymous pay data for documentation roles. The {{ salary_survey.year }} survey
            closes {{ salary_survey.closes }}, and <a href="/surveys/">past results</a> are free to read.</p></li>
{% else %}     <li><strong><a href="/surveys/">See the salary survey</a></strong>
         <p>Anonymous pay data for documentation roles, published free every year.</p></li>
{% endif %}
     <li><strong><a href="/sponsorship/">Become a sponsor</a></strong>
         <p>Reach documentarians through our conferences, newsletter, Slack and website.</p></li>
   </ul>

More from Write the Docs
------------------------

.. rst-class:: home-more

* Watch past conference talks on our `YouTube channel <https://www.youtube.com/c/WritetheDocs>`_
* Subscribe to our :doc:`conference announcement </newsletter>` mailing lists
* Read the latest in our :doc:`blog </blog/index>`
* Read our :doc:`software documentation guide </guide/index>`
* Read our :doc:`Hiring Guide </hiring-guide/index>` to get started in the industry
* Join our :doc:`book club </book-club/index>`
* See all :doc:`learning resources </about/learning-resources>`
* Learn about :doc:`our organization <about/about-the-org>`

We're glad you stopped by!
We hope you'll join us either online or in-person for an event soon.

.. The sidebar nav is built from ``extra_nav_links`` in conf.py, so this only
   needs to register the pages, not render a second copy of it on the page.

.. toctree::
   :hidden:
   :glob:
   :maxdepth: 1

   conf/index
   slack
   meetups/index
   newsletter
   topics
   blog/index
   guide/index
   surveys/index
   hiring-guide/index
   book-club/index
   sponsorship/index
   about/*

.. toctree::
   :hidden:
   :glob:
   :maxdepth: 1

   *
   conf/*
   conf/atlantic/*/*
   conf/atlantic/*/*/*
   conf/portland/*/*
   conf/portland/*/*/*
   conf/prague/*/*
   conf/prague/*/*/*
   conf/cincinnati/*/*
   conf/cincinnati/*/*/*
   conf/australia/*/*
   conf/australia/*/*/*
   conf/vilnius/*/*
   conf/vilnius/*/*/*
   conf/kenya/*/*
   conf/kenya/*/*/*
   conf/cfp/*
   book-club/*/*
   conf/berlin/*/*
   conf/berlin/*/*/*
