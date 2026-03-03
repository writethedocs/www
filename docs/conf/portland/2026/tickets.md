---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
banner: _static/conf/images/headers/2026/tickets.jpg
---

# Tickets

{% if flagticketsonsale %}

**Tickets are on sale now!**

We're excited to invite you to our {{ year }} conference in {{ city }}.

{% if shirts and flaghasshirts %}

Conference shirts are also available. See the [Official Conference Shirts](#official-conference-shirts) section below for details.

{% endif %}

{% elif flagsoldout %}

**Tickets are sold out!**

{% else %}

**Tickets will be available in {{ date.tickets_live }}.**

{% endif %}

## Ticket Information

Write the Docs {{ name }} {{ year }} is a hybrid conference, which you can attend in person or virtually. Each in-person ticket includes:

- Entry to all conference events and activities
- Snacks and drinks on event days (Sunday-Tuesday)
- Welcome Reception and Social Event with light snacks and drinks
- Wifi throughout the event
- Meeting lots of fantastic people in a spacious, inviting venue

Learn more about the [virtual attendance experience](/conf/{{shortcode}}/{{year}}/virtual/).

All attendees, in person or virtual, are required to abide by our [Code of Conduct](https://www.writethedocs.org/code-of-conduct/).

## Refund Policy

Refunds are offered with a 10% processing fee, up to 2 weeks before the conference.
This includes changing your in-person ticket to virtual, where we will refund the price difference,
minus the processing fee.

If you need to cancel your ticket because of fear of traveling internationally to the United States or getting COVID-19 prior to the conference, we will offer a 100% refund.

## Ticket Types

<div class="ticket">
  <h2>
    <strong>Student/Unemployed</strong>: <em>{{tickets.student.price}}</em> in-person / <em>{{tickets.virtual_student.price}}</em> virtual
  </h2>
  <p>
    Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.
  </p>
  {% if flagticketsonsale %}
  <ul>
    <li>
      <a href="https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}">Buy Student or Unemployed Ticket</a>
    </li>
  </ul>
  {% endif %}
</div>

<div class="ticket">
  <h2>
    <strong>Independent</strong>: <em>{{tickets.independent.price}}</em> in-person / <em>{{tickets.virtual_independent.price}}</em> virtual
  </h2>
  <p>
    Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with fewer than 10 employees.
  </p>
  {% if flagticketsonsale %}
  <ul>
    <li>
      <a href="https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}">Buy Independent Ticket</a>
    </li>
  </ul>
  {% endif %}
</div>

<div class="ticket">
  <h2>
    <strong>Corporate</strong>: <em>{{tickets.corporate.price}}</em> in-person / <em>{{tickets.virtual_corporate.price}}</em> virtual
  </h2>
  <p>
    Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.
  </p>
  {% if flagticketsonsale %}
  <ul>
    <li>
      <a href="https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}">Buy Corporate Ticket</a>
    </li>
  </ul>
  {% endif %}
</div>

{% if shirts and flaghasshirts %}

<div class="ticket">
  <h2>
    <strong>Official Conference Shirts</strong>
  </h2>
  <p>
    You can now visit our Write the Docs {{ name }} {{ year }} Pop-Up Shop and order this year's branded shirt. The campaign will run until <strong>{{ shirts.ends }}</strong>.
  </p>
  <ul>
    <li>
      <a href="{{ shirts.url }}">Buy {{ name }} {{ year }} Shirt</a>
    </li>
  </ul>
</div>
{% endif %}

<div class="ticket">
  <h2>
    <strong>Opportunity Grants</strong>
  </h2>
  <p>
    If you need support in paying for your ticket, travel or other costs, you can apply to our Opportunity Grant program.
  </p>
  {% if grants and grants.ends and grants.url %}
  <p>
    You can apply until <strong>{{ grants.ends }}, 11:59 PM {{ tz }}</strong> on <a href="https://www.writethedocs.org/conf/{{ shortcode }}/{{ year }}/opportunity-grants/">our website</a>.
  </p>
  {% else %}
  <p>
    Grant applications will open soon.
  </p>
  {% endif %}
</div>
