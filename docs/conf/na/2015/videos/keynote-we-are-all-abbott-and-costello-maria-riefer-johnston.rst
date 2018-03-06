:template: 2017/video-details.html

Keynote: We Are All Abbott and Costello
=======================================

{% set talk = conferences[2015]['na']['speakers'][0] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
