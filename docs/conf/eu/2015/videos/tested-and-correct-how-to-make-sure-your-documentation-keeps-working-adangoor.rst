:template: 2017/video-details.html

Tested and Correct, How to Make Sure Your Documentation Keeps Working
=====================================================================

{% set talk = conferences[2015]['eu']['speakers'][0] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
