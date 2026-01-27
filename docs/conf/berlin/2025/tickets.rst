:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
:banner: _static/conf/images/headers/2025/tickets.jpg

Tickets
=======

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

Ticket Information
------------------

Write the Docs {{ name }} {{ year }} is a hybrid conference, which you can attend in person or virtually. Each in-person ticket includes:

* Entry to all conference events and activities
* Snacks and drinks on conference days
* Social Event with light snacks and drinks
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

All attendees, in person or virtual, are required to abide by our `Code of Conduct <https://www.writethedocs.org/code-of-conduct/>`_.

Refund Policy
-------------

Refunds are offered with a 10% processing fee, up to 2 weeks before the conference.
This includes changing your in-person ticket to virtual, where we will refund the price difference,
minus the processing fee.

Virtual or in-person
--------------------
Each ticket is available as a virtual or in-person form.
Learn more about the `virtual attendance experience </conf/{{shortcode}}/{{year}}/virtual/>`_.


Ticket Types
------------

.. class:: ticket

**Student/Unemployed Tickets**: *{{tickets.student.price}}* in-person / *{{tickets.virtual_student.price}}* virtual
---------------------------------------------------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

* `Buy Student or Unemployed Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets**: *{{tickets.independent.price}}* in-person / *{{tickets.virtual_independent.price}}* virtual
--------------------------------------------------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with fewer than 10 employees.

{% if flagticketsonsale %}

* `Buy Independent Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Corporate Tickets**: *{{tickets.corporate.price}}* in-person / *{{tickets.virtual_corporate.price}}* virtual
--------------------------------------------------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

* `Buy Corporate Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

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
The minimum purchase is three tickets at *{{tickets.concierge.price}}* per ticket.

{% if flagticketsonsale %}

* Contact us at `{{email}} <mailto:{{email}}>`_ for this service.

{% endif %}
