:template: {{year}}/generic.html

Tickets
=======

Ticket Information
------------------

{% if flagticketsonsale %}

**Tickets are on sale now!**

We're excited to invite you to our {{ year }} conference in {{ city }}.

{% elif flagsoldout %}

Ticket status
~~~~~~~~~~~~~

**Tickets are sold out!**

{% else %}

**Tickets will be available in {{ date.tickets_live }}.**

{% endif %}

Ticket details
~~~~~~~~~~~~~~

Write the Docs {{ name }} {{ year }} is an in-person conference. Each ticket includes:

* Entry to all conference events and activities
* Drinks and snacks on event days (Sunday-Tuesday)
* Welcome Reception and Social Event with light snacks and drinks
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

All attendees are required to abide by our `Health and Safety Policy <https://www.writethedocs.org/conf/portland/2023/health/>`_,
as well as our `Code of Conduct <https://www.writethedocs.org/code-of-conduct/>`_.

Refund Policy
-------------

Refunds will be offered with a 10% processing fee until 2 weeks before the conference.
Exceptions will be made according to our `Health and Safety Policy <https://www.writethedocs.org/conf/portland/2023/health/>`_.

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

**Corporate Concierge Tickets** *{{tickets.concierge.price}}*
------------------------------------------------------

We offer a corporate concierge service if your company is unable to follow our regular ticket sales process through the website.
We can offer payment by invoice, process purchase orders, bank transfers, fill in supplier registration forms, and offer other support.
Your tickets will be issued after we have received payment.
The minimum purchase is three tickets.

{% if flagticketsonsale %}

* Contact us at `{{email}} <mailto:{{email}}>`_ for this service.

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
