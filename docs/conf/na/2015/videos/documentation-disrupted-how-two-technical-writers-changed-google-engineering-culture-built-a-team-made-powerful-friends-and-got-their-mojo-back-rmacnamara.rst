:template: 2017/video-details.html

Documentation, Disrupted How Two Technical Writers Changed Google Engineering Culture, Built a Team, Made Powerful Friends, And Got Their Mojo Back
===================================================================================================================================================

{% set talk = conferences[2015]['na']['speakers'][3] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
