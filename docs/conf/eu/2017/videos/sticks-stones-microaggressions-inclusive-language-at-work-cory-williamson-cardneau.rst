:template: 2017/video-details.html

Sticks & Stones... Microaggressions & Inclusive Language at Work
================================================================

{% set talk = conferences[2017]['eu']['speakers'][5] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
