:template: {{year}}/generic.html

{% if shortcode == 'prague'%}
:banner: _static/conf/images/headers/group.png

Write the Docs Boat Ride
========================

{% include "conf/prague/boat.rst" %}

{% elif shortcode == 'portland'%}

:banner: _static/conf/images/headers/hike.png

Write the Docs Hike
===================

{% include "conf/portland/hike.rst" %}

{% else %}

We don't have an outing yet.

{% endif %}
