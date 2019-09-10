{% for talk in data %}

{% for speaker in talk.speakers %}
.. _speaker-{{ shortcode }}-{{ year }}-{{ speaker.slug }}:
{% endfor %}

.. Comment to break up reference issues
.. * comment

* {% for speaker in talk.speakers %}{{ speaker.name }}{{ ", " if not loop.last }} {% endfor %} – {{ talk.title }} {% endfor %}
