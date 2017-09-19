:template: 2017/video-details.html

How to Write Documentation for People that Don't Read
=====================================================

{% set talk = conferences[2015]['na']['speakers'][2] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
