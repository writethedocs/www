:template: 2017/video-details.html

Success is More Than Not Failing
================================

{% set talk = conferences[2015]['na']['speakers'][6] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
