:template: 2017/video-details.html

Deprecate and destroy: documenting your software’s last days
============================================================

{% set talk = conferences[2017]['eu']['speakers'][13] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
