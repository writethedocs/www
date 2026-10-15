{#
  Renders one section per conference day listed in the config's date.days,
  with that day's schedule from the schedule YAML.
  Used by the 2027+ conference schedule pages.
#}
{% for day in date.days %}
{% if not loop.first %}
<hr>
{% endif %}

## {{ day.dotw }}, {{ day.date }}

{{ day.summary }}

{% if flaghasschedule %}

```{raw} html
{% with day_schedule=schedule[day.schedule] %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% else %}
A detailed schedule will be announced soon.

{% endif %}
{% endfor %}
