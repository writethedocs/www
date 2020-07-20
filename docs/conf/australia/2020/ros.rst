:template: {{year}}/generic.html
:orphan:


Run of show
============

{% if not flaghasschedule %}
  A detailed schedule will be announced soon.
{% endif %}


{{date.day_two.dotw}}, {{date.day_two.date}}
-----------------------------------------

{% if flaghasschedule %}
{% with day_schedule=schedule.writing_day %}
{% include "include/ros2020.rst" %}
{% endwith %}
{% endif %}

Thursday, December 3
---------------------

{% if flaghasschedule %}
{% with day_schedule=schedule.day1 %}
{% include "include/ros2020.rst" %}
{% endwith %}
{% endif %}

Friday, December 4
-------------------

{% if flaghasschedule %}
{% with day_schedule=schedule.day2 %}
{% include "include/ros2020.rst" %}
{% endwith %}
{% endif %}
