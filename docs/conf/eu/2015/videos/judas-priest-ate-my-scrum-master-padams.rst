:template: 2017/video-details.html

Judas Priest Ate My Scrum Master
================================

{% set talk = conferences[2015]['eu']['speakers'][12] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
