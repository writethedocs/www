:template: {{year}}/generic.html
:banner: _static/conf/images/headers/{{ shortcode }}-group.png

Online Sponsorship Prospectus
#############################

.. contents:: Sections
   :local:
   :depth: 1
   :backlinks: none

Introduction
============

Welcome to our **2022 Conference Sponsorship Prospectus**.
This document has been adapted for our hybrid conference format,
including new benefits and increased value across our community.
Our new hybrid format has brought on many questions,
and we're working to create innovative solutions where possible.

We're excited to work with the organizations in our community to build the best possible event in {{ year }}.
In particular, we would love your feedback on sponsorship levels and benefits.
We expanded the offerings and introduced a lot of new things,
but please let us know if there are other points of interaction with our community that would be valuable for you.

Concept
=======

{% include "conf/sponsorship/concept.rst" %}

Demographics
============

{% include "conf/sponsorship/demographics.rst" %}

Why Sponsor
===========

{% include "conf/sponsorship/why.rst" %}

Sponsorship Packages
====================

The following options are suggested sponsorship levels. We are happy to discuss adjustments and custom packages.

Second Draft
------------

The **Second Draft** package is great for companies looking to hire or to promote a product.

- Two (2) tickets
- A small table at our **job fair**
- One (1) featured job postings on our Job Board, also promoted in our newsletter ({{ newsletter_subs }} subscribers)
- A short description (250 characters) and logo of your company on the conference website
- Name included in welcome announcement in email newsletters and social media
- Display 1 promotional (“Swag”) item on the conference swag table (provided by sponsor)

The **Second Draft** package costs **{{sponsorship.second_draft.price}}**.

Publisher
---------

The **Publisher** package is great for sending a team and getting to know the community.

- Five (5) tickets
- A table at our **job fair**
- Two (2) featured job postings on our Job Board, also promoted in our newsletter ({{ newsletter_subs }} subscribers)
- A medium description (500 characters) and logo of your company on the conference website
- Name included in welcome announcement in email newsletters and social media
- Display 2 promotional (“Swag”) items on the conference swag table (provided by sponsor)

The **Publisher** package costs **{{sponsorship.publisher.price}}**.

Patron
------

**Limit 3**

The **Patron** package highlights your company as a force in the industry and community:

- Ten (10) tickets
- A **sponsorship booth**
- A featured table at our **job fair**
- Four (4) featured job postings on our Job Board, also promoted in our newsletter ({{ newsletter_subs }} subscribers)
- A long description (750 characters) and logo of your company on the conference website
- Small logo included **livestream & talk videos**
- 5 minute **sponsored lightning talk**
- A logo on all Write the Docs website pages until the end of {{ year }}. (30,000 pageviews/mo)
- Display unlimited promotional ("Swag") items
- Name included in welcome announcement in email newsletters and social media

The **Patron** package costs **{{sponsorship.patron.price}}**.

Keystone
--------

The **Keystone** package highlights you as our main community partner:

- Fifteen (15) tickets
- A featured **sponsorship booth**
- A featured table at our **job fair**
- Eight (8) featured job postings on our Job Board, also promoted in our newsletter ({{ newsletter_subs }} subscribers)
- Large logo included **livestream & talk videos**
- 5 minute **sponsored lightning talk**
- A long description (750 characters) and logo of your company on the conference website
- A logo on all Write the Docs website pages until the end of {{ year }}. (30,000 pageviews/mo)
- Display unlimited promotional ("Swag") items
- Name included in welcome announcement in email newsletters and social media

The **Keystone** package costs **{{sponsorship.keystone.price}}**.

Other Sponsorship Opportunities
===============================

The following a la carte offerings are available either independently or
combined with one of the previous packages to increase visibility at the event.

Opportunity Grants
------------------

Provide additional money for our Opportunity Grant program,
which provides funding for people to attend the conference.

**{{sponsorship.second_draft.price}}**

This sponsorship helps people attend the conference that couldn't otherwise attend.
It's great to show your support to the community.

Benefits
~~~~~~~~

* Your sponsor logo will be shown on the stage during all staff presentations as a grant sponsor (opening, closing).
* We will mention your company as a grant sponsor on Twitter from the official Write the Docs account

Writing Day
-----------

Sponsor the Writing Day, where we get together to help improve the documentation of many projects.
This is great for any company that is looking for contributors to their open source projects.

**{{sponsorship.second_draft.price}}**

Inquiries
=========

Please direct all inquiries to our sponsorship team at:

- sponsorship@writethedocs.org

Payment
=======

Invoices must be paid **within 30 days of invoice receipt**, or no later than one (1) week before the conference.

.. _ticket: https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}/
.. _tickets: https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}/


Run of Show
===========
{% if not flagrunofshow %}

The Run of Show will be published closer to the event.

{% else %}

This Run of Show provides more context about the event and answers some common questions you may have.
Please let us know if there is any information missing that would be useful for you.

Sponsorship schedule
--------------------

* **MONDAY**: The conference platform opens at 8am, so we recommend arriving around this time to get the most interaction with attendees. The conference will run until around 5pm.

* **TUESDAY**: The Job Fair will be on Tuesday morning in the Expo area of the online platform. It will take place in existing sponsorship booths. If you do not have a booth, a temporary booth will be set up for the job fair, and then removed during lunch.

See the :doc:`full schedule </conf/{{ shortcode }}/{{ year }}/schedule>` for exact timing details.

Sponsorship platform
--------------------

We will be using `Hopin <https://hopin.to/>`_ as our online conference platform. It has multiple unique spaces for attendees during the conference, and we hope it will allow for a good amount of interaction between attendees and sponsors. The conference platform won't become fully active until the Sunday of the conference.

Sponsorship spaces
------------------

A quick overview of the important spaces in the "venue":

* The *Main stage* is where the talks happen. This is also where Lightning talks will be given.
* The *Sessions area* is where the Writing Day and Unconference will happen.
* The *Expo area* is where the Job Fair will happen. You can chat in text or video directly with attendees.

Sponsorship events
------------------

Job Fair
~~~~~~~~

On Tuesday morning we hold our Job Fair,
which is a wonderful place to connect with our over {{ about.attendees }} attendees.
Many of them are looking for jobs now or will be in the near future,
so it's a great chance to talk more about your company culture and open positions.

**Logistics**: You will be assigned a sponsor booth in the *Expo area* where you can engage with attendees and answer questions.  We recommend that you answer general questions in the main session and then break off into private calls or chats to talk in more depth with specific people.

You can also offer attendees a link to your website or a way to register interest in your job postings.

Writing day
~~~~~~~~~~~

We're still working out the details for the Writing Day, we will update this page when we know the schedule and details.
This is a place where the community gathers to get actual work done.
This generally involved communities and organizations hosting a documentation sprint on some piece of documentation that is open source and needs improvements.

If you want to participate in the Writing Day,
it helps to do a bit of work up front.
The best way to prepare is to have a set of issues that you've already picked as "easy for beginners".
Starting with these issues will make it much easier for people to start,
and feel productive.
Make sure you also have good installation instructions and other helpful beginners content as well.

**Logistics**: We will send a signup sheet to the general attendee list a week before the conference, where you can sign up. You can introduce your project to attendees on Sunday morning during the Writing Day Introduction.

How do I get the most out of my sponsorship?
--------------------------------------------

Come prepared to engage with our community, and to learn just as much as you teach. Engage with our event as attendees as well as sponsors. Send technical staff who can chat with people on the interesting things your company is doing, and get value from the vast amount of insight in the room. We do have some decision makers in the room, but soft sells will work better than hard sales in the environment we strive for.

Who is my primary contact?
--------------------------

Eric Holscher will be your primary contact, but our team is available at sponsorship@writethedocs.org. If you have a time sensitive inquiry, please email the entire team to ensure a timely response.

During the conference itself, we will also have a *help desk* available on the Hopin platform.
You can find staff members there to ask any additional questions you might have.

How do I use my sponsorship tickets?
------------------------------------

You should have received a unique URL with a discount code for your sponsorship tickets. We are happy to send it over again, just ask!

How do I use my job postings?
-----------------------------

You can post your jobs to our `job board <https://jobs.writethedocs.org/>`_.
You will be given a discount code that will let you post them for free,
please ask us for this if you don't have it!
They will be published in our :doc:`Newsletter </newsletter>` every month,
and displayed on our website as well.

What do I need for the job fair?
--------------------------------

The job fair will be a low key event. Generally we recommend having links available to your job descriptions, and ways for attendees to engage with you online after the event.

What does the platform look and feel like?
------------------------------------------

You can see a demo of the platform in this video.
It's currently linked to the expo hall demo,
but it has demos of all the other areas as well:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/JgGVOlbOPUU?start=465" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% endif %}
