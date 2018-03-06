:template: 2017/video-details.html

Keynote: The Federated Wiki
===========================

{% set talk = conferences[2015]['na']['speakers'][1] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
