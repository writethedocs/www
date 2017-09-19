:template: 2017/video-details.html

When bad screenshots happen to good writers
===========================================

{% set talk = conferences[2016]['eu']['speakers'][3] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
