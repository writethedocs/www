:template: 2017/video-details.html

CSAT- what's that?
==================

{% set talk = conferences[2016]['na']['speakers'][15] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
