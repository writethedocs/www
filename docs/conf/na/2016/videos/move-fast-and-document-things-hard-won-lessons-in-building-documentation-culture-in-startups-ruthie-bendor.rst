:template: 2017/video-details.html

Move Fast And Document Things: Hard-won lessons in building documentation culture in startups.
==============================================================================================

{% set talk = conferences[2016]['na']['speakers'][5] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
