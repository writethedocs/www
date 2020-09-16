:template: {{year}}/generic.html

Tickets
=======

Ticket Information
------------------

{% if flagticketsonsale %}

**Tickets are on sale now!**

{% elif flagsoldout %}

Ticket status
~~~~~~~~~~~~~

**Tickets are sold out!**

We have a `waiting list <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`_ where you can register in case of cancellations, but we usually don't have a high rate of cancellations so please do not book travel unless you have a ticket.

{% else %}

**Tickets will be available in {{ date.tickets_live }}.**

{% endif %}

Ticket details
~~~~~~~~~~~~~~

Write the Docs {{ name }} {{ year }} is a virtual conference. Each ticket includes:

* Live streaming of all talks
* Q&A with speakers after each talk (may not be available for all speakers)
* Access to the conference chat with all other attendees, speakers and sponsors
* Access to the writing day
* The virtual job fair

Refund Policy
-------------

Refunds will be offered with a 10% processing fee until 2 weeks before the conference.
Refunds after this date are not possible.

Ticket Types
------------


{% if shirts.url %}

.. class:: ticket

**Official Conference Shirts**
------------------------------------

You can now visit our Write the Docs {{ name }} {{ year }} Pop-Up Shop and order this year’s branded shirt. The campaign will run until **{{ shirts.ends }}**.

* `Buy {{ name }} {{ year }} Shirt <{{ shirts.url }}>`_

{% endif %}

.. class:: ticket

**Corporate Tickets** *{{tickets.corporate.price}}*
--------------------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

* `Buy Corporate Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets** *{{tickets.independent.price}}*
--------------------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with fewer than 10 employees.

{% if flagticketsonsale %}

* `Buy Independent Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Student or Unemployed Tickets** *{{tickets.student.price}}*
--------------------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

* `Buy Student or Unemployed Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**None of the above**
---------------------

If you can't afford these prices and still wish to attend, you can apply for our grant program.
{% if grants.ends and grants.url %}
You can apply until **{{ grants.ends }}, Midnight {{ tz }}** on `our website <https://www.writethedocs.org/conf/{{ shortcode }}/{{ year }}/opportunity-grants/>`_.
{% else %}
Grant applications will open soon.
{% endif %}
