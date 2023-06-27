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
* Drinks and snacks on event days (Thursday-Friday)
* Social Event with light snacks and drinks
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

Refund Policy
-------------

Refunds will be offered with a 10% processing fee until 2 weeks before the conference.
Refunds after this date are not possible.

Ticket Types
------------

.. class:: ticket

**Student or Unemployed Tickets** *{{tickets.student.price}}*
--------------------------------------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

* `Buy Student or Unemployed Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets** *{{tickets.independent.price}}*
-------------------------------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with fewer than 10 employees.

{% if flagticketsonsale %}

* `Buy Independent Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Corporate Tickets** *{{tickets.corporate.price}}*
---------------------------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

* `Buy Corporate Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Opportunity Grants**
-----------------------

If you need support in paying for your ticket, travel or other costs,
you can apply to our Opportunity Grant program.

{% if grants and grants.ends and grants.url %}
You can apply until **{{ grants.ends }}, Midnight {{ tz }}** on `our website <https://www.writethedocs.org/conf/{{ shortcode }}/{{ year }}/opportunity-grants/>`_.
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
