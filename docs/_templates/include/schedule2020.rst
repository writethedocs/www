.. raw:: html

    <article class="schedule">
    {% for session in day_schedule %}
          <div class="schedule-item">
              <div class="item-starting-time">{{ session.time }}</div>
              <div class="item-content">
                  <div class="item-description">
                  {% if session.title %}
                      {{ session.title }}
                  {% elif session.data %}
                     <a href="../speakers/#speaker-{{ session.data.speakers.0.slug }}">{{ session.speaker_names }} - {{ session.data.title }}</a>
                  {% else %}
                     ERROR: {{ session }}
                  {% endif %}
                  </div>
                  <!-- <div class="item-speaker"></div> -->
              </div>
          </div>
    {% endfor %}
    </article>
