<article class="schedule">
{% for session in day_schedule %}
  <div class="schedule-item
    {%- if day_type == 'talks' -%}
      {%- if session.data or 'Lightning' in (session.title or '') or 'Q&A' in (session.title or '') -%}
        {{ ' ' }}schedule-item--main
      {%- elif 'Unconference' in (session.title or '') -%}
        {{ ' ' }}schedule-item--unconf
      {%- elif 'Welcome Wagon' in (session.title or '') -%}
        {{ ' ' }}schedule-item--unconf
      {%- elif 'Sponsor' in (session.title or '') -%}
        {{ ' ' }}schedule-item--main
      {%- elif 'Social event' in (session.title or '') or 'Reception' in (session.title or '') -%}
        {{ ' ' }}schedule-item--social
      {%- endif -%}
    {%- elif day_type == 'writing' -%}
      {%- if 'Welcome Wagon' in (session.title or '') -%}
        {{ ' ' }}schedule-item--unconf
      {%- elif 'Reception' in (session.title or '') -%}
        {{ ' ' }}schedule-item--social
      {%- elif 'Roundtable' in (session.title or '') or 'workshop' in (session.title or '') or 'writing' in (session.title or '') or 'Writing' in (session.title or '') or 'Projects' in (session.title or '') or 'Afternoon session' in (session.title or '') or 'Morning introduction' in (session.title or '') -%}
        {{ ' ' }}schedule-item--writing
      {%- endif -%}
    {%- elif day_type == 'outing' -%}
      {{ ' ' }}schedule-item--outdoor
    {%- endif -%}
  ">
    <div class="item-starting-time">{{ session.time }}</div>
    <div class="item-content">
      <div class="item-description">
        {% if session.title %}
          {{ session.title | safe }}
        {% elif session.data %}
          <a href="../speakers/#speaker-{{ session.data.speakers.0.slug }}-{{ session.data.slug }}">{{ session.speaker_names }} - {{ session.data.title }}</a>
        {% else %}
          ERROR: {{ session }}
        {% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</article>
