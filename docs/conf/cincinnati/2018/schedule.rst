:template: {{year}}/generic.html

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{{date.day_one.dotw}}, {{date.day_one.date}}
--------------------------------------------------

{{ date.day_one.event }}
~~~~~~~~~~~~~~~~~~~~~~~~

{{ date.day_one.summary }}

{% if date.day_two is defined %}

{{date.day_two.dotw}}, {{date.day_two.date}}
----------------------------------------

{{ date.day_two.event }}
~~~~~~~~~~~~~~~~~~~~~~~~

{{ date.day_two.summary }}

{% endif %}

{% if date.day_three is defined %}

{{date.day_three.dotw}}, {{date.day_three.date}}
--------------------------------------------

{{ date.day_three.event }}
~~~~~~~~~~~~~~~~~~~~~~~~

{{ date.day_three.summary }}

{% endif %}


{% if date.day_four is defined %}

{{date.day_four.dotw}}, {{date.day_four.date}}
--------------------------------------------------

{{ date.day_four.summary }}

{% endif %}
