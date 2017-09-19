:template: 2017/video-details.html

Accessible Math on the Web: A Server/Client Solution
====================================================

{% set talk = conferences[2016]['na']['speakers'][21] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
