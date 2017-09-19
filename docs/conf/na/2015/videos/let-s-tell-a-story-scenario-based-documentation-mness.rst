:template: 2017/video-details.html

Let’s Tell a Story: Scenario-Based Documentation
================================================

{% set talk = conferences[2015]['na']['speakers'][12] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
