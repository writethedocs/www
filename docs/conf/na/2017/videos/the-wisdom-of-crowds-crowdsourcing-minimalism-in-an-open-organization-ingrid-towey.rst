:template: 2017/video-details.html

The Wisdom of Crowds: Crowdsourcing Minimalism in an Open Organization
======================================================================

{% set talk = conferences[2017]['na']['speakers'][13] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
