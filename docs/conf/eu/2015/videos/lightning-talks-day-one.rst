:template: 2017/video-details.html

Lightning Talks - Day One
=========================

{% set talk = conferences[2015]['eu']['speakers'][18] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
