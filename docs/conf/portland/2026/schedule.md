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

```{raw} html
<style>
.schedule-item--main { border-left: 4px solid #fdb913; }
.schedule-item--unconf { border-left: 4px solid #7e4d00; }
.schedule-item--writing { border-left: 4px solid #3a7ca5; }
.schedule-item--social { border-left: 4px solid #c45b9a; }
.schedule-item--outdoor { border-left: 4px solid #4a8c5c; }
.schedule-item--main,
.schedule-item--unconf,
.schedule-item--writing,
.schedule-item--social,
.schedule-item--outdoor { padding-left: 12px; }
.schedule-legend {
  display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;
  font-size: 14px; color: #4a4a4a;
}
.schedule-legend-item {
  display: flex; align-items: center; gap: 6px;
}
.schedule-legend-swatch {
  display: inline-block; width: 14px; height: 14px;
  border-radius: 2px; flex-shrink: 0;
}
.swatch-main { background: #fdb913; }
.swatch-unconf { background: #7e4d00; }
.swatch-writing { background: #3a7ca5; }
.swatch-social { background: #c45b9a; }
.swatch-outdoor { background: #4a8c5c; }
</style>
```

```{contents}
:local:
:depth: 1
:backlinks: none
```

{% if flaghashike or flaghasboat %}

## {{date.day_one.dotw}}, {{date.day_one.date}}

{% if flaghasschedule %}

```{raw} html
<div class="schedule-legend">
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-outdoor"></span> Outdoor</span>
</div>
{% with day_schedule=schedule.outing, day_type="outing" %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% endif %}

{% endif %}

<hr>

## {{date.day_two.dotw}}, {{date.day_two.date}}

{% if flaghasschedule %}

```{raw} html
<div class="schedule-legend">
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-writing"></span> {{about.unconfroom}}</span>
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-unconf"></span> Welcome Wagon tours</span>
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-social"></span> Social</span>
</div>
{% with day_schedule=schedule.writing_day, day_type="writing" %}
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
<div class="schedule-legend">
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-main"></span> {{about.mainroom}}</span>
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-unconf"></span> {{about.unconfroom}}</span>
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-social"></span> Social</span>
</div>
{% with day_schedule=schedule.talks_day1, day_type="talks" %}
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
<div class="schedule-legend">
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-main"></span> {{about.mainroom}}</span>
  <span class="schedule-legend-item"><span class="schedule-legend-swatch swatch-unconf"></span> {{about.unconfroom}}</span>
</div>
{% with day_schedule=schedule.talks_day2, day_type="talks" %}
{% include "include/schedule2026.md" %}
{% endwith %}
```

{% else %}
A detailed schedule will be announced soon.

{% endif %}

{% endif %}
