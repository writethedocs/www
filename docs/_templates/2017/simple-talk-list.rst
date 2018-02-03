{# Set the `speakers` and `conf` variables before including this template #}

{% for talk in data %}

  {% for speaker in talk.speakers %}

  - {{ speaker.name }} - {{ talk.title }}

  {% endfor %}

{% endfor %}
