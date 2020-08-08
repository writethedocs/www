:template: {{year}}/generic.html
:banner: _static/conf/images/headers/speakers.jpg

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{year}}.{{shortcode}}.speakers.yaml
   :template: {{year}}/speakers.rst

{% else %}
  Nothing to see yet.
{% endif %}
