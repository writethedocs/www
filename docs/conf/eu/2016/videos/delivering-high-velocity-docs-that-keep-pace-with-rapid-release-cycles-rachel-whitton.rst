:template: 2017/video-details.html

Delivering High-Velocity Docs that Keep Pace with Rapid Release Cycles
======================================================================

{% set talk = conferences[2016]['eu']['speakers'][17] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
