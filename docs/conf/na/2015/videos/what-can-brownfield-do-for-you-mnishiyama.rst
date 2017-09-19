:template: 2017/video-details.html

What Can Brownfield Do For You?
===============================

{% set talk = conferences[2015]['na']['speakers'][9] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
