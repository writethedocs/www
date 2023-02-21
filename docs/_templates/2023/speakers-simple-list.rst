{% for talk in data %}

.. Comment to break up reference issues

* {% for speaker in talk.speakers %} :ref:`{{ speaker.name }} <speaker-{{ speaker.slug }}>`{{ ", " if not loop.last }}{% endfor %}: {{ talk.title }}

{%- endfor -%}
