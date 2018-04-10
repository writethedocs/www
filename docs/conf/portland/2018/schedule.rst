:template: {{year}}/{{templatecode}}/generic.html
:banner: _static/2018/assets/headers/venue.png

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

Saturday, May 5 - Hike
-----------------------

The only event scheduled on Saturday is the :doc:`annual hike to Pittock Mansion </conf/portland/2018/hike>`.
If you get into town early, join us on the hike and take the chance to explore Portland in all of its glory.

* **Where**: Lower Macleay Park or Macleay Park Entrance.
* **When**: 13:45
* **Details**: :doc:`Annual hike to Pittock Mansion </conf/portland/2018/hike>`

Sunday, May 6 - Writing Day and Reception
---------------------------------------------

The Writing Day and Welcome Reception will be held at the **Crystal Ballroom located at 1332 W Burnside St**.

Writing Day
~~~~~~~~~~~

* **Where**: Main stage, Crystal Ballroom
* **When**: **9am-5pm**
* **Details**: :doc:`Writing Day documentation sprints </conf/portland/2018/writing-day>`

Reception
~~~~~~~~~

We encourage everyone to drop by on Sunday evening for the conference reception.
You'll have a chance to get acquainted with each other over some drinks and snacks.
We'll also help groups organize dinner plans, so you can continue your conversations over more substantial food as well.

* **Where**: Main stage, Crystal Ballroom
* **When**: **5pm-8pm**
* **Details**: TBA

Monday, May 7 - Conference and social
---------------------------------------

.. contents::
    :local:
    :backlinks: none

This is the main event! Hear from lots of interesting folks about all things documentation.
We will have talks all day on the main stage, and a unconference session running in parallel in the afternoon at Lola's Room.

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**:   Main stage, Crystal Ballroom
* **When**: **9am-5pm**
* **Details**: Full main stage schedule below!

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-1.yaml
   :template: include/schedule2018.rst
   :include_env:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Second Stage
~~~~~~~~~~~~~

The :doc:`/conf/portland/2018/unconference` sessions run in parallel to the main conference talks in Lola's room, Crystal Ballroom.

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{year}}.{{shortcode}}.second-schedule-day-1.yaml
   :template: include/schedule2018.rst
   :include_env:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}


Monday Night Social
~~~~~~~~~~~~~~~~~~~

The official Write the Docs social!
Location and directions will be posted soon!

This event is for **conference attendees only**. Please bring your badge to be let into the venue.

There will be light snacks and drinks available on the conference while our tab lasts.

* **Where**: TBA
* **When**: **7pm-11pm**
* **Details**: TBA

Tuesday, May 8 - Conference
-----------------------------

.. contents::
    :local:
    :backlinks: none

And the conference goes on!

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: Main stage, Crystal Ballroom
* **When**: **9am-4pm**
* **Details**: Full main stage schedule below!

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-2.yaml
   :template: include/schedule2018.rst
   :include_env:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Second Stage
~~~~~~~~~~~~~~

**New in 2018! We'll be holding a job fair on Tuesday morning!**

The :doc:`/conf/portland/2018/job-fair` and  :doc:`/conf/portland/2018/unconference` sessions run in parallel to the main conference talks in Lola's room, Crystal Ballroom.

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{year}}.{{shortcode}}.second-schedule-day-2.yaml
   :template: include/schedule2018.rst
   :include_env:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}
