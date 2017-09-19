:template: 2017/video-details.html

Using meaningful names to improve API-documentation
===================================================

{% set talk = conferences[2016]['eu']['speakers'][10] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
