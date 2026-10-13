:template: community/index.html

.. meta::
   :description: A series of events for technical writers,
                 documentarians,
                 and all those who write the docs.
   :author: Write the Docs
   :geo.placename: Worldwide

.. The front page. community/index.html adds the hero at the top; each section
   below is a full-width band (see the home-* rules in _community.scss).

Welcome to our community!
=========================

.. rst-class:: home-section

Upcoming conferences
--------------------

.. raw:: html

   <ul class="home-conferences">
   {%- for conf in community.upcoming_conferences %}
     <li>
       <a href="{{ conf.url }}">
         <span class="home-conference__logo">
         {%- if conf.logo %}
           <img src="/{{ conf.logo }}" alt="" loading="lazy">
         {%- else %}
           <span aria-hidden="true">Write<br>the<br>Docs<br>{{ conf.name }}<br>{{ conf.year }}</span>
         {%- endif %}
         </span>
         <span class="home-conference__text">
           <strong>{{ conf.title }}</strong>
           <span>{{ conf.dates }}</span>
           <span>{{ conf.location }}</span>
           <span class="home-conference__cta">Visit the conference site</span>
         </span>
       </a>
     </li>
   {%- endfor %}
   </ul>

.. rst-class:: home-section__more

See :doc:`all our conferences </conf/index>`, past and present.

.. rst-class:: home-section home-section--muted

Get involved
------------

.. raw:: html

   <ul class="home-tiles">
     <li>
       <span class="home-tiles__icon">{% include "community/icons/slack.svg" %}</span>
       <h3><a href="/slack/">Join our Slack</a></h3>
       <p>Over {{ slack_members }} people hanging out and chatting about documentation.</p>
     </li>
     <li>
       <span class="home-tiles__icon">{% include "community/icons/meetups.svg" %}</span>
       <h3><a href="/meetups/">Find a local meetup</a></h3>
       <p>Local and virtual groups in over {{ meetup_cities }} cities, run by volunteers.</p>
     </li>
     <li>
       <span class="home-tiles__icon">{% include "community/icons/newsletter.svg" %}</span>
       <h3><a href="/newsletter/">Read the newsletter</a></h3>
       <p>A monthly roundup of what our community is talking about, for over {{ newsletter_subs }} subscribers.</p>
     </li>
     <li>
       <span class="home-tiles__icon">{% include "community/icons/topics.svg" %}</span>
       <h3><a href="/topics/">Browse by topic</a></h3>
       <p>Over 700 talks and newsletter articles, on everything from API docs to getting hired.</p>
     </li>
     <li>
       <span class="home-tiles__icon">{% include "community/icons/survey.svg" %}</span>
   {%- if salary_survey.open %}
       <h3><a href="{{ salary_survey.url }}">Take the salary survey</a></h3>
       <p>Anonymous pay data for documentation roles. The {{ salary_survey.year }} survey
          closes {{ salary_survey.closes }}, and <a href="/surveys/">past results</a> are free to read.</p>
   {%- else %}
       <h3><a href="/surveys/">See the salary survey</a></h3>
       <p>Anonymous pay data for documentation roles, published free every year.</p>
   {%- endif %}
     </li>
     <li>
       <span class="home-tiles__icon">{% include "community/icons/sponsor.svg" %}</span>
       <h3><a href="/sponsorship/">Become a sponsor</a></h3>
       <p>Reach documentarians through our conferences, newsletter, Slack and website.</p>
     </li>
   </ul>

.. rst-class:: home-section

What is Write the Docs?
-----------------------

.. container:: home-split

   .. container::

      Write the Docs is a global community of people who care about documentation.
      We consider everyone who cares about communication, documentation, and their users
      to be a member of our community. This can be programmers, tech writers, developer advocates,
      customer support, marketers, and anyone else who wants people to have great experiences with software.

      Since starting in Portland, Oregon in 2013, we've run conferences around the world,
      and :doc:`volunteers </about/about-the-org>` keep everything going.

   .. raw:: html

      <img src="/_static/conf/images/headers/2026/writing-day.jpg" alt="Attendees working together at Writing Day" loading="lazy">

.. rst-class:: home-section home-section--muted

More from Write the Docs
------------------------

.. rst-class:: home-links

* Watch past conference talks on our `YouTube channel <https://www.youtube.com/c/WritetheDocs>`_
* Subscribe to our :doc:`conference announcement </newsletter>` mailing lists
* Read the latest in our :doc:`blog </blog/index>`
* Read our :doc:`software documentation guide </guide/index>`
* Read our :doc:`Hiring Guide </hiring-guide/index>` to get started in the industry
* Join our :doc:`book club </book-club/index>`
* See all :doc:`learning resources </about/learning-resources>`
* Learn about :doc:`our organization <about/about-the-org>`

.. The header menu comes from _data/community.yaml, so these toctrees only
   register the pages; they don't render anything.

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
