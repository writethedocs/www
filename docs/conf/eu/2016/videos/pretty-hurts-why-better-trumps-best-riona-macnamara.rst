:template: 2017/video-details.html

Pretty hurts: Why better trumps best
====================================

{% set talk = conferences[2016]['eu']['speakers'][12] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
