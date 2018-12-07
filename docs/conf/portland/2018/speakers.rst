:template: {{year}}/generic.html
:banner: _static/2018/assets/headers/portland-speakers.png

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{year}}.{{shortcode}}.speakers.yaml
   :template: {{year}}/speakers.rst
   :include_context:

{% else %}
  Nothing to see yet.
{% endif %}
