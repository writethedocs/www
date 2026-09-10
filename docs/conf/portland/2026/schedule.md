---
template: {{year}}/generic.html
banner: _static/conf/images/headers/2026/schedule.jpg
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

# Schedule

{% if flaghasschedule %}

```{raw} html
<nav class="uk-flex uk-flex-wrap uk-flex-center" aria-label="Schedule dates">
{% if flaghashike or flaghasboat %}
  <a class="uk-button uk-button-secondary uk-margin-small-right uk-margin-small-bottom" href="#day-one">{{date.day_one.dotw}}, {{date.day_one.date}}</a>
{% endif %}
  <a class="uk-button uk-button-secondary uk-margin-small-right uk-margin-small-bottom" href="#day-two">{{date.day_two.dotw}}, {{date.day_two.date}}</a>
  <a class="uk-button uk-button-secondary uk-margin-small-right uk-margin-small-bottom" href="#day-three">{{date.day_three.dotw}}, {{date.day_three.date}}</a>
  <a class="uk-button uk-button-secondary uk-margin-small-bottom" href="#day-four">{{date.day_four.dotw}}, {{date.day_four.date}}</a>
</nav>
```

{% endif %}

Write the Docs is more than a conference. Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

{% if not flaghasschedule %}

**Full schedule will be released closer to the conference.** See the [schedule overview](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/#schedule-overview) for high level details.

{% else %}

All times are in [{{ tz }}](https://time.is/{{ tz | replace(' ', '_') }}).

{% if flaghashike or flaghasboat %}

<span id="day-one"></span>

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

<span id="day-two"></span>

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

<span id="day-three"></span>

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

<span id="day-four"></span>

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
