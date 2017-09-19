:template: 2017/video-details.html

Writer, Meet Tester
===================

{% set talk = conferences[2015]['na']['speakers'][10] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
