:template: 2017/video-details.html

An Alien Looking From the Outside In: Main Takeaways After One Year in Documentation
====================================================================================

{% set talk = conferences[2016]['eu']['speakers'][12] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
