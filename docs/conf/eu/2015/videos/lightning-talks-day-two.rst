:template: 2017/video-details.html

Lightning Talks - Day Two
=========================

{% set talk = conferences[2015]['eu']['speakers'][19] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
