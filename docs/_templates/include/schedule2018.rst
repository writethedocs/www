.. raw:: html

{% set dont_link = ['Lunch',
                    'Snack break',
                    'Switch Speakers',
                    'Doors Open, Breakfast Served',
                    'Introduction & State of the Docs',
                    'Lightning Talks',
                    'Day 1 wraps up',
                    'Closing & Group Photo',
                    'Day 2 wraps up',
                    'Writing Day Introduction - Introduction to Sprints & Project Introductions',
                    'Team up and start working',
                    'Lunch Break',
                    'End of Writing Day, Beginning of Reception',
                    'End of Reception',
                    'Introduction to Write the Docs',
                    'Workshop begins: Learn how to Git',
                    'Workshop ends: Learn how to Git. Lunch Break',
                    'Workshop begins: Structuring and writing documentation',
                    'Workshop ends: Structuring and writing documentation',
                    '5 Min Switch Speakers',
                    'Group Photo',
                    'Closing Announcements',
                    'Snacks & milling about and chatting with other attendees',
                    'Write the Docs meetup social and conference after-party',
                    ] %}

    <article class="schedule">
    {% for talk in data %}
          <div class="schedule-item">
              <div class="item-starting-time">{{ talk.Time }}</div>
              <div class="item-content">
                  <div class="item-description">
                  {% if talk.Slug %}
                     <a href="../speakers/#speaker-{{ talk.Slug }}">{{ talk.Session }}</a>
                  {% else %}
                    {{ talk.Session }}
                  {% endif %}
                  </div>
                  <!-- <div class="item-speaker"></div> -->
              </div>
          </div>
    {% endfor %}
    </article>
