---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

```{post} September 2, 2026
:tags: {{shortcode}}-{{year}}
```

# Welcome to Write the Docs {{ city }} {{ year }}!

Our conference kicks off in just a few days! We can't wait to gather with you — in {{ city }} and online — for two days of talks, an Unconference, and the return of Writing Day. Below is an overview of the conference, along with a few announcements.

## Important Links

The website is full of useful information about the conference, venue, and {{ city }}. We encourage you to check out a few of our pages below:

- [Attendee Guide](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/attendee-guide/)
- [Visiting Berlin](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/)
- [Schedule](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/)
- [Meet the Team](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/team/)
- [Code of Conduct](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/code-of-conduct/)

```{figure} /_static/conf/images/pics/berlin-2025-opening.jpg
```

## How to Participate in the Conference

- **Writing Day:** Join us on {{ date.day_two.dotw }} to collaborate with fellow documentarians on a project. We've already shared the full schedule, and it's all on the [Writing Day page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/writing-day/). If you'd like to join the **New to Git** workshop, [sign up soon]({{ writing_day.git_signup_url }}), since space is limited. Everything else is drop-in, and you're welcome to bring your own project.
- **Welcome Reception:** Do not miss our {{ date.day_two.dotw }} evening reception at {{ about.venue }}! Everyone with a conference ticket is welcome, whether or not you join Writing Day. Pick up your badge, meet other attendees, and enjoy drinks and snacks on us.
- **Speaker Talks:** Take a look at our schedule and pick the talks you want to attend. [View our lineup here](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/#monday-september-7).
- **Unconference:** Lead or attend a session so you can connect with like-minded folks about topics you care about. We're accepting sign-ups for {{ date.day_three.dotw }} morning sessions now. [Learn more about signing up](#monday-unconference-sessions-open).
- **Lightning Talks:** Do you have an idea, concept, or topic you'd like to share with our community in five minutes? We're now accepting {{ date.day_three.dotw }} submissions. [Learn more about submitting a talk](#monday-lightning-talk-submissions-open).
- **{{ date.day_three.dotw }} Night Social:** Our offsite gathering is an informal way to relax with fellow attendees, and again enjoy some drinks and snacks on us! Held at {{ about.social_venue }}.
- **Virtually:** Want to stream speaker talks and Q&As from the comfort of your own home? [Attend the conference virtually](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/virtual/).

There are still [a few tickets available](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/tickets/). Virtual registration will close on September 6.

## {{ date.day_three.dotw }} Unconference Sessions Open

We've already opened up the {{ date.day_three.dotw }} morning Unconference sign-ups! Unconferences are amazing ways to foster connection within our community, and we hope this gives more visibility to the earlier {{ date.day_three.dotw }} slots. [Learn more about the Unconference here](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/unconference/).

{% if unconf.url %}
```{button-link} {{ unconf.url }}
Sign up to Lead a {{ date.day_three.dotw }} Morning Unconference Session
```
{% endif %}

And as always, sign-ups are also welcome during the conference.

## {{ date.day_three.dotw }} Lightning Talk Submissions Open

We have opened up {{ date.day_three.dotw }} Lightning Talk submissions. Lightning Talks are a wonderful way to share an idea, concept, or piece of information you find interesting, in an informal five-minute talk. [Learn more about giving a Lightning Talk here.](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/lightning-talks/)

{% if lightning_talks.signup_url %}
```{button-link} {{ lightning_talks.signup_url }}
Submit your {{ date.day_three.dotw }} Lightning Talk
```
{% endif %}

{{ date.day_four.dotw }} Lightning Talk sign-ups will open later.

## Access to the Virtual Platform

You'll receive your virtual platform access link in a separate email today.
This will be sent to the email address of each ticket holder.
You'll also receive this if you have an in-person ticket, in case you can't or don't want to come into the venue some of the time.

## Join our Slack Community

### #wtd-conferences channel

Our [#wtd-conferences](https://writethedocs.slack.com/archives/C1AKFQATH) channel is the primary space for communication during the conference. We encourage you to join the discussion.

We'll be posting announcements in that channel throughout the conference, and we welcome attendees to connect with each other leading up to and during the conference in there, too!

[Join the conversation!](https://docs.google.com/forms/d/e/1FAIpQLSdq4DWRphVt1qVqH8NsjNnS0Szu_NljjZRUvyYqR7mdc00zKQ/viewform)

## FAQ

**Where do I check in?**

Registration opens on {{ date.day_two.dotw }} morning for Writing Day, and is open for the entire conference on {{ date.day_three.dotw }} and {{ date.day_four.dotw }}. It is located at the entrance of {{ about.venue }}.

**How can I stream talks?**

This conference has virtual and in-person ticket options. All in-person and virtual ticket holders will receive a login link for the virtual conference platform, where we'll be streaming main stage talks and Q&As live. For in-person attendees, this may come in handy if you can't be at the venue for part of the event.

**Do you cater lunch?**

No, we don't cater a full lunch, but we provide coffee, tea and drinks throughout the day, morning fruit and pastries, and an afternoon dessert. **The Cafeteria at {{ about.venue }} is open only on Tuesday.** There are a number of great restaurants within walking distance. View our [Visiting Berlin](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/) page for more ideas.

**Do you have a place to store luggage?**

Yes, we do! Go to Registration and they will check your bags.

**Do you have a Parents Room?**

Yes, visit Registration to get access.

**Will you publish videos of the talks?**

Yes, all talks are recorded and videos will be published within a few weeks after the conference.
Writing Day and Unconference sessions are not recorded.

## Thanks To Our Sponsors

Thanks to our sponsors for supporting the conference this year. A number of them will be present on {{ date.day_three.dotw }} and {{ date.day_four.dotw }}. We hope you get a chance to talk with them while you're here.

A message from Mintlify:

> Mintlify is sponsoring Write the Docs Berlin and we can't wait to meet you! We build a docs platform that makes sure your content is agent-ready and gives you top notch tooling without having to maintain it yourself.
>
> Visit us at the sponsor tables to chat about making your content agent-friendly, empowering more people across your organization to contribute to docs, docs-as-code, or anything else. It's a treat to meet our users and share what we're building.
>
> See you in Berlin!

Thanks to all our sponsors:

```{eval-rst}
.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-config.yaml
   :template: {{year}}/sponsors-simplelist.rst
```

See you soon!
