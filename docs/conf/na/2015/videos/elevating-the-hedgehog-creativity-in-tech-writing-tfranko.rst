:template: 2017/video-details.html

Elevating the Hedgehog: Creativity in Tech Writing
==================================================

{% set talk = conferences[2015]['na']['speakers'][4] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
