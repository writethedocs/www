:template: 2017/video-details.html

Watch that tone! Creating an information experience in the Atlassian voice
==========================================================================

{% set talk = conferences[2016]['eu']['speakers'][16] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
