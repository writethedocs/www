:template: 2017/video-details.html

Writing as a non-native speaker
===============================

{% set talk = conferences[2016]['eu']['speakers'][6] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
