:template: 2017/video-details.html

Documentoring: Growing a "Love The Docs" community
==================================================

{% set talk = conferences[2016]['eu']['speakers'][2] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
