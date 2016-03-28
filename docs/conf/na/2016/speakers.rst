:template: 2016/na.html

Speakers
========

{% for speaker in speakers2016 %}

.. raw:: html

    <a name="speaker-{{ speaker.slug }}"></a>
    <div class="row row-speaker">
      <div class="col-md-2 col-md-offset-1 col-sm-2 col-sm-offset-1">
        <img class="speaker-image" src="/_static/img/speakers/{{ speaker.img_file }}" />
      </div>
      <div class="col-md-8 col-sm-8">
        <h3>
          {{ speaker.name|indent(10) }}
          <span class="speaker-details">
          {{ speaker.details|indent(10) }}
          </span>
        </h3>
        <h4>{{ speaker.title }}</h4>
        {{ speaker.abstract|indent(10) }}
      </div>
    </div>

{% endfor %}
