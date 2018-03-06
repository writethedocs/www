:template: 2017/video-details.html

Caring Systems: Documentation as care
=====================================

{% set talk = conferences[2017]['na']['speakers'][14] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
