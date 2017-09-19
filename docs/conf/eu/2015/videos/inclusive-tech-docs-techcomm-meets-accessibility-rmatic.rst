:template: 2017/video-details.html

Inclusive Tech Docs - TechComm Meets Accessibility
==================================================

{% set talk = conferences[2015]['eu']['speakers'][14] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
