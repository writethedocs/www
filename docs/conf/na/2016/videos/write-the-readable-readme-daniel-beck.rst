:template: 2017/video-details.html

Write the Readable README
=========================

{% set talk = conferences[2016]['na']['speakers'][9] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
