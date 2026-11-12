---
template: {{year}}/news.html
banner: _static/conf/images/headers/2026/news.jpg
---

# News

Announcements from the Write the Docs {{ name }} {{ year }} team, as they happen: the call for
proposals, speakers, the schedule and tickets. Each one also goes out to our
mailing list, so [join it](#join-our-mailing-list) to get the next one by email.

## Latest news

<!-- news-latest -->

## Join our mailing list

Get these announcements by email, along with our monthly newsletter: the best
conversations from Slack, plus news from all our conferences. Choose what you'd
like to hear about. Your information will never be shared with anyone, and you
can unsubscribe at any time.

{% include "conf/mailing-list.html" %}

## All posts

```{postlist} 100
:date: "%A, %B %d, %Y"
:format: "{date}{title}"
:list-style: none
:tags: "{{ shortcode }}-{{ year }}"
```
