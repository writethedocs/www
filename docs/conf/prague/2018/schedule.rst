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

{{date.day_one.dotw}}, {{date.month}} {{date.day_one.date}}
--------------------------------------------------

{% if flaghashike %}

Hike
~~~~

The only event scheduled on Saturday is the :doc:`annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us on the hike and take the chance to explore Portland in all of its glory.

* **Where**: Lower Macleay Park or Macleay Park Entrance.
* **When**: 13:45
* **Details**: :doc:`Annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`

{% endif %}

{% if flaghasboat %}

Boat Ride
~~~~~~~~~

The only event scheduled on Saturday is the :doc:`Prague Boat Ride </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us and experience Prague from the water.

{% endif %}


{{date.day_two.dotw}}, {{date.month}} {{date.day_two.date}}
----------------------------------------

The Writing Day and Welcome Reception will be held at the **{{about.venue}}**.

*Breakfast and lunch will be provided, as well as snacks and drinks throughtout the day.*

.. contents::
    :local:
    :backlinks: none

Writing Day
~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **9:00-17:00**
* **Details**: :doc:`Writing Day documentation sprints </conf/{{shortcode}}/{{year}}/writing-day>`

Reception
~~~~~~~~~

We encourage everyone to drop by on Sunday evening for the conference reception.
You'll have a chance to get acquainted with each other over some drinks and snacks.
We'll also help groups organize dinner plans, so you can continue your conversations over more substantial food as well.

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **17:00-20:00**

{{date.day_three.dotw}}, {{date.month}} {{date.day_three.date}}
--------------------------------------------

.. contents::
   :local:
   :backlinks: none

This is the main event! Hear from lots of interesting folks about all things documentation.
We will have talks all day on the main stage, and a unconference session running in parallel in the afternoon.

*Breakfast and lunch will be provided, as well as snacks and drinks throughtout the day.*

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00-18:00**
* **Details**: TBA
..
    .. datatemplate::
       :source: /_data/na-2018-day-1.yaml
       :template: include/schedule2018.rst

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **13:30-18:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Monday Night Social
~~~~~~~~~~~~~~~~~~~

The official Write the Docs social!
Location and directions will be posted soon!

This event is for **conference attendees only**. Please bring your badge to be let into the venue.

There will be light snacks and drinks available on the conference while our tab lasts.

* **Where**: TBA
* **When**: **20:00-23:00**
* **Details**: TBA

{{date.day_four.dotw}}, {{date.month}} {{date.day_four.date}}
--------------------------------------------------

.. contents::
   :local:
   :backlinks: none

And the conference goes on!

*Breakfast and lunch will be provided, as well as snacks and drinks throughtout the day.*

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00-17:00**
* **Details**: TBA

..
    .. datatemplate::
       :source: /_data/na-2018-day-1.yaml
       :template: include/schedule2018.rst

Job Fair
~~~~~~~~

New in 2018! We'll be holding a job fair on Tuesday morning!

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **9:00-12:00**
* **Details**: TBA

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **12:00-17:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`
