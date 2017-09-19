:template: 2017/video-details.html

All roads might not lead to docs
================================

{% set talk = conferences[2015]['eu']['speakers'][4] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
