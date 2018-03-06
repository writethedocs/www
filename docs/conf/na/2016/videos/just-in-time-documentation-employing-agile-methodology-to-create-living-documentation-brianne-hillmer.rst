:template: 2017/video-details.html

Just-In-Time Documentation: Employing Agile Methodology To Create Living Documentation
======================================================================================

{% set talk = conferences[2016]['na']['speakers'][6] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
