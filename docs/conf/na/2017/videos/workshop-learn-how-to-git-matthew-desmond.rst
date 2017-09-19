:template: 2017/video-details.html

Workshop: Learn how to Git
==========================

{% set talk = conferences[2017]['na']['speakers'][0] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
