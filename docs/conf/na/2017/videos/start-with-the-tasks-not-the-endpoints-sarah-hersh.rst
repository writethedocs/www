:template: 2017/video-details.html

Start with the tasks, not the endpoints
=======================================

{% set talk = conferences[2017]['na']['speakers'][19] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
