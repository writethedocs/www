:template: 2017/video-details.html

Tech writing in a continuous deployment world
=============================================

{% set talk = conferences[2015]['na']['speakers'][15] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
