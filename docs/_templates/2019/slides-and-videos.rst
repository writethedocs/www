{% for talk in data %}

.. raw:: html
      <ul>
      {% for speaker in talk.speakers %}
        <li>
        {{ speaker.name }} - {{ talk.title }}
        {% if talk.youtubeId is defined %}
          [<a href="https://www.youtube.com/watch?v={{ talk.youtubeId }}">video</a>]&nbsp;
        {% endif %}
        {% if talk.slides is defined %}
          [<a href="{{ talk.slides }}">slides</a>]
        {% endif %}
        </li>
     {% endfor %}
     </ul>

{% endfor %}
