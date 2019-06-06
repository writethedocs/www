:template: {{year}}/index.html
:banner: _static/{{year}}/assets/headers/group.png
:orphan:

.. raw:: html

  <div class="news-block">
    <div class="uk-container">

      <h2 id="slides">Speaker slides</h2>
      <section>
      <div class="content">

{% if flagspeakersannounced %}

.. datatemplate::
   :source: /_data/{{year}}.{{shortcode}}.speakers.yaml
   :template: {{year}}/slides.rst
   :include_context:
{% endif %}

.. raw:: html

      </div>
      </section>
    </div>
    </div>

.. raw:: html

  <div class="news-block">
    <div class="uk-container">

      <h2>Updates from the team</h2>
      <section>
      <div class="content">

.. postlist:: 10
   :date: %B %d, %Y
   :format: {title} - {date}
   :list-style: none
   :tags: {{ shortcode }}-{{ year }}

.. raw:: html

      </div>
      </section>
    </div>
  </div><!--- end news block -->
