:template: 2017/video-details.html

Even Naming This Talk Is Hard
=============================

{% set talk = conferences[2016]['eu']['speakers'][0] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
