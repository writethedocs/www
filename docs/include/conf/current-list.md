{#- The upcoming conferences, from upcoming_conferences in _data/community.yaml.
    Pages include this file with Jinja's include tag, not the include directive,
    so the list is rendered. -#}
{% for conf in community.upcoming_conferences %}
- [{{ conf.title }}]({{ conf.url }}), {{ conf.dates }}, **{{ conf.location }}**
{%- endfor %}
