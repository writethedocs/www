:template: 2017/video-details.html

How to Publish Wild-Caught Articles
===================================

{% set talk = conferences[2016]['na']['speakers'][8] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
