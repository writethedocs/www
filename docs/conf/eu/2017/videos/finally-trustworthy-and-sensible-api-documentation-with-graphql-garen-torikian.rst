:template: 2017/video-details.html

Finally! Trustworthy and Sensible API Documentation with GraphQL 
=================================================================

{% set talk = conferences[2017]['eu']['speakers'][2] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
