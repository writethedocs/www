:template: 2017/video-details.html

One-on-One 101
==============

{% set talk = conferences[2017]['eu']['speakers'][15] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
