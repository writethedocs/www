---
template: {{year}}/generic.html
banner: _static/conf/images/headers/2026/schedule.jpg
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

# Schedule

Write the Docs is more than a conference. Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

{% if not flaghasschedule %}

**Full schedule will be released closer to the conference.** See the [schedule overview](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/#schedule-overview) for high level details.

{% else %}

All times are in [{{ tz }}](https://time.is/{{ tz | replace(' ', '_') }}).

```{contents}
:local:
:depth: 1
:backlinks: none
```

{% if flaghashike or flaghasboat %}

## {{date.day_one.dotw}}, {{date.day_one.date}}

{% if flaghasschedule %}

```{raw} html
{% with day_schedule=schedule.outing %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% endif %}

{% endif %}

<hr>

## {{date.day_two.dotw}}, {{date.day_two.date}}

{% if flaghasschedule %}

```{raw} html
{% with day_schedule=schedule.writing_day %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

<hr>

## {{date.day_three.dotw}}, {{date.day_three.date}}

{% if flaghasschedule %}

```{raw} html
{% with day_schedule=schedule.talks_day1 %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

<hr>

## {{date.day_four.dotw}}, {{date.day_four.date}}

{% if flaghasschedule %}

```{raw} html
{% with day_schedule=schedule.talks_day2 %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

{% endif %}
