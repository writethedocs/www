:template: {{year}}/generic.html

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{year}}.{{shortcode}}.speakers.yaml
   :template: {{year}}/speakers.rst

{% else %}
  Nothing to see yet.
{% endif %}
