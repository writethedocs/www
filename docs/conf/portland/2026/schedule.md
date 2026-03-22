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
.schedule-tab-nav {
  display: flex;
  gap: 4px;
  margin-bottom: 0;
  flex-wrap: wrap;
}
.schedule-tab-btn {
  padding: 10px 18px;
  border: 1px solid #cebea9;
  border-bottom: none;
  border-radius: 6px 6px 0 0;
  background: #f5f0ea;
  color: #4a4a4a;
  font-family: "Nunito Sans", sans-serif;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s;
}
.schedule-tab-btn:hover {
  background: #ebe3d8;
}
.schedule-tab-btn.active {
  background: #e8ddcf;
  border-color: #cebea9;
  color: #000;
}
.schedule-tab-panel {
  display: none;
}
.schedule-tab-panel.active {
  display: block;
}
.schedule-tab-panel .schedule {
  border-radius: 0 4px 4px 4px;
  margin-top: 0 !important;
}
.schedule-rooms-legend {
  display: flex;
  gap: 12px;
  padding: 12px 24px;
  background: #e8ddcf;
  border: 1px solid #cebea9;
  border-bottom: none;
  border-radius: 0;
  flex-wrap: wrap;
  align-items: center;
  font-size: 14px;
}
.schedule-rooms-legend::before {
  content: "Rooms:";
  font-weight: 700;
  color: #4a4a4a;
}
.room-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 3px;
  font-size: 13px;
  font-weight: 600;
}
.room-main {
  background: #fdb913;
  color: #000;
}
.room-unconf {
  background: #7e4d00;
  color: #fff;
}
.room-outdoor {
  background: #4a8c5c;
  color: #fff;
}
.schedule-item .item-room {
  margin-top: 2px;
}
.schedule-item .item-room .room-badge {
  font-size: 11px;
  padding: 1px 6px;
}
@media (max-width: 639px) {
  .schedule-tab-btn {
    font-size: 12px;
    padding: 8px 10px;
  }
}
</style>

<div class="schedule-tabs">
  <div class="schedule-tab-nav">
    {% if flaghashike or flaghasboat %}
    <button class="schedule-tab-btn active" onclick="switchScheduleTab(this, 'sat')">{{date.day_one.dotw}}, {{date.day_one.date}}</button>
    {% endif %}
    <button class="schedule-tab-btn{% if not flaghashike and not flaghasboat %} active{% endif %}" onclick="switchScheduleTab(this, 'sun')">{{date.day_two.dotw}}, {{date.day_two.date}}</button>
    <button class="schedule-tab-btn" onclick="switchScheduleTab(this, 'mon')">{{date.day_three.dotw}}, {{date.day_three.date}}</button>
    <button class="schedule-tab-btn" onclick="switchScheduleTab(this, 'tue')">{{date.day_four.dotw}}, {{date.day_four.date}}</button>
  </div>

  {% if flaghashike or flaghasboat %}
  <div class="schedule-tab-panel active" id="tab-sat">
    {% with day_schedule=schedule.outing %}
    {% include "include/schedule2026.md" %}
    {% endwith %}
  </div>
  {% endif %}

  <div class="schedule-tab-panel{% if not flaghashike and not flaghasboat %} active{% endif %}" id="tab-sun">
    {% with day_schedule=schedule.writing_day, day_room="writing" %}
    {% include "include/schedule2026.md" %}
    {% endwith %}
  </div>

  <div class="schedule-tab-panel" id="tab-mon">
    <div class="schedule-rooms-legend">
      <span class="room-badge room-main">{{about.mainroom}}</span>
      <span class="room-badge room-unconf">{{about.unconfroom}}</span>
    </div>
    {% with day_schedule=schedule.talks_day1, day_room="talks" %}
    {% include "include/schedule2026.md" %}
    {% endwith %}
  </div>

  <div class="schedule-tab-panel" id="tab-tue">
    <div class="schedule-rooms-legend">
      <span class="room-badge room-main">{{about.mainroom}}</span>
      <span class="room-badge room-unconf">{{about.unconfroom}}</span>
    </div>
    {% with day_schedule=schedule.talks_day2, day_room="talks" %}
    {% include "include/schedule2026.md" %}
    {% endwith %}
  </div>
</div>

<script>
function switchScheduleTab(btn, day) {
  document.querySelectorAll('.schedule-tab-btn').forEach(function(b) { b.classList.remove('active'); });
  document.querySelectorAll('.schedule-tab-panel').forEach(function(p) { p.classList.remove('active'); });
  btn.classList.add('active');
  document.getElementById('tab-' + day).classList.add('active');
}
</script>
```

{% endif %}
