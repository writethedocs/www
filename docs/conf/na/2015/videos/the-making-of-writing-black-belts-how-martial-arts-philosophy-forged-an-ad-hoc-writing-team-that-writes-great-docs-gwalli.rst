:template: 2017/video-details.html

The Making of Writing Black Belts: How Martial Arts Philosophy Forged an Ad-Hoc Writing Team that Writes Great Docs
===================================================================================================================

{% set talk = conferences[2015]['na']['speakers'][18] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
