:template: 2017/video-details.html

Managing community-driven documentation - how to herd doc-writing cats through motivation and a pinch of automation
===================================================================================================================

{% set talk = conferences[2016]['eu']['speakers'][7] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
