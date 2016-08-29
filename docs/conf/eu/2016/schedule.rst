:template: 2016/eu.html

Schedule
========

Write the Docs is more than a conference. Each year we organize a wide
range of events so that people can come together, collaborate, and learn
from each other in different ways.

Saturday, September 17th
------------------------
If you're in town early, we'll organize some sight-seeing activities to introduce
you to this lovely city and to meet other documentarians who will be around.

Sunday, September 18th
----------------------

During the day, we’ll hold our :doc:`Writing Day documentation
sprints </conf/eu/2016/writingday>`, followed by the conference reception in the evening.
We encourage everyone to drop by on Sunday evening for the conference reception.

You’ll have a chance to get acquainted with each other over some drinks and snacks.
We’ll also help groups organize dinner plans, so you can continue your conversations
over more substantial food as well.

.. raw:: html

   <table class="schedule">
   <tr>
    <td class="schedule-time">10:00</td>
    <td><a href="/conf/eu/2016/writingday/">Writing Day</a> documentation sprints begin 
   </tr>
   <tr>
    <td class="schedule-time">10:30</td>
    <td>Introduction to the Writing Day</td>
   </tr>
   <tr>
    <td class="schedule-time">18:00</td>
    <td>Writing Day ends. Reception begins. Stop working and start chatting!</td>
   </tr>
   <tr>
    <td class="schedule-time">20:00</td>
    <td>Reception ends</td>
   </tr>
   </table>


Monday, September 19th - Day 1
------------------------------

This is the main event! Hear from lots of interesting folks about all
things documentation.

Parallel to the main presentations, we will also provide an unconference space
each afternoon as well as lightning talks. Sign up for these on the morning of
the event.

Main Stage
~~~~~~~~~~

.. raw:: html

    <table>
    {% for talk in eu_2016_day1 %}
      <tr>
        <td class=" schedule-time">{{ talk.Time }}</td>
        <td>

:ref:`{{ talk.Session }} <speaker-eu-2016-{{ talk.slug }}>`

.. raw:: html

        </td>
      </tr>

    {% endfor %}
    </table>

Unconference
~~~~~~~~~~~~

:doc:`/conf/eu/2016/unconference` from 13:00-17:00

Monday Night - Party
~~~~~~~~~~~~~~~~~~~~

Wind down and talk about the day's talks in a relaxed and friendly
environment. Free drinks of all varieties, snacks, and sweets will be
provided.

Tuesday, September 20th - Day 2
-------------------------------

More interesting folks, more things documentation. Unconference space and
lightning talks too!

Main Stage
~~~~~~~~~~

.. raw:: html

    <table>
    {% for talk in eu_2016_day2 %}
      <tr>
        <td class=" schedule-time">{{ talk.Time }}</td>
        <td>

:ref:`{{ talk.Session }} <speaker-eu-2016-{{ talk.slug }}>`

.. raw:: html

        </td>
      </tr>

    {% endfor %}
    </table>

Unconference
~~~~~~~~~~~~

:doc:`/conf/eu/2016/unconference` from 13:00-17:00

