---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

```{post} July 16, 2026
:tags: {{shortcode}}-{{year}}, speakers, tickets, visiting, writing-day, social, shirts, sponsors, volunteer
```

# Conference is 2 Months Away!

Write the Docs {{ city }} is just two months away, on **{{ date.short }}**. This year, we've added Writing Day back in, on {{ date.day_two.dotw }}. If you have not grabbed your ticket yet, now is a great time. Check out our [speaker lineup](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speakers/), or read on to learn about our Attendee Guide, Writing Day, our Welcome Reception, T-shirts, and tips for planning your trip to Berlin.

<!-- call to action button -->
<table cellpadding="0" cellspacing="0" width="200" role="presentation" align="center" class="cta">
<tr><td height="30"></td></tr>
<tr><td style="background:#FDB913;padding:10px 15px;border-radius:8px;text-align:center"><a href="https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}" target="_blank" style="color:#4A4A4A;text-decoration:none;font-size:15px;font-weight:bold;text-transform:uppercase">Buy your ticket</a></td></tr>
<tr><td height="30"></td></tr></table>
<!-- / call to action button -->

## Prepare for the conference with the Attendee Guide

Wondering where to ask questions, where to get food, or how to get the most out of Write the Docs? Check out our [Attendee Guide](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/attendee-guide/) for all that info and more.

## Writing Day kicks off the conference

Writing Day is on **{{ date.day_two.dotw }}, {{ date.day_two.date }}** at [bUm](https://www.bum.berlin/), and is included with every in-person ticket. It is a full day for documentarians to work together on real projects, whether that is open-source documentation, community content, or something you bring yourself.

**{{ date.day_two.dotw }}, {{ date.day_two.date }}, {{ date.day_two.writing_day_time }} {{ tz }}**

- **Morning Session**
  - Welcome and overview
  - Project announcements: Leads give a 2 minute summary and projects begin
- **Lunch Break**
- **Afternoon Session**
  - Project announcements: Leads give a 2 minute summary, starting with the afternoon-only projects, and projects reconvene

We invite you to lead a half-day or full-day project, or you can show up and join one on the day. If you plan to lead, submit your project by **{{ writing_day.project_deadline }}** and we will share it in a pre-conference blog post and email.

{% if writing_day.url %}
<!-- call to action button -->
<table cellpadding="0" cellspacing="0" width="320" role="presentation" align="center" class="cta">
<tr><td height="30"></td></tr>
<tr><td style="background:#FDB913;padding:10px 15px;border-radius:8px;text-align:center"><a href="{{ writing_day.url }}" target="_blank" style="color:#4A4A4A;text-decoration:none;font-size:15px;font-weight:bold;text-transform:uppercase">Submit Your Writing Day Project</a></td></tr>
<tr><td height="30"></td></tr></table>
<!-- / call to action button -->
{% endif %}

See the [Writing Day page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/writing-day/) for more details.

## Sign up to volunteer

Volunteers help the conference run smoothly and receive a **free ticket** in exchange for two or more 3-4 hour shifts. Volunteer applications close on **{{ volunteer.applications_close }}**. Visit our [Volunteer page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/volunteer/) to learn more and sign up.

## Welcome Reception

New this year, we are hosting our Welcome Reception on {{ date.day_two.dotw }} evening. This is a great chance to get your badge and meet other attendees.

**When**: {{ date.day_two.dotw }}, {{ date.day_two.reception_time }} {{ tz }}

Both alcoholic and non-alcoholic drinks and snacks will be provided.

## Planning your trip to Berlin

If you are travelling to Berlin, our [Visiting Berlin](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/) page has tips on getting around, neighbourhoods to consider staying in, and things to do while you are here. The [Venue page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/venue/) has directions to bUm from the nearest U-Bahn stations, including notes on step-free access.

## Join the conversation on Slack

Our [Slack community](https://www.writethedocs.org/slack/) is the best place to connect with other attendees before, during, and after the conference. The `#wtd-conferences` channel is the primary space for conference chatter. If you have not joined yet, note that there is a short signup form before you can create your account.

## T-shirts are now available

The [Write the Docs {{ city }} {{ year }} T-shirt Shop]({{ shirts.url }}) is open! We're doing a mail order shop so people can order the exact shirt they want, if they want one. Shipping is available from the USA or Europe. We recommend you order your shirt at least 2-3 weeks in advance if you want to sport your new garb during the conference.

## Thanks to our sponsors

We are grateful to have the support of the following companies in {{year}}:

```{eval-rst}
.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-config.yaml
   :template: {{year}}/sponsors-simplelist.rst
```

If your company is interested in sponsoring, you can find all the details in our [sponsorship prospectus](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/sponsors/prospectus/).

For the latest updates, follow us on [LinkedIn](https://www.linkedin.com/company/write-the-docs), [Bluesky](https://bsky.app/profile/writethedocs.bsky.social), and [Mastodon](https://fosstodon.org/@writethedocs).

We look forward to seeing you in Berlin in September!
