:template: {{cookiecutter.year}}/{{cookiecutter.continent}}-content.html


Schedule
========

Write the Docs is more than a conference. Each year we organize a wide
range of events so that people can come together, collaborate, and learn
from each other in different ways.

TODO:  Date, Day
----------------

{% if cookiecutter.continent == "na" %}

The only event scheduled on Saturday is the :doc:`annual hike to Pittock Mansion </conf/{{cookiecutter.continent}}/{{cookiecutter.year}}/hike>`.
If you get into town early,
join us on the hike and take the chance to explore Portland in all of its glory.

The hike starts at **2pm** on Saturday.

{% endif %}

Sunday, TODO: Date
---------------

The Writing Day, Workshops, & Reception will be held at TODO:.

During the day, we'll hold our :doc:`Writing Day documentation
sprints </conf/{{cookiecutter.continent}}/{{cookiecutter.year}}/writing-day>`, followed by the conference
reception in the evening. We also have two half-day :doc:`workshops </conf/{{cookiecutter.continent}}/{{cookiecutter.year}}/workshops>`
running in parallel with the writing day.

We encourage everyone to drop by on Sunday evening for the conference
reception. You'll have a chance to get acquainted with each other over
some drinks and snacks. We'll also help groups organize dinner plans, so
you can continue your conversations over more substantial food as well.

Writing Day Schedule (Free for attendees)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`Learn more</conf/{{cookiecutter.continent}}/{{cookiecutter.year}}/writing-day>` about Writing Day.

.. datatemplate::
   :source: /_data/{{cookiecutter.continent}}-{{cookiecutter.year}}-writing-day.yaml
   :template: include/schedule{{cookiecutter.year}}.rst

Monday, TODO: Dat
----------------

The main conference will take place at the **Crystal Ballroom located at 1332 W
Burnside St**.

This is the main event! Hear from lots of interesting folks about all
things documentation.

Main Stage
^^^^^^^^^^^

.. datatemplate::
   :source: /_data/{{cookiecutter.continent}}-{{cookiecutter.year}}-day-1.yaml
   :template: include/schedule{{cookiecutter.year}}.rst

TODO: location
^^^^^^^^^^^^^

:doc:`/conf/{{cookiecutter.continent}}/{{cookiecutter.year}}/unconference` from 1pm-5pm, these run in parallel to the main talks.

Monday Night - Party
^^^^^^^^^^^^^^^^^^^^^^

The party will start at **7pm**.
It will be at the TODO:.

The party is for **conference attendees only**. Please bring your badge, as it
is an official conference event.

There will be light dinner and drinks available on the conference while our tab lasts.

Tuesday, TODO
---------------

The talks will take place at the **Crystal Ballroom located at 1332 W
Burnside St**.

Main Stage
^^^^^^^^^^^

.. datatemplate::
   :source: /_data/{{cookiecutter.continent}}-{{cookiecutter.year}}-day-2.yaml
   :template: include/schedule{{cookiecutter.year}}.rst

TODO: location
^^^^^^^^^^^^^^^

:doc:`/conf/{{cookiecutter.continent}}/{{cookiecutter.year}}/unconference` from 9am-3pm,  these run in parallel to the main talks.
