:template: 2017/video-details.html

Documentarians and Support: Work Better Together
================================================

{% set talk = conferences[2016]['eu']['speakers'][11] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
