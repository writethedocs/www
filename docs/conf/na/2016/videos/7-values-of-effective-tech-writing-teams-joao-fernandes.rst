:template: 2017/video-details.html

7 values of effective tech writing teams
========================================

{% set talk = conferences[2016]['na']['speakers'][7] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
