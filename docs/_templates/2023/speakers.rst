{% for talk in data %}

{% for speaker in talk.speakers %}
.. _speaker-{{ speaker.slug }}:
{% endfor %}

.. Comment to break up reference issues

.. raw:: html

    <article class="talk">
      {% for speaker in talk.speakers %}
      <div class="speaker-info">
        <img src="{{ speaker.slug|speaker_photo }}" class="speaker-picture">
        <div class="speaker-contact-info">
            <h2 class="speaker-name">{{ speaker.name }}</h2>
            <!--
            <ul class="speaker-social-contant">
                <li>
                    <a href="#">
                        <img src="../../../../_static/conf/images/icons/twitter-brown.svg" class="twitter">
                    </a>
                </li>
                <li>
                    <a href="">
                        <img src="../../../../_static/conf/images/icons/github-brown.svg" class="github">
                    </a>
                </li>
                <li>
                    <a href="">
                        <img src="../../../../_static/conf/images/icons/worldwideweb-brown.svg" class="webpage">
                    </a>
                </li>
            </ul>
            -->
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
