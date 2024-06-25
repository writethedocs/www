:template: {{year}}/index.html
:banner: _static/conf/images/headers/{{shortcode}}-{{year}}-group.jpg
:og:image: _static/conf/images/headers/portland-2025-opengraph.png

:orphan:

.. title:: Home | Write the docs {{ name }} {{ year }}


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

