:template: 2017/video-details.html

A Developers Approach to Documentation: From Passive to Dynamic
===============================================================

{% set talk = conferences[2015]['na']['speakers'][7] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
