:template: 2017/video-details.html

Beyond Software - Learning from Other Technical Writers
=======================================================

{% set talk = conferences[2016]['eu']['speakers'][4] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
