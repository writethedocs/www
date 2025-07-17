:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
:banner: _static/conf/images/headers/2025/tickets.jpg

Tickets
=======

.. class:: ticket

**Looking for tickets for Write the Docs Berlin?**
--------------------------------------------------

A newsletter for the Berlin 2025 conference accidentally included a link to
this page.
You can `order your Berlin conference tickets here </conf/berlin/2025/tickets>`_.

{# commented out as interfered with banner
{% if flagticketsonsale %}

**Tickets are on sale now!**

We're excited to invite you to our {{ year }} conference in {{ city }}.

{% if shirts and flaghasshirts %}
Conference shirts are also available. See the `Official Conference Shirts`_ section below for details.

{% endif %}


{% elif flagsoldout %}

**Tickets are sold out!**

{% else %}

**Tickets will be available in {{ date.tickets_live }}.**

{% endif %}
#}

Ticket Information
------------------

Write the Docs {{ name }} {{ year }} is a hybrid conference, which you can attend in person or virtually. Each in-person ticket includes:

* Entry to all conference events and activities
* Snacks and drinks on event days (Sunday-Tuesday)
* Welcome Reception and Social Event with light snacks and drinks
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

Learn more about the `virtual attendance experience </conf/portland/2025/virtual/>`_.

All attendees, in person or virtual, are required to abide by our `Code of Conduct <https://www.writethedocs.org/code-of-conduct/>`_.

Refund Policy
-------------

Refunds are offered with a 10% processing fee, up to 2 weeks before the conference.

If you need to cancel your ticket because of fear of traveling internationally to the United States or getting COVID-19 prior to the conference, we will offer a 100% refund. 

Ticket Types
------------

.. class:: ticket

**Student or Unemployed Tickets** *{{tickets.student.price}}*
--------------------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

* `Buy Student or Unemployed Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets** *{{tickets.independent.price}}*
--------------------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with fewer than 10 employees.

{% if flagticketsonsale %}

* `Buy Independent Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Corporate Tickets** *{{tickets.corporate.price}}*
--------------------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

* `Buy Corporate Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Virtual Tickets** *{{tickets.virtual.price}}*
--------------------------------------------

Join us virtually for the main conference days (May 5-6). Learn more about the `virtual attendance experience </conf/portland/2025/virtual/>`_.

{% if flagticketsonsale %}

* `Buy Virtual Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Opportunity Grants**
----------------------

If you need support in paying for your ticket, travel or other costs,
you can apply to our Opportunity Grant program.

{% if grants and grants.ends and grants.url %}
You can apply until **{{ grants.ends }}, 11:59 PM {{ tz }}** on `our website <https://www.writethedocs.org/conf/{{ shortcode }}/{{ year }}/opportunity-grants/>`_.
{% else %}
Grant applications will open soon.
{% endif %}

{% if shirts and flaghasshirts %}

.. class:: ticket

**Official Conference Shirts**
------------------------------------

You can now visit our Write the Docs {{ name }} {{ year }} Pop-Up Shop and order this year’s branded shirt. The campaign will run until **{{ shirts.ends }}**.

* `Buy {{ name }} {{ year }} Shirt <{{ shirts.url }}>`_

{% endif %}

.. class:: ticket

**Corporate Concierge Tickets** 
------------------------------------------------------

We offer a corporate concierge service if your company is unable to follow our regular ticket sales process through the website.
We can offer payment by invoice, process purchase orders, bank transfers, fill in supplier registration forms, and offer other support.
Your tickets will be issued after we have received payment.
The minimum purchase is three tickets at $750 per ticket.

{% if flagticketsonsale %}

* Contact us at `{{email}} <mailto:{{email}}>`_ for this service.

{% endif %}
