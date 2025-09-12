:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

{% if not flaghasschedule %}

**Full schedule will be released closer to the conference.** See the `schedule overview </conf/{{shortcode}}/{{year}}/#schedule-overview>`_ for high level details.

{% else %}

All times are in `{{ tz }} <https://time.is/{{ tz }}>`_.


.. contents::
    :local:
    :depth: 1
    :backlinks: none


{% if flaghashike or flaghasboat %}

{{date.day_one.dotw}}, {{date.day_one.date}}
--------------------------------------------------

.. raw:: html

   {{ date.day_one.summary }}

{% if flaghasschedule %}

{% with day_schedule=schedule.outing %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% endif %}

{% endif %}

.. raw:: html

   <hr>

{% if flaghaswritingday %}

{{date.day_two.dotw}}, {{date.day_two.date}}
-----------------------------------------

.. raw:: html

   {{ date.day_two.summary }}

{% if flaghasschedule %}

{% with day_schedule=schedule.writing_day %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

{% endif %}

{% if flaghaswritingday %}{{date.day_three.dotw}}, {{date.day_three.date}}{% else %}{{date.day_one.dotw}}, {{date.day_one.date}}{% endif %}
-----------------------------------------

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day1 %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
    A detailed schedule will be announced soon.
{% endif %}

.. raw:: html

   <hr>

{% if flaghaswritingday %}{{date.day_four.dotw}}, {{date.day_four.date}}{% else %}{{date.day_two.dotw}}, {{date.day_two.date}}{% endif %}
-----------------------------------------

{% if flaghasfood %}
*Snacks and drinks will be provided throughout the day.*
{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day2 %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

{% endif %}
