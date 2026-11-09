---
template: {{year}}/news.html
banner: _static/conf/images/headers/2026/news.jpg
---

# News

Updates from the team. More here as it happens!

<!-- news-latest -->

## Join our mailing list

Stay connected with the Write the Docs community! Our mailing lists send out messages 1-2 times a month, and your email won't be shared or used for any other purpose.

{% include "conf/mailing-list.html" %}

## All posts

```{postlist} 100
:date: "%A, %B %d, %Y"
:format: "{date}{title}"
:list-style: none
:tags: "{{ shortcode }}-{{ year }}"
```
