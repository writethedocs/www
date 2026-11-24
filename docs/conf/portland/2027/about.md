---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
banner: _static/conf/images/photos/team-2026-55266368424.jpg
---

# About the Conference

We invite you to join hundreds of other folks for a three-day event to explore the art and science of documentation.
The Write the Docs conference covers any topic related to documentation in the software industry.
Past talks have also covered such diverse topics as empathy, the history of math symbols, and using emoji to keep your users' attention.

Write the Docs brings *everyone* who writes the docs together in the same room: writers, developers, support engineers, community managers, developer relations, and more.
We all have things to learn, and there's no better way than gathering at our events and sharing knowledge.

## Who attends

Each conference brings together around {{ about.attendees }} documentarians, most of them from companies in the software industry.

<div class="share-bar">
{% for share in about.audience %}  <span class="seg seg-{{ loop.index }}" style="width: {{ share.percent }}%;" title="{{ share.label }} ({{ share.percent }}%)"></span>
{% endfor %}</div>
<ul class="share-legend">
{% for share in about.audience %}  <li><i class="seg-{{ loop.index }}"></i>{{ share.label }} <b>{{ share.percent }}%</b></li>
{% endfor %}</ul>

- {{ about.documentarians }}% of attendees write or manage documentation. Programmers and developer relations roles are {{ about.engineering }}% between them.
- Roughly 1 in 5 attendees holds a manager-level role: documentation managers, product and project managers, directors and team leads.
- Half the room is new each year. {{ about.first_time }}% of our Portland 2026 attendees had never been to a Write the Docs conference, so you'll be in good company if this is your first one.
- Oregon, Washington and California are 42% of the room, and 13% of attendees travel from outside the US.

These figures come from the 566 registration survey responses at Write the Docs Portland 2026.
