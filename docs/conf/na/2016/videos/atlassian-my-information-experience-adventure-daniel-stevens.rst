:template: 2017/video-details.html

Atlassian: My Information Experience Adventure
==============================================

{% set talk = conferences[2016]['na']['speakers'][2] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
