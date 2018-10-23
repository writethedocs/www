{% for talk in data %}

{% for speaker in talk.speakers %}
.. _speaker-{{ shortcode }}-{{ year }}-{{ speaker.slug }}:
{% endfor %}

.. Comment to break up reference issues
.. * Ashleigh Rentz – `The Facts About FAQs <http://www.writethedocs.org/conf/portland/2019/speakers/#speaker-portland-2019-ashleigh-rentz>`_

{% for speaker in talk.speakers %}
* {{ speaker.name }} – `{{ talk.title }} <http://www.writethedocs.org/conf/{{ shortcode }}/{{ year }}/speakers/#speaker-{{ shortcode }}-{{ year }}-{{ speaker.slug }}>`__
{% endfor %}
{% endfor %}
