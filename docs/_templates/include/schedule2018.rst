.. raw:: html

{% set shortcode = env.app.config.html_context.shortcode %}
{% set year = env.app.config.html_context.year %}

    <article class="schedule">
    {% for talk in data %}
          <div class="schedule-item">
              <div class="item-starting-time">{{ talk.Time }}</div>
              <div class="item-content">
                  <div class="item-description">
                  {% if talk.Slug %}
                     <a href="../speakers/#speaker-{{ shortcode }}-{{ year }}-{{ talk.Slug }}">{{ talk.Session }}</a>
                  {% else %}
                    {{ talk.Session }}
                  {% endif %}
                  </div>
                  <!-- <div class="item-speaker"></div> -->
              </div>
          </div>
    {% endfor %}
    </article>
