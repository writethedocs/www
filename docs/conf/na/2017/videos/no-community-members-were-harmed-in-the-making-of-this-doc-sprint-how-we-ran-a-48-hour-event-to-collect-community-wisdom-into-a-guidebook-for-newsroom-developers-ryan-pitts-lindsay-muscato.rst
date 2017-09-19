:template: 2017/video-details.html

No Community Members Were Harmed in the Making of This Doc Sprint: How we ran a 48-hour event to collect community wisdom into a guidebook for newsroom developers
==================================================================================================================================================================

{% set talk = conferences[2017]['na']['speakers'][12] %}
{% set output %}
{% include conf_py_root + '/_templates/video-details-body.html' %}
{% endset %}
.. raw:: html

    {{ output|indent(4) }}
