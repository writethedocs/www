:template: 2017/video-details.html

Writing a book in 2017 
=======================

{% set talk = conferences[2017]['eu']['speakers'][9] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
