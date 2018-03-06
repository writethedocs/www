:template: 2017/video-details.html

Two great teams that work better together: Bridging the gap between Documentation and Customer Support
======================================================================================================

{% set talk = conferences[2016]['na']['speakers'][3] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
