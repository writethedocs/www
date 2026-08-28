---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
---

```{post} August 18, 2026
:tags: {{shortcode}}-{{year}}
```

# Welcome to Write the Docs {{ city }} {{ year }}!

Our conference kicks off in a few days! We're looking forward to gathering in {{ city }} and online, for a few days of talks, an Unconference, and the return of Writing Day. We hope you're as excited as we are! Below is an overview of the conference, along with a couple of announcements.

## Important Links

The website is full of useful information about the conference, venue, and {{ city }}. We encourage you to check out a few of our pages below:

- [Attendee Guide](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/attendee-guide/)
- [Visiting Berlin](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/)
- [Schedule](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/)
- [Meet the Team](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/team/)
- [Code of Conduct](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/code-of-conduct/)

```{figure} /_static/conf/images/pics/portland-unconference.jpg
```

## How to Participate in the Conference

- **Writing Day:** Join us on {{ date.day_two.dotw }} to collaborate with fellow documentarians on a project. We've already shared the full schedule, and it's all on the [Writing Day page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/writing-day/). If you'd like to join the **New to Git** workshop, [sign up soon]({{ writing_day.git_signup_url }}), since space is limited. Everything else is drop-in, and you're welcome to bring your own project.
- **Welcome Reception:** Do not miss our {{ date.day_two.dotw }} evening reception at {{ about.venue }}! Pick up your badge, meet other attendees, and enjoy drinks and snacks on us.
- **Speaker Talks:** Take a look at our schedule and pick the talks you want to attend. [View our lineup here](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/#monday-september-7).
- **Unconference:** Lead or attend a session so you can connect with like-minded folks about topics you care about. We're accepting Monday session sign-ups now. [Learn more about signing up](#monday-unconference-sessions-open).
- **Lightning Talks:** Do you have an idea, concept, or topic you'd like to share with our community in five minutes? We're now accepting Monday submissions. [Learn more about submitting a talk](#monday-lightning-talk-submissions-open).
- **Monday Night Social:** Our offsite gathering is an informal way to relax with fellow attendees, and again enjoy some drinks and snacks on us! Held at {{ about.social_venue }}.
- **Virtually:** Want to stream speaker talks and Q&As from the comfort of your own home? [Attend the conference virtually](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/virtual/).

**[TODO: ticket status — e.g. "In-person tickets are sold out. Virtual ticket registrations will close on September 5.".]**

## Monday Unconference Sessions Open

We've already opened up the Monday Unconference sign-ups! Unconferences are amazing ways to foster connection within our community, and we hope this gives more visibility to the earlier Monday slots. [Learn more about the Unconference here](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/unconference/).

{% if unconf.url %}
```{button-link} {{ unconf.url }}
Sign up to Lead a Monday Unconference
```
{% endif %}

And as always, sign-ups are also welcome during the conference.

## Monday Lightning Talk Submissions Open

We have opened up Monday Lightning Talk submissions. Lightning Talks are a wonderful way to share an idea, concept, or piece of information you find interesting, in an informal five-minute talk. [Learn more about giving a Lightning Talk here.](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/lightning-talks/)

{% if lightning_talks.signup_url %}
```{button-link} {{ lightning_talks.signup_url }}
Submit your Monday Lightning Talk
```
{% endif %}

Tuesday Lightning Talk sign-ups will open later.

## Join our Slack Community

### #wtd-conferences channel

Our [#wtd-conferences](https://writethedocs.slack.com/archives/C1AKFQATH) channel is the primary space for communication during the conference. We encourage you to join the discussion.

We'll be posting announcements in that channel throughout the conference, and we welcome attendees to connect with each other leading up to and during the conference in there, too!

[Join the conversation!](https://docs.google.com/forms/d/e/1FAIpQLSdq4DWRphVt1qVqH8NsjNnS0Szu_NljjZRUvyYqR7mdc00zKQ/viewform)

## FAQ

**Where do I check in?**

Registration opens on {{ date.day_two.dotw }} morning for Writing Day, and again in the morning on Monday and Tuesday, at the entrance of {{ about.venue }}.

**How can I stream talks?**

This conference has virtual and in-person ticket options. All in-person and virtual ticket holders will receive a login link for the virtual conference platform, where we'll be streaming main stage talks and Q&As live. For in-person attendees, this may come in handy if you can't be at the venue for part of the event.

**Do you cater lunch?**

No, we don't cater a full lunch, but we provide coffee, tea and drinks throughout the day, morning fruit and pastries, and an afternoon dessert. [TODO: CHECK] The Cafeteria at {{ about.venue }} will be open during the conference. There are a number of great restaurants within walking distance. View our [Visiting Berlin](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/visiting/) page for more ideas.

**Do you have a place to store luggage?**

Yes, we do! Go to Registration and they will check your bags. Space may be limited.

**Do you have a Parents Room?**

Yes, visit Registration to get access.

## Thanks To Our Sponsors

Thanks to our sponsors for supporting the conference this year. A number of them will be present on Monday and Tuesday. We hope you get a chance to talk with them while you're here.

A message from Mintlify:

> Mintlify is sponsoring Write the Docs Berlin and we can't wait to meet you! We build a docs platform that makes sure your content is agent-ready and gives you top notch tooling without having to maintain it yourself.

> Visit us at the sponsor tables to chat about making your content agent-friendly, empowering more people across your organization to contribute to docs, docs-as-code, or anything else. It's a treat to meet our users and share what we're building.

> See you in Berlin!

Thanks to all our sponsors:

```{eval-rst}
.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-config.yaml
   :template: {{year}}/sponsors-simplelist.rst
```

See you soon!
