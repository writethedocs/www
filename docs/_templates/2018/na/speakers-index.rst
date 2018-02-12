.. raw:: html

  <div class="speakers">
    <div class="uk-container">
      <h2>Speakers</h2>
      <div class="speakers-carousel">

      {% for talk in data %}

        {% for speaker in talk.speakers %}
        <div class="speaker">
          <img class="uk-border-circle" src="/_static/img/speakers/{{ speaker.img_file }}">

          <h3>{{ speaker.name }}</h3>
          <a href="speakers#speaker-portland-2018-{{ speaker.slug }}">
            <p>{{ talk.title }}</p>
          </a>
          <!--
          <div class="contact-icon-list">
            <a href=""><img src="/_static/2018/assets/icons/twitter.svg"></a>

          </div>
          -->
        </div>
        {% endfor %}

      {% endfor %}

      </div>
    </div>
  </div>
