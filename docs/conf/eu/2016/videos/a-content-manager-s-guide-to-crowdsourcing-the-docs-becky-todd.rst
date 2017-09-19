:template: 2017/video-details.html

A content manager's guide to crowdsourcing the docs
===================================================

{% set talk = conferences[2016]['eu']['speakers'][17] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
