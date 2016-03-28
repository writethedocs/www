:template: 2016/na.html

Write the Docs NA 2016 Speakers
===============================


Presentations
-------------

.. raw:: html

    <a name="speaker-panel"></a>
    <div class="row row-speaker">
      <div class="col-md-2 col-md-offset-1 col-sm-2 col-sm-offset-1">
      </div>
      <div class="col-md-8 col-sm-8">
        <h3>
          Leon Barnard<br>
          Zachary Corleissen<br>
          Ted Hudek<br>
          <em>Unconfirmed Speaker</em>
          <span class="speaker-details">
          </span>
        </h3>
        <h4>Panel: Transforming your Documentation Process</h4>
        <p>
        We had a number of interesting presentations about companies transforming their documentation process.
        Instead of choosing just one,
        we asked the speakers to join us on a panel,
        so that folks can compare and contrast the different approaches.
        </p>
      </div>
    </div>

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
