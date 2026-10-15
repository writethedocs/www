{#
  Renders one section per talk day listed in the config's date.days,
  with that day's schedule from the schedule YAML.
  Used by the 2027+ conference virtual schedule pages.
#}
{% for day in date.talk_days %}
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

### Conference Talks

Talks are around 30 minutes, followed by moderated Q&A.

- **Where**: Venueless virtual platform
{% if not flaghasschedule %}
- **When**: **{{ day.hours }} {{ tz }}**
{% endif %}
- **Details**: [Speakers and talks](/conf/{{shortcode}}/{{year}}/speakers/)

### Social space

You can socialize with other virtual attendees in the various hallway channels.
{% endfor %}
