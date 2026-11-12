---
template: {{year}}/generic.html
banner: _static/conf/images/headers/2026/virtual.jpg
---

# Virtual Attendance

We're excited to offer a virtual attendance option for Write the Docs {{name}} {{year}}.
The virtual component will run on **{{date.conference.date}}** alongside our in-person conference.
If you can't join us in person, you can still participate and connect from wherever you are.

## What's included

- **Talks:** Watch all talks and Q&A sessions on the main stage live, in {{tz}}.
- **Q&A:** Each talk is followed by a moderated Q&A. Send in your question using the QR code, and our moderators will put it to the speaker. Virtual attendees use the same QR code.
- **Hallway track:** A virtual hallway track and chat so you can network with other remote attendees.
- **Unconference:** A dedicated **Virtual unconference** channel, with a sign-up sheet for the slots or sessions of the day. Read more about the [Unconference](/conf/{{shortcode}}/{{year}}/unconference/).
- **Videos:** Conference talk videos are available 2-3 weeks after the event on the [Write the Docs YouTube channel](https://www.youtube.com/c/WritetheDocs).

## The platform

We'll be hosting the virtual conference on [Venueless](https://venueless.org).
You get one login link. The talks play on the main stage, the chat is always on the right-hand side of any page, and the schedule is on the **Reception** page.
Under **Sessions** you'll find the hallway sessions, where you can join with your own audio and video, or chat only.

You'll receive an email titled **Virtual platform access for Write the Docs** one week before the conference, and again on the day of the conference, with your unique login link, a quick start guide for the platform, and information about testing your setup.

## Tickets

All in-person tickets include access to the virtual platform too.
See the [tickets page](/conf/{{shortcode}}/{{year}}/tickets/) for in-person tickets and the refund policy.

{% if not flagticketsonsale %}
**Tickets will be available in {{ date.tickets_live }}.**
{% endif %}

{% include "include/virtual-tickets.html" %}
