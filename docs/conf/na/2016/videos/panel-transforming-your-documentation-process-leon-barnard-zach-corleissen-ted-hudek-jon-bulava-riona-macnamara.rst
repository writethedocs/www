:template: 2017/video-details.html

Panel: Transforming your Documentation Process
==============================================

{% set talk = conferences[2016]['na']['speakers'][0] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
