:template: 2017/video-details.html

We’re not in Kansas anymore: How to find courage while following the Technical Doc Road
=======================================================================================

{% set talk = conferences[2016]['na']['speakers'][17] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
