:template: 2017/video-details.html

You have already succeeded: Design critique guidelines make feedback easier 2.0
===============================================================================

{% set talk = conferences[2016]['eu']['speakers'][18] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
