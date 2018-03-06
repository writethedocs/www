:template: 2017/video-details.html

You have already succeeded: Design critique guidelines make feedback easier.
============================================================================

{% set talk = conferences[2017]['na']['speakers'][6] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
