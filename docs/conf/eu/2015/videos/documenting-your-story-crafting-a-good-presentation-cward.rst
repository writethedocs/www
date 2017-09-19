:template: 2017/video-details.html

Documenting your Story - Crafting a good presentation
=====================================================

{% set talk = conferences[2015]['eu']['speakers'][3] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
