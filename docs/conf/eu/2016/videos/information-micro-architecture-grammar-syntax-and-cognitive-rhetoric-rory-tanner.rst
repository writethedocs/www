:template: 2017/video-details.html

Information micro-architecture: grammar, syntax, and cognitive rhetoric
=======================================================================

{% set talk = conferences[2016]['eu']['speakers'][14] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
