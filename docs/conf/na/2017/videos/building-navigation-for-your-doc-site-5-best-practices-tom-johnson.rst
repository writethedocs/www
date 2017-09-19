:template: 2017/video-details.html

Building navigation for your doc site: 5 best practices
=======================================================

{% set talk = conferences[2017]['na']['speakers'][5] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
