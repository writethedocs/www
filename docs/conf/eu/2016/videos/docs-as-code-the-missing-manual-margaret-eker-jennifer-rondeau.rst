:template: 2017/video-details.html

Docs as Code: The Missing Manual
================================

{% set talk = conferences[2016]['eu']['speakers'][18] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
