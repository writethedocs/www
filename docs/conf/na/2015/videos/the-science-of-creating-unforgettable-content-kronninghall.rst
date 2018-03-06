:template: 2017/video-details.html

The Science of Creating Unforgettable Content
=============================================

{% set talk = conferences[2015]['na']['speakers'][19] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
