:template: 2017/video-details.html

The quest for scientific credit for software documentation
==========================================================

{% set talk = conferences[2015]['eu']['speakers'][1] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
