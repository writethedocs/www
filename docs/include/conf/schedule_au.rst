{% if not flaghasschedule %}
**WARNING**: This schedule has not been finalized and is subject to change. The schedule will be finalized around 1 month prior to the event.
{% endif %}

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

All times are in `{{ tz }} <https://time.is/{{ tz }}>`_.

.. contents::
    :local:
    :depth: 1
    :backlinks: none


Thursday, December 8
--------------------

.. contents::
   :local:
   :backlinks: none

This is the main event! Hear from lots of interesting folks about all things documentation.
We will have talks all day, and an unconference session running in parallel.

{% if flaghasfood %}

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

{% endif %}

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00am-4:30pm AEDT**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

.. separator to fix list formatting

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day1 %}
{% include "include/schedule2022.rst" %}
{% endwith %}

{% else %}
    A detailed schedule will be announced soon.
{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in the second half of the day.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **1:00pm-4:30pm AEDT**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Thursday Night Social
~~~~~~~~~~~~~~~~~~~~~

The official Write the Docs social!
Further details will be announced later,
but expect some music and games,
and bring your favourite beverage along to the computer :)

Friday, December 9
------------------

.. contents::
   :local:
   :backlinks: none

And the conference goes on!

{% if flaghasfood %}

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

{% endif %}

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **1:00pm-4:30pm AEDT**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

.. separator to fix list formatting

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day2 %}
{% include "include/schedule2022.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

.. _{{shortcode}}-{{year}}-job-fair:

Unconference
~~~~~~~~~~~~

The unconference sessions run in the second half of the day.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **2:00pm-4:00pm AEDT**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`
