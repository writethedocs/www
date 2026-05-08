.. while called schedule2021, this file applies to 2021 *and newer*

.. raw:: html

    <article class="schedule">
    {% for session in day_schedule %}
          {% set availability = session.availability or day_availability %}
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
                  {% if availability %}
                  <div class="item-availability availability-{{ availability }}">
                      {% if availability == 'both' %}
                          <span class="availability-icon" title="Available in person and virtually">📍 💻</span>
                      {% elif availability == 'in_person' %}
                          <span class="availability-icon" title="In person only">📍</span>
                      {% elif availability == 'virtual' %}
                          <span class="availability-icon" title="Virtual only">💻</span>
                      {% endif %}
                  </div>
                  {% endif %}
                  <!-- <div class="item-speaker"></div> -->
              </div>
          </div>
    {% endfor %}
    </article>
