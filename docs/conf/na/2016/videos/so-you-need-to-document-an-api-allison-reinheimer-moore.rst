:template: 2017/video-details.html

so you need to document an API
==============================

{% set talk = conferences[2016]['na']['speakers'][16] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
