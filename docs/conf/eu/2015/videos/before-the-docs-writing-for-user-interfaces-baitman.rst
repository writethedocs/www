:template: 2017/video-details.html

Before the docs: writing for user interfaces
============================================

{% set talk = conferences[2015]['eu']['speakers'][2] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
