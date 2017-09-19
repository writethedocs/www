:template: 2017/video-details.html

Do you know a runbook from a flip book? How sysadmins use documentation
=======================================================================

{% set talk = conferences[2017]['na']['speakers'][21] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
