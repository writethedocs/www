.. raw:: html

    <article class="schedule">
    {% for talk in day_schedule %}
          <div class="schedule-item">
              <div class="item-starting-time">{{ talk.time }}</div>
              <div class="item-content">
                  <div class="item-description">
                  {% if talk.title %}
                      {{ talk.title }}
                  {% elif talk.data %}
                     <a href="../speakers/#speaker-{{ shortcode }}-{{ year }}-{{ talk.data.speakers.0.slug }}">{{ talk.speaker_names }} - {{ talk.data.title }}</a>
                  {% else %}
                     ERROR: {{ talk }}
                  {% endif %}
                  </div>
                  <!-- <div class="item-speaker"></div> -->
              </div>
          </div>
    {% endfor %}
    </article>
