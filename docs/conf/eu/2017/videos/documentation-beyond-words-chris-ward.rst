:template: 2017/video-details.html

Documentation beyond words
==========================

{% set talk = conferences[2017]['eu']['speakers'][11] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
