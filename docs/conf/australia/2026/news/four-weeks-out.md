---
template: {{year}}/generic.html
banner: _static/conf/images/headers/WTDHeader.png
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

```{post} November 4, 2026
:tags: {{shortcode}}-{{year}}, tickets, social, sponsors
```

# Only 4 weeks until Write the Docs Australia

Write the Docs Australia is officially just under 4 weeks away, on {{ date.main }}! Whether you're a programmer, tech writer, designer, project manager, or developer advocate, we have talks and a community for you.

## Get your tickets

We will be closing ticket sales **Saturday, 21st November**, so if you've been on the fence, now is the time to buy one!

| Ticket type                         | In person (AUD) &nbsp; &nbsp;   | Virtual (AUD)                           |
| :---------------------------------- | :------------------------------ | :-------------------------------------- |
| Student or unemployed &nbsp; &nbsp; | {{ tickets.student.price }}     | {{ tickets.virtual_student.price }}     |
| Independent                         | {{ tickets.independent.price }} | {{ tickets.virtual_independent.price }} |
| Corporate                           | {{ tickets.corporate.price }}   | {{ tickets.virtual_corporate.price }}   |

In-person space is limited, so we recommend getting your ticket soon.

```{button-link} https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}
:year: {{ year }}
Buy your ticket
```

## How do I participate in the conference?

There are a number of ways to engage in the conference. You can listen to Speaker Talks, participate in the [Fishbowl](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/fishbowl/) session, give a [Lightning Talk](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/lightning-talks/), or chat with our Sponsors!

View our [Attendee Guide](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/attendee-guide/) for strategies and tips on how to get plugged in and connect with others!

View our [Schedule](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/) page for exact times of the conference.

## Thursday night social

This is an event just for conference attendees, held on *Thursday evening from 5pm-7pm*, with free snacks and drinks. It will be held at **Springrock Public Bar**, Level 1/87 Bourke St, Melbourne, with a range of alcoholic and non-alcoholic beverage options.

## Planning your trip to Melbourne

If you're travelling in, our [Visiting Melbourne](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/) page has tips on getting around and neighbourhoods to consider, and the [Venue page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/venue/) has directions to {{ about.venue }}.

## Join our Slack community

Our Slack network is the best way to connect with our community. Visit our [Slack info page](https://www.writethedocs.org/slack/) to join and explore a list of our channels.

### #australia-oceania channel

The [#australia-oceania](https://writethedocs.slack.com/archives/C09UGF22W) channel is the primary space for conference communication. We *highly* recommend that you join the discussion before the conference!

To join our Slack, you need to complete a short signup form before you can create your account.

```{button-link} https://docs.google.com/forms/d/e/1FAIpQLSdq4DWRphVt1qVqH8NsjNnS0Szu_NljjZRUvyYqR7mdc00zKQ/viewform
:year: {{ year }}
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
