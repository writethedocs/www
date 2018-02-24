:template: {{year}}/{{templatecode}}/generic.html
:banner: _static/2018/assets/headers/speakers.jpg

Conference Speakers
===================

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{year}}.{{city}}.speakers.yaml
   :template: {{year}}/{{templatecode}}/speakers.rst

{% else %}
  Nothing to see yet.
{% endif %}
