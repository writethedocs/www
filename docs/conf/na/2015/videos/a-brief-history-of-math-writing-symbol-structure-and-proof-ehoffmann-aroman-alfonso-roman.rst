:template: 2017/video-details.html

A brief history of math writing: symbol, structure, and proof
=============================================================

{% set talk = conferences[2015]['na']['speakers'][14] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
