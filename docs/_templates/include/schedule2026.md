<article class="schedule">
{% for session in day_schedule %}
  <div class="schedule-item">
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
      {% if day_room == "talks" %}
        {% if session.data %}
          <div class="item-room"><span class="room-badge room-main">Main stage</span></div>
        {% elif "Unconference" in (session.title or "") %}
          <div class="item-room"><span class="room-badge room-unconf">Library &amp; Astoria</span></div>
        {% elif "Welcome Wagon" in (session.title or "") %}
          <div class="item-room"><span class="room-badge room-unconf">1st floor</span></div>
        {% elif "Lightning" in (session.title or "") %}
          <div class="item-room"><span class="room-badge room-main">Main stage</span></div>
        {% elif "Sponsor" in (session.title or "") %}
          <div class="item-room"><span class="room-badge room-main">Main stage</span></div>
        {% endif %}
      {% endif %}
    </div>
  </div>
{% endfor %}
</article>
