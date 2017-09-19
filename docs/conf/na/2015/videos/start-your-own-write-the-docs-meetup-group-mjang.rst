:template: 2017/video-details.html

Start Your Own Write the Docs Meetup Group
==========================================

{% set talk = conferences[2015]['na']['speakers'][16] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
