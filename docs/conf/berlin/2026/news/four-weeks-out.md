---
template: {{year}}/generic.html
banner: _static/conf/images/headers/berlin-2026-group-photo.jpg
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

```{post} August 11, 2026
:tags: {{shortcode}}-{{year}}, tickets, writing-day, shirts, social, sponsors
```

# Only 4 weeks until Write the Docs {{ city }}

Write the Docs {{ city }} is officially just under 4 weeks away, on {{ date.main }}! Whether you're a programmer, tech writer, designer, project manager, or developer advocate, we have talks and a community for you.

## Get your tickets

Still need a ticket? Now is a great time to purchase your ticket.

| Ticket type                         | In person &nbsp; &nbsp;         | Virtual                                 |
| :---------------------------------- | :------------------------------ | :-------------------------------------- |
| Student or unemployed &nbsp; &nbsp; | {{ tickets.student.price }}     | {{ tickets.virtual_student.price }}     |
| Independent                         | {{ tickets.independent.price }} | {{ tickets.virtual_independent.price }} |
| Corporate                           | {{ tickets.corporate.price }}   | {{ tickets.virtual_corporate.price }}   |

In-person space is limited, so we recommend getting your ticket soon.

```{button-link} https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}
Buy your ticket
```

## Writing Day projects

For best visibility, submit your project by **{{ writing_day.project_deadline }}** and we'll include it in our email and on social before the conference. Online project submission is recommended but optional. You're always welcome to introduce a project day of.

New this year, we're also running [Roundtable Discussions](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/writing-day/#roundtable-discussions): pre-scheduled, facilitated afternoon conversations on focused topics, which might include AI in documentation and API docs. All are welcome!

```{button-link} {{ writing_day.url }}
Submit your Writing Day project
```

## How do I participate in the conference?

There are a number of ways to engage in the conference. You can contribute to a Writing Day project, listen to Speaker Talks, facilitate an [Unconference](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/unconference/) session, give a [Lightning Talk](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/lightning-talks/), or chat with our Sponsors!

View our [Attendee Guide](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/attendee-guide/) for strategies and tips on how to get plugged in and connect with others!

View our [Schedule](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/) page for exact times of the conference.

## Welcome Reception and Night Social

We have two evening events this year. On {{ date.day_two.dotw }} we're hosting a Welcome Reception at {{ about.venue }} from {{ date.day_two.reception_time }} {{ tz }}, right after Writing Day. On {{ date.day_three.dotw }} evening we're hosting an off-site social at Straßenbräu Ausschank 2 from {{ date.day_three.social_time }} {{ tz }}. Drinks and snacks are provided at both events, with non-alcoholic options available.

## Planning your trip to Berlin

If you're travelling in, our [Visiting Berlin](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/) page has tips on getting around and neighbourhoods to consider, and the [Venue page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/venue/) has directions to {{ about.venue }}, including notes on step-free access.

## T-shirts

The [Write the Docs {{ city }} {{ year }} T-shirt Shop]({{ shirts.url }}) is open! We're doing a mail order shop so people can order the exact shirt they want. Shipping is available from the USA or Europe, so we recommend ordering at least 2-3 weeks in advance if you want to wear yours at the conference.

## Join our Slack community

Our Slack network is the best way to connect with our community. Visit our [Slack info page](https://www.writethedocs.org/slack/) to join and explore a list of our channels.

### #wtd-conferences channel

The [#wtd-conferences](https://writethedocs.slack.com/archives/C1AKFQATH) channel is the primary space for conference communication. We *highly* recommend that you join the discussion before the conference!

To join our Slack, you need to complete a short signup form before you can create your account.

```{button-link} https://docs.google.com/forms/d/e/1FAIpQLSdq4DWRphVt1qVqH8NsjNnS0Szu_NljjZRUvyYqR7mdc00zKQ/viewform
Join the Write the Docs Slack
```

## Thanks to our sponsors

We are grateful to have the support of the following companies in {{year}}:

```{eval-rst}
.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-config.yaml
   :template: {{year}}/sponsors-simplelist.rst
```

Sponsors help make Write the Docs possible. Their support keeps ticket prices affordable and funds our Opportunity Grants, which help documentarians attend who otherwise could not. Sponsoring is also a direct way to reach and hire from a community of people who care about documentation.

We still have some space for additional sponsors! If your company would like to get involved, our [sponsorship prospectus](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/sponsors/prospectus/) has packages for organizations of every size, and you can reach our team at <sponsorship@writethedocs.org>.

See you in {{ date.month }}!
