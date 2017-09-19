:template: 2017/video-details.html

Interviewing and hiring technical writers: the Siberian way
===========================================================

{% set talk = conferences[2017]['na']['speakers'][10] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
