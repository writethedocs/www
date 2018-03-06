:template: 2017/video-details.html

Crossing the Streams: Enabling Collaboration Between Products and Upstreams 
============================================================================

{% set talk = conferences[2016]['na']['speakers'][13] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
