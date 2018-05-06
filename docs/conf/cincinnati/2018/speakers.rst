:template: {{year}}/generic.html

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{year}}.{{city}}.speakers.yaml
   :template: {{year}}/speakers.rst
   :include_context:

{% else %}
  Nothing to see yet.
{% endif %}
