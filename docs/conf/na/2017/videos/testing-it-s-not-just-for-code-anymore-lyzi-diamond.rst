:template: 2017/video-details.html

Testing: it's not just for code anymore
=======================================

{% set talk = conferences[2017]['na']['speakers'][3] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
