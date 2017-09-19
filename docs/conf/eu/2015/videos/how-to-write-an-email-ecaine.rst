:template: 2017/video-details.html

How to Write an Email
=====================

{% set talk = conferences[2015]['eu']['speakers'][6] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
