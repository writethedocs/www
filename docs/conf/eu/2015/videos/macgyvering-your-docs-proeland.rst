:template: 2017/video-details.html

MacGyvering your docs
=====================

{% set talk = conferences[2015]['eu']['speakers'][13] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
