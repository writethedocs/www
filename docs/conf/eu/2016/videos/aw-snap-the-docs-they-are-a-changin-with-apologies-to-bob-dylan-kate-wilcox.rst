:template: 2017/video-details.html

Aw Snap!  The Docs, They Are A-Changin’ (with apologies to Bob Dylan)
=====================================================================

{% set talk = conferences[2016]['eu']['speakers'][8] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
