:template: 2017/video-details.html

Only Interesting Conversations: The symbiotic relationship between docs and support
===================================================================================

{% set talk = conferences[2017]['na']['speakers'][7] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
