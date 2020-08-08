{# Set the `speakers` and `conf` variables before including this template #}

{% for talk in data %}

- {{ talk.title }} by  {% for speaker in talk.speakers %} {{ speaker.name }}{{ "," if not loop.last }} {% endfor %}

{% endfor %}
