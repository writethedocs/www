:template: 2017/video-details.html

API documentation: Exploring the information needs of software developers
=========================================================================

{% set talk = conferences[2016]['eu']['speakers'][5] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
