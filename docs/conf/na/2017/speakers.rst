:template: 2017/na-content.html

Write the Docs NA 2016 Speakers
===============================

Presentations
-------------

{% for talk in na_2016_speakers %}

{% for speaker in talk.speakers %}
.. _speaker-{{ speaker.slug }}:
{% endfor %}

.. raw:: html

    {% for speaker in talk.speakers %}
    <a name="speaker-{{ speaker.slug }}"></a>
    {% endfor %}
    <div class="row row-speaker">
      <div class="col-md-2 col-md-offset-1 col-sm-2 col-sm-offset-1">
        {% for speaker in talk.speakers %}
        <img class="speaker-image" src="/_static/img/speakers/{{ speaker.img_file }}" />
        {% endfor %}
      </div>
      <div class="col-md-8 col-sm-8">
        <h3>
          {% for speaker in talk.speakers %}
          {{ speaker.name|indent(10) }}
          <span class="speaker-details">
          {% if speaker.twitter %}
          <a href="https://twitter.com/{{ speaker.twitter }}">@{{ speaker.twitter }}</a>
          {% endif %}
          </span>
          {% endfor %}
        </h3>
        <h4>{{ talk.title }}</h4>
        {{ talk.abstract|indent(10) }}
      </div>
    </div>

{% endfor %}
