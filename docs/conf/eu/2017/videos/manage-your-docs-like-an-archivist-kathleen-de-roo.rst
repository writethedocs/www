:template: 2017/video-details.html

Manage your docs like an archivist
==================================

{% set talk = conferences[2017]['eu']['speakers'][6] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
