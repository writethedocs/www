:template: {{year}}/generic.html
:banner: _static/conf/images/headers/speakers.jpg

Conference Speakers
===================

**All talk videos will be published on our YouTube channel no later than 1 week after the conference.**

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-sessions.yaml
   :template: {{year}}/speakers.rst

{% else %}
  Nothing to see yet. The speakers for the conference will be announced shortly after the call for papers ends.
{% endif %}
