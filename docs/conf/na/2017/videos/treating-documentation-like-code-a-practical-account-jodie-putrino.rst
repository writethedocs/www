:template: 2017/video-details.html

Treating documentation like code: a practical account
=====================================================

{% set talk = conferences[2017]['na']['speakers'][11] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
