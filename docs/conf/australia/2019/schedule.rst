:template: {{year}}/generic.html


Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{% if flaglivestreaming %}

We're `live streaming </conf/{{shortcode}}/{{year}}/livestream>`_ the talks!

{% endif %}

Thursday, 14th November 2019
----------------------------

*Tea, coffee and lunch will be provided, as well as snacks and drinks all day.*

Conference talks and workshops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **8:45-17:30** (including a lunch break)

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-1.yaml
   :template: include/schedule2018.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel with the workshop.

* **Where**: {{about.unconfroom}}
* **When**: **13:00-17:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Thursday Night Social
~~~~~~~~~~~~~~~~~~~~~~~

The official Write the Docs Australia social!
This event is for **conference attendees only**, so please bring your badge to be let into the venue.
There will be drinks and nibbles available while our tab lasts.

* **Where**: Harts Pub, Essex St & Gloucester St, The Rocks, NSW
* **When**: **6.30pm-9.00pm**


Friday, 15th November 2019
----------------------------------------

*Tea, coffee and lunch will be provided, as well as snacks and drinks all day.*

Conference talks and workshops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **9:00-17:00** (including a lunch break)

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-2.yaml
   :template: include/schedule2019.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the mini-workshop.

* **Where**: {{about.unconfroom}}
* **When**: **13:00-17:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`
