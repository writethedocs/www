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

{% for talk in data %}

      <div class="row">
        <div class="col-xs-2">
          <p>{{ talk.Time }}</p>
        </div>
        <div style="color: black;" class="col-xs-10">
          <p>

          {{ talk.Session }}

          </p>
        </div>
      </div>

{% endfor %}
