:template: 2017/video-details.html

IMPOSTER NO MORE: How Tech Writers Can Shed Self-Doubt, Embrace Uncertainty, and Surf the Upcoming Swerve in Technical Documentation
====================================================================================================================================

{% set talk = conferences[2015]['eu']['speakers'][15] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
