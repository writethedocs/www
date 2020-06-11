:template: {{year}}/generic.html
:orphan:


Run of show
============


Monday, May 20
--------------

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-1.yaml
   :template: include/ros{{year}}.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Tuesday, May 21
---------------

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-2.yaml
   :template: include/ros{{year}}.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}
