---
template: {{year}}/generic.html
banner: _static/conf/images/photos/talk-stage-podium-55257879930.jpg
---

# Virtual Attendance

We're excited to offer a virtual attendance option for Write the Docs {{name}} {{year}}.
The virtual component will run on **{{date.conference.date}}** alongside our in-person conference.
If you can't join us in person, you can still participate and connect from wherever you are.

## The platform

We'll be hosting the virtual conference on [Venueless](https://venueless.org).
You get one login link. The talks play on the main stage, the chat is always on the right-hand side of any page, and the schedule is on the **Reception** page.
Under **Sessions** you'll find the hallway sessions, where you can join with your own audio and video, or chat only.

## What you can do

### Watch the talks live

Watch all talks and Q&A sessions on the main stage live, in {{tz}}.

### Ask the speakers questions

Each talk is followed by a moderated Q&A. Send in your question using the QR code, and our moderators will put it to the speaker. Virtual attendees use the same QR code.

### Meet other attendees

A virtual hallway track and chat inside Venueless, so you can network with other remote attendees.
You can also find the community in [#wtd-conferences](https://writethedocs.slack.com/archives/C1AKFQATH) on Slack.

### Join the Unconference

From the Venueless platform, look for the **Virtual unconference** channel and take a look at the sign-up sheet for the slots or sessions of the day.
Read more about the [Unconference](/conf/{{shortcode}}/{{year}}/unconference/).

### Watch again afterwards

Conference talk videos are available 2-3 weeks after the event on the [Write the Docs YouTube channel](https://www.youtube.com/c/WritetheDocs).

## Tickets

| Ticket type           | Virtual                                 |
| :-------------------- | :-------------------------------------- |
| Student or unemployed | {{ tickets.virtual_student.price }}     |
| Independent           | {{ tickets.virtual_independent.price }} |
| Corporate             | {{ tickets.virtual_corporate.price }}   |

All in-person tickets include access to the virtual platform too.

{% if flagticketsonsale %}
```{button-link} https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}
:year: {{ year }}
Buy a virtual ticket
```
{% else %}
Tickets will be available in {{ date.tickets_live }}.
{% endif %}

See the [tickets page](/conf/{{shortcode}}/{{year}}/tickets/) for in-person tickets and the refund policy.

## Getting Started

You'll receive an email titled **Virtual platform access for Write the Docs** one week before the conference, and again on the day of the conference, with:

* Your unique login link for Venueless
* A quick start guide for the platform
* Information about testing your setup
