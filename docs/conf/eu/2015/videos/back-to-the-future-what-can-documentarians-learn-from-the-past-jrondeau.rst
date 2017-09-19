:template: 2017/video-details.html

Back to the Future: What Can Documentarians Learn From The Past?
================================================================

{% set talk = conferences[2015]['eu']['speakers'][10] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
