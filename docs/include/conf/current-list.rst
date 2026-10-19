{#- The upcoming conferences, from upcoming_conferences in _data/community.yaml.
    Pages include this file with Jinja's include tag, not the RST directive,
    so the list is rendered. -#}
{% for conf in community.upcoming_conferences %}
- :doc:`{{ conf.title }} </{{ conf.docname }}>`, {{ conf.dates }}, **{{ conf.location }}**
{%- endfor %}
