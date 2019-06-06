{% for talk in data %}

.. raw:: html
      <ul>
      {% for speaker in talk.speakers %}
        {% if talk.slides is defined %}
          <li>
          {{ speaker.name }} - <a href="{{ talk.slides }}">{{ talk.title }}</a>
          </li>
        {% endif %}
      {% endfor %}
      </ul>

{% endfor %}

We'll add more as we get them. `Add yours <https://github.com/writethedocs/www/edit/master/docs/_data/{{year}}.{{shortcode}}.speakers.yaml>`_.
