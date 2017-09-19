:template: 2017/video-details.html

What Writing Fiction Teaches You About Writing Documentation
============================================================

{% set talk = conferences[2016]['na']['speakers'][14] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
