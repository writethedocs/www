:template: 2017/video-details.html

Unconference Session: Release Notes: What's Working (and Not Working) for You?
==============================================================================

{% set talk = conferences[2017]['na']['speakers'][16] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
