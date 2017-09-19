:template: 2017/conference-videos-archive.html

Videos from Write the Docs EU
=============================================

{% set output %}
{% set talks = sessions_by_series['eu'] %}
{% set path_to_root = '../../..' %}
{% include conf_py_root + "/_templates/video-listing.html" %}
{% endset %}

.. raw:: html
   
   {{ output|indent(3) }}

