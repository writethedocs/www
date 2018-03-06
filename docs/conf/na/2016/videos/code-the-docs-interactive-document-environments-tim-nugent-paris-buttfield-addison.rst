:template: 2017/video-details.html

Code the Docs: Interactive Document Environments
================================================

{% set talk = conferences[2016]['na']['speakers'][10] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
