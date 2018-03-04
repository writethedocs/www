:template: {{year}}/{{templatecode}}/generic.html

{% if shortcode == 'prague'%}
:banner: _static/2018/assets/headers/group.png

Write the Docs Boat Ride
========================

.. include:: /include/conf/prague/boat.rst

{% elif shortcode == 'portland'%}

:banner: _static/2018/assets/headers/hike.png

Write the Docs Hike
===================

.. include:: /include/conf/portland/hike.rst

{% else %}

We don't have an outing yet.

{% endif %}
