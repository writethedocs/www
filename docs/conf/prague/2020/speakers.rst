:template: {{year}}/generic.html
:banner: _static/conf/images/headers/speakers.jpg

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-sessions.yaml
   :template: {{year}}/speakers.rst
   :include_context:

{% else %}
  Nothing to see yet.
{% endif %}
