:template: 2017/video-details.html

Writing So Your Words Are Read
==============================

{% set talk = conferences[2016]['na']['speakers'][11] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
