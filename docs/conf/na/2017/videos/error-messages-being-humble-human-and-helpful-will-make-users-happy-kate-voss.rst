:template: 2017/video-details.html

Error Messages: Being Humble, Human, and Helpful will make users Happy
======================================================================

{% set talk = conferences[2017]['na']['speakers'][9] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
