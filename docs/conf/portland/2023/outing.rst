:template: {{year}}/generic.html

{% if shortcode == '{{ shortcode }}'%}
:banner: _static/conf/images/headers/group.png

Write the Docs Boat Ride
========================

As this year's conference is virtual, we encourage you to go on a boat ride or walk in your own beautiful home town.

{% elif shortcode == 'portland'%}

:banner: _static/conf/images/headers/hike.png

Write the Docs Hike
===================

Every year we have a conference hike, and at this point it's a fantastic tradition.
We'll be doing the same hike again this year, because it's the best one easily accessible from downtown Portland.

It's rained on us the past, but we have faith it will be beautiful this year! We will hopefully see Mount Hood at the top :)

Logistics
---------

**Please register for your ticket so we can contact you in advance for day-of weather and logistics information**

- Tickets: `Register your hike ticket <https://ti.to/writethedocs/write-the-docs-portland-2023/with/hike-ticket>`_
- Date & Time: Leaves promptly at **{{ hike.date }}**.
- Start: **Lower Macleay Park** (`Map link <https://goo.gl/maps/bU7MAMsKCJAbG3zFA>`__). There is a pavilion at the park entrance where we will gather.
- End: **Oregon Zoo** around 4-5pm -- There is a MAX stop here to take us back downtown.
- `Visual of the hike <https://maps.google.com/maps?saddr=MacLeay+Park+Entrance,+NW+Upshur+St,+Portland,+OR&daddr=45.527373,-122.718589+to:45.5225885,-122.717297+to:oregon+zoo&hl=en&ll=45.52448,-122.717757&spn=0.023933,0.032358&sll=45.522345,-122.712822&sspn=0.023934,0.032358&geocode=FYLStgIdMI6v-CGojI77DIHw4SnVqz2N6QmVVDGojI77DIHw4Q%3BFU2xtgIdg3av-CmRNoxzkQmVVDFxAN8jMh2eKQ%3BFZyetgIdj3uv-CnD2fb_jgmVVDHuWX9DnHsevQ%3BFZpttgIdAoGv-CEm_N2esCDn5ykFuFa4LgqVVDEm_N2esCDn5w&oq=macleay+park&gl=us&dirflg=w&mra=dpe&mrsp=2&sz=15&via=1,2&t=m&z=15>`__

We will be hiking in the amazing `Forest Park <http://www.forestparkconservancy.org/>`__, the largest urban forested park in the country.
It is conveniently located in Northwest Portland, not far from the conference venue. It's about a 35 minute walk
from the venue to the park, or you can `take transit <https://www.google.com/maps/dir/Crystal+Ballroom,+1332+W+Burnside+St,+Portland,+OR+97209,+United+States/MacLeay+Park+Entrance,+Northwest+Upshur+Street,+Portland,+OR/@45.5290603,-122.707244,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x54950a02e43decb9:0xe289ad93ad758c66!2m2!1d-122.68483!2d45.522785!1m5!1m1!1s0x549509e98d3dabd5:0xe1f0810cfb8e8ca8!2m2!1d-122.712528!2d45.535874!3e3?hl=en>`__ to make it a bit quicker.

**Note**

The hike does not end where it starts. Take this into consideration when you plan.
There is an out-and-back option if you choose to just go to Pittock Mansion, then return back down to the start.

{% include "conf/portland/hike.rst" %}

{% else %}

We don't have an outing yet.

{% endif %}
