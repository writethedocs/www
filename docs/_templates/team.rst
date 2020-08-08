{% for lovely_human in data %}

.. _team-{{ lovely_human.slug }}:

.. 
    .. image:: /_static/img/crew/{{ lovely_human.slug }}.jpg
       :width: 30%

{{ lovely_human.name }}
{{ "=" * lovely_human.name|length }}

.. include:: /include/bios/{{ lovely_human.slug }}.rst

{% endfor %}