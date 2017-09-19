:template: 2017/video-details.html

Generating docs from APIs
=========================

{% set talk = conferences[2015]['eu']['speakers'][9] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
