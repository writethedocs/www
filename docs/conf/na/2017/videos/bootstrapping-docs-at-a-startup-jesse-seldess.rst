:template: 2017/video-details.html

Bootstrapping Docs at a Startup
===============================

{% set talk = conferences[2017]['na']['speakers'][15] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
