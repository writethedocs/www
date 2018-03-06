:template: 2017/video-details.html

User-Story Driven Docs
======================

{% set talk = conferences[2015]['na']['speakers'][17] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
