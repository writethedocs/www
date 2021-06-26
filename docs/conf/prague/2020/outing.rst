:template: {{year}}/generic.html

{% if shortcode == 'prague'%}
:banner: _static/conf/images/headers/group.png

Write the Docs Boat Ride
========================

As this year's conference is virtual, we encourage you to go on a boat ride or walk in your own beautiful home town.

{% elif shortcode == 'portland'%}

:banner: _static/conf/images/headers/hike.png

Write the Docs Hike
===================

{% include "conf/portland/hike.rst" %}

{% else %}

We don't have an outing yet.

{% endif %}
