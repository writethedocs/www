:template: 2017/video-details.html

Feedback handling, community wrangling, panhandling
===================================================

{% set talk = conferences[2016]['eu']['speakers'][1] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
