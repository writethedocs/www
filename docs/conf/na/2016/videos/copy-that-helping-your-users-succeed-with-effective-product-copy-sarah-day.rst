:template: 2017/video-details.html

Copy that: Helping your users succeed with effective product copy
=================================================================

{% set talk = conferences[2016]['na']['speakers'][12] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
