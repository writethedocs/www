:template: 2017/video-details.html

The four kinds of documentation, and why you need to understand what they are
=============================================================================

{% set talk = conferences[2017]['eu']['speakers'][4] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
