:template: {{year}}/generic.html
:banner: _static/conf/images/headers/speakers.jpg
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-sessions.yaml
   :template: {{year}}/speakers.rst

{% else %}
  Nothing to see yet. The speakers for the conference will be announced shortly after the call for papers ends.
{% endif %}
