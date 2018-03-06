:template: 2017/video-details.html

Everyone's a player (in a mid-90s MUD)
======================================

{% set talk = conferences[2017]['na']['speakers'][2] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
