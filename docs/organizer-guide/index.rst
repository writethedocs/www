===============
Organizer Guide
===============

Welcome! This guide aims to help anyone who wants to start a local Write the Docs meetup or a regional conference. Our community is growing quickly and we want to provide resources, guidelines, and tips on how to build and maintain events no matter where you are in the world.

All the content in this guide and in the `resources repository <https://github.com/writethedocs/resources>`_ is open source, and we welcome contributions and suggestions! Feel free to communicate and share ideas with your fellow documentarians on `Slack <https://writethedocs.slack.com/>`_ or by creating `issues <https://github.com/writethedocs/www>`_ and `pull requests <https://github.com/writethedocs/www/pulls>`_ in the `GitHub repository <https://github.com/writethedocs/www>`_.

.. note:: There are a number of topics that aren't written yet.
          That means that you can write them!
          Please submit your thoughts and ideas,
          and you can contribute to making this guide better.

You should also look at the :doc:`/team` page to see more information about who is currently filling these roles.

If you're interested in helping start or organize a Write the Docs conference, send us email at support@writethedocs.org.

Meetups
-------

Information about the global Write the Docs :doc:`/meetups/index`.

.. toctree::
   :maxdepth: 2

   meetups/covid-19-meetups
   meetups/starting
   meetups/faq-meetups
   meetups/sustainable-meetups
   meetups/livestreaming-meetups

Newsletter
------------

The nitty-gritty about creating our hand-crafted newsletter.

.. toctree::
   :maxdepth: 2

   newsletter/editorial-guidelines
   newsletter/newsletter-process

Conferences
-----------

Information about our regional Write the Docs conferences.

.. toctree::
   :maxdepth: 2

   confs/start
   confs/checklist
   confs/event-roles
   confs/cfp
   confs/communication
   confs/volunteer-coordination
   confs/volunteer-roles
   confs/registration
   confs/welcome-wagon
   confs/community-events
   confs/website

.. TODO

.. toctree::
   :maxdepth: 2
   :hidden:

   confs/budget
   confs/venues-logistics
   confs/sponsorship
   confs/tickets
   confs/print-resources

We also recommend reading the DevOps Days organizer guide.
They have very similar philosophies and have a great guide as well:

https://devopsdays.org/organizing/

Community Spotlight
-------------------

Information about contributing interview content for the community.

.. toctree::
   :maxdepth: 2

   community-spotlight-interviewing-guide
    
Salary Surveys
--------------

Convert from Google Doc to ReStructuredText:

1. In Google Docs, save the survey as HTML.
2. Use `pandoc <https://pandoc.org/>`__ to convert to RST::

      pandoc -s -f html -t rst SalarySurvey2020.html > survey.rst

3. If the output is full `rubrics` and single-cell tables like this: ::

      +-------------------------------------------------------------+
      | .. rubric:: What we asked                                   |
      |    :name: h.p5d0g4ykb8x1                                    |
      |    :class: c15                                              |
      |                                                             |
      | 1. What is the basis of your employment?                    |
      |                                                             |
      | -  I am an employee                                         |
      | -  I am an independent contractor, freelance operator, or   |
      |    self-employed                                            |
      | -  I was an employee, but am not currently employed         |
      | -  I was an independent contractor, freelance operator, or  |
      |    self-employed, but do not currently have work            |
      +-------------------------------------------------------------+

   use something like the script in `docs/_scripts/fix_gdocs2rst.py` to clean it up.jwqj

4. Add images to `docs/surveys/salary-survey/images`, and include them manually.

5. Triple check output. 😈

Credits
-------

This guide draws much inspiration from the `Django Girls Organizer's Guide <http://organize.djangogirls.org/>`__.
