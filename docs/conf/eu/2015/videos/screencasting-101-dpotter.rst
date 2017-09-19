:template: 2017/video-details.html

Screencasting 101
=================

{% set talk = conferences[2015]['eu']['speakers'][5] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
