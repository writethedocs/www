---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

```{eval-rst}
.. post:: October 3, {{year}}
   :tags: {{shortcode}}-{{year}}
```

# Just Under One Month Until Write the Docs {{name}}

Write the Docs {{name}} is officially just under one month away on October 27-28! Whether you're a programmer, tech writer, designer, project manager, or developer advocate, we have talks and a community for you.

## Buy Your Tickets

Still need a ticket? Now is a great time to purchase your ticket at one of our varying price levels.

- In-person Student or Unemployed Tickets: {{tickets.student.price}} 
- In-person Independent Tickets: {{tickets.independent.price}} 
- In-person Corporate Tickets: {{tickets.corporate.price}} 
- Virtual Student or Unemployed Tickets: {{tickets.virtual_student.price}}
- Virtual Independent Tickets: {{tickets.virtual_independent.price}}
- Virtual Corporate Tickets: {{tickets.virtual_corporate.price}}
   
We do expect in-person tickets to sell out some time before the conference.

```{button-link} https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/tickets/
:color: "#2ecc71"
Buy your ticket
```

## Join our Slack Community

Our Slack network is the best way to connect with our community. Visit our [Slack info page](https://www.writethedocs.org/slack/) to join and explore a list of our channels.

### #wtd-conferences channel
Our [#wtd-conferences](https://writethedocs.slack.com/archives/C1AKFQATH) channel is the primary space for virtual communication during the conference. We *highly* recommend you view and join the discussion before the conference!

**Reminder**: There is a two-step process to join Slack. You need to complete a short signup form before you can create your account.

```{button-link} https://docs.google.com/forms/d/e/1FAIpQLSdq4DWRphVt1qVqH8NsjNnS0Szu_NljjZRUvyYqR7mdc00zKQ/viewform
:color: "#2ecc71"
Join Slack today
```

## How Do I Participate in the Conference? 

There are a number of ways to engage in the conference. You can listen to Speaker Talks, facilitate an Unconference session, or chat with our Sponsors!

View our [Attendee Guide](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/attendee-guide/) for strategies and tips on how to get plugged in and connect with others!

View our [Schedule](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/) page for exact times of the conference.

The Unconference schedule will open about a week before the conference, so start thinking about what 
[session you'd like to lead](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/).

## Thanks to our sponsors

We are grateful to have the support of the following companies in {{year}}:

```{eval-rst}
.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-config.yaml
   :template: {{year}}/sponsors-simplelist.rst
```

See you in one month!
