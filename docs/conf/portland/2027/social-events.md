---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
banner: _static/conf/images/photos/roof-deck-55246787066.jpg
---

# Social Events

Write the Docs is a community conference,
which means a big part of the experience is meeting and getting to know other documentarians.
Along with the talks and Unconference sessions,
we have a few social events planned to help you connect with other attendees.

## Sunday Reception

We encourage everyone to drop by on Sunday evening for the conference reception.
This is a great chance to meet other attendees,
and make sure you know your way around the conference venue.

**Where**: {{about.venue}}, {{about.unconfroom}} and Show Bar  
**When**: {{ date.day_two.reception_time }}

*Both alcoholic and non-alcoholic drinks and snacks will be provided.*

{% if social_events.reception_sponsor %}
{% set sponsor = sponsors|find_sponsor(social_events.reception_sponsor) %}
### Sponsored by

<p style="text-align: center; margin-top: 1em;">
<a href="{{ sponsor.link }}" style="border-bottom: none;"><img src="{{ sponsor.name|sponsor_photo }}" alt="{{ sponsor.brand }}" style="max-width: 250px;"></a>
</p>

*The Sunday Reception is sponsored by [{{ sponsor.brand }}]({{ sponsor.link }}).*
{% endif %}

## Monday Night Social

Join us for our Monday night social event! This is a great chance to meet more of your fellow documentarians 
and chat about the conference in a relaxed atmosphere.

**Where**: {{about.social_venue}}  
**When**: {{ date.day_three.social_time }}

*Both alcoholic and non-alcoholic drinks and snacks will be provided.*

{% if social_events.social_sponsor %}
{% set sponsor = sponsors|find_sponsor(social_events.social_sponsor) %}
### Sponsored by

<p style="text-align: center; margin-top: 1em;">
<a href="{{ sponsor.link }}" style="border-bottom: none;"><img src="{{ sponsor.name|sponsor_photo }}" alt="{{ sponsor.brand }}" style="max-width: 250px;"></a>
</p>

*The Monday Night Social is sponsored by [{{ sponsor.brand }}]({{ sponsor.link }}).*
{% endif %}
