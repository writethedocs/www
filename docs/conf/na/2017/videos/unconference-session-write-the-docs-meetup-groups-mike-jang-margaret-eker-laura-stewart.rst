:template: 2017/video-details.html

Unconference Session: Write the Docs Meetup Groups
==================================================

{% set talk = conferences[2017]['na']['speakers'][4] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
