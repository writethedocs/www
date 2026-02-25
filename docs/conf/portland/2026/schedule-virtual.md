---
template: {{year}}/generic-iframe.html
---

# Virtual Schedule

Write the Docs is more than a conference. Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

{% if not flaghasschedule %}

**Full schedule will be released closer to the conference.** See the [schedule overview](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/#schedule-overview) for high level details.

{% else %}

All times are in [{{ tz }}](https://time.is/{{ tz }}).

```{contents}
:local:
:depth: 1
:backlinks: none
```

<hr>

## {{date.day_three.dotw}}, {{date.day_three.date}}

{{ date.day_three.summary }}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day1 %} {% include "include/schedule2021.rst" %} {% endwith %}

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

### Conference Talks

Talks are around 30 minutes, with moderated 10 minute Q&A.

- **Where**: Venueless virtual platform
{% if not flaghasschedule %}
- **When**: **{{ date.day_three.talk_time }} {{ tz }}**
{% endif %}
- **Details**: [Speakers and talks](/conf/{{shortcode}}/{{year}}/speakers/)

### Social space

You can socialize with other virtual attendees in the various hallway channels.

## {{date.day_four.dotw}}, {{date.day_four.date}}

{{ date.day_four.summary }}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day2 %} {% include "include/schedule2021.rst" %} {% endwith %}

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

### Conference Talks

Talks are around 30 minutes, with moderated 10 minute Q&A.

- **Where**: Venueless virtual platform
{% if not flaghasschedule %}
- **When**: **{{ date.day_four.talk_time }} {{ tz }}**
{% endif %}
- **Details**: [Speakers and talks](/conf/{{shortcode}}/{{year}}/speakers/)

### Social space

You can socialize with other virtual attendees in the various hallway channels.

{% endif %}
