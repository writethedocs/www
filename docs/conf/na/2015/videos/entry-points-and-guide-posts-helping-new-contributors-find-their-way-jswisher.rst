:template: 2017/video-details.html

Entry points and guide posts: Helping new contributors find their way
=====================================================================

{% set talk = conferences[2015]['na']['speakers'][5] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
