{% for talk in data %}

{# Make speakers linkable from announcements and other places #}
{% for speaker in talk.speakers %}
.. _speaker-{{ speaker.slug }}-{{ talk.slug }}:
{% endfor %}

.. Comment to break up reference issues

.. raw:: html

    <article class="talk">
      {% for speaker in talk.speakers %}

      <div class="speaker-info">
        <img src="{{ speaker.slug|speaker_photo }}" class="speaker-picture" style="height: 6em; width: auto">
        <div class="speaker-contact-info" style="display: flex; align-items: center; justify-content: flex-end;">
            <h2 class="speaker-name" style="font-size: 24px; text-align: right;">{{ speaker.name }}</h2>
        </div>
      </div>

     {% endfor %}
      <div class="talk-content">
        <h3 class="talk-title">{{ talk.title }}</h3>
        <div class="talk-description">
          {{ talk.abstract|indent(10) }}
        </div>
      </div>
    </article>

{% endfor %}
