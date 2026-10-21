:template: community/index.html
:og:description: Write the Docs is a global community of people who care about documentation. Join over {{ slack_members }} documentarians in Slack, at meetups, and at our conferences around the world.
:banner: _static/conf/images/photos/audience-berlin-55523762940.jpg

.. meta::
   :description: Write the Docs is a global community of people who care about
                 documentation. Join over {{ slack_members }} documentarians in Slack,
                 at meetups, and at our conferences around the world.
   :author: Write the Docs
   :geo.placename: Worldwide

.. The front page. community/index.html adds the hero at the top; each section
   below is a full-width band (see the home-* rules in _community.scss). The
   hero and the "Get involved" tiles come from `home` in _data/community.yaml.

A global community of people who care about documentation
==========================================================

.. A welcome to the new website, until `new_website_welcome` in conf.py ends.

{% if new_website_welcome %}
.. rst-class:: home-section home-section-muted home-welcome

Welcome to the new website
--------------------------

Our community pages now share the design of our conference sites,
with a simpler menu and a photo from our events on every page.
{% endif %}

.. rst-class:: home-section

Upcoming conferences
--------------------

.. raw:: html

   {% filter indent(3) %}{% include "community/conference-cards.html" %}{% endfilter %}

.. rst-class:: home-section-more

See :doc:`all our conferences </conf/index>`, past and present.

.. rst-class:: home-section home-section-muted

Get involved
------------

.. raw:: html

   <ul class="home-tiles">
   {%- for tile in community.home.tiles %}
     <li>
       <span class="home-tiles__icon">{% include "community/icons/" ~ tile.icon ~ ".svg" %}</span>
       <h3><a href="{{ tile.link }}">{{ tile.title }}</a></h3>
       <p>{{ tile.text }}</p>
     </li>
   {%- endfor %}
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

      Since starting in Portland, Oregon in 2013, we've run conferences around the world.
      Meet the :doc:`team </team>` that keeps everything going.

   .. raw:: html

      <img src="/_static/conf/images/photos/writing-day-table-55246793808.jpg" alt="Attendees writing together at Writing Day" loading="lazy">

.. rst-class:: home-section home-section-muted

More from Write the Docs
------------------------

.. rst-class:: home-links

* Watch past conference talks on our `YouTube channel <https://www.youtube.com/c/WritetheDocs>`_
* Subscribe to our :doc:`conference announcement </newsletter>` mailing lists
* Read the latest in our :doc:`blog </blog/index>`
* Read our :doc:`software documentation guide </guide/index>`
* Read our :doc:`Hiring Guide </hiring-guide/index>` to get started in the industry
* See all :doc:`learning resources </about/learning-resources>`
* Learn about :doc:`our organization <about/about-the-org>`

.. The first toctree lists the site's sections, in the header menu's order.
   Each section's page lists its own pages in a toctree, which gives every
   page its breadcrumbs and its current item in the header menu. The menu
   itself comes from _data/community.yaml. The second toctree registers
   every other page. Neither renders anything.

.. toctree::
   :hidden:
   :maxdepth: 1

   conf/index
   about/learning-resources
   about/stay-connected
   about/about-the-org

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
