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

All times are in [{{ tz }}](https://time.is/{{ tz }}).

```{contents}
:local:
:depth: 1
:backlinks: none
```

### Welcome Wagon Introduction

Is this your first time at Write the Docs? Join us for an informal Introduction to Write the Docs, to the Welcome Wagon, and to other first-time conference attendees. We'll pass on some information about the conference specifically for first-timers and give everyone a chance to meet someone new.

- **Where**: {{about.unconfroom}}
- **Details**: [Attendee guide](/conf/{{shortcode}}/{{year}}/attendee-guide/)

<hr>

## {{date.day_one.dotw}}, {{date.day_one.date}}

<p>
{{ date.day_one.summary }}
</p>

- Conference talks are held in {{about.venue}}
- Unconference is held in {{about.venue}}, {{about.unconfroom}}

{% if flaghasfood %}

*Morning tea, boxed lunch, and afternoon tea will be provided.*

{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day1 %} {% include "include/schedule2021.rst" %} {% endwith %}

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

<hr>

## Social Event

The official Write the Docs social! Expect a relaxed atmosphere where you can chat and network with your fellow documentarians.

Snacks and drinks (non-alcoholic & alcoholic) will be provided.

* **Where**: {{ about.social_venue }}
{% if not flaghasschedule %}
* **When**: **{{ date.day_one.social_time }} {{ tz }}**
{% endif %}

<hr>

## {{date.day_two.dotw}}, {{date.day_two.date}}

<p>
{{ date.day_two.summary }}
</p>

- Conference talks are held in {{about.venue}}
- Unconference is held in {{about.venue}}, {{about.unconfroom}}

{% if flaghasfood %}

*Morning tea, boxed lunch, and afternoon tea will be provided.*

{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day2 %} {% include "include/schedule2021.rst" %} {% endwith %}

{% else %}  
A detailed schedule will be announced soon.

{% endif %}

{% endif %}
