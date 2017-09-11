:template: 2017/conference-videos-archive.html

Write the Docs 2017 EU Videos
=============================

{% set output %}
{% set path_to_root = "../../../.." %}
{% set talks = conferences[2017]['eu']['speakers'] %}
{% include conf_py_root + "/_templates/video-listing.html" %}
{% endset %}

.. raw:: html
   
   {{ output|indent(3) }}

.. toctree::
    :hidden:
    :glob:

    videos/*
