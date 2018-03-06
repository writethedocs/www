:template: 2017/video-details.html

Workshop: Structuring and writing documentation
===============================================

{% set talk = conferences[2017]['na']['speakers'][1] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
