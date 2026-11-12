---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
banner: _static/conf/images/photos/auditorium-day-1-55249270408.jpg
---

# Tickets

{% if flagticketsonsale %}

Tickets are on sale now! We're excited to invite you to our {{ year }} conference in {{ city }}, on {{ date.main }}.

```{button-link} https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}
:year: {{ year }}
Buy your ticket
```

{% if shirts and flaghasshirts %}

Conference shirts are also available. See the [Official Conference Shirts](#official-conference-shirts) section below for details.

{% endif %}

{% elif flagsoldout %}

Tickets are sold out! Thank you to everyone who is joining us for our {{ year }} conference in {{ city }}, on {{ date.main }}.

{% if tickets.waiting_list %}

If someone cancels, we release their ticket to the waiting list:

```{button-link} {{ tickets.waiting_list }}
:year: {{ year }}
Join the waiting list
```

{% endif %}

{% else %}

**Tickets are not on sale yet.** They will be available in {{ date.tickets_live }}, for our {{ year }} conference in {{ city }} on {{ date.main }}.

```{button-link} /conf/{{shortcode}}/{{year}}/mailing-list/
:year: {{ year }}
Hear about tickets on the mailing list
```

{% endif %}

Write the Docs {{ name }} {{ year }} is a hybrid conference, which you can attend in person or virtually. Each in-person ticket includes:

- Entry to all conference events and activities
- Snacks and drinks on event days (Sunday-Tuesday)
- Welcome Reception and Social Event with light snacks and drinks
- Wifi throughout the event
- Meeting lots of fantastic people in a spacious, inviting venue

Virtual tickets include:

- Watching all talks and Q&A sessions on the main stage live
- Submitting live Q&A questions for speakers
- A virtual hallway track and chat to network with other remote attendees

Learn more about the [virtual attendance experience](/conf/{{shortcode}}/{{year}}/virtual/).

All attendees, in person or virtual, are required to abide by our [Code of Conduct](https://www.writethedocs.org/code-of-conduct/).

## Ticket Types

<div class="ticket">
  <h2>
    <strong>Student/Unemployed</strong>{% if flagticketsonsale or flagsoldout %}: <em>{{tickets.student.price}}</em> in-person / <em>{{tickets.virtual_student.price}}</em> virtual{% endif %}
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
    <strong>Independent</strong>{% if flagticketsonsale or flagsoldout %}: <em>{{tickets.independent.price}}</em> in-person / <em>{{tickets.virtual_independent.price}}</em> virtual{% endif %}
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
    <strong>Corporate</strong>{% if flagticketsonsale or flagsoldout %}: <em>{{tickets.corporate.price}}</em> in-person / <em>{{tickets.virtual_corporate.price}}</em> virtual{% endif %}
  </h2>
  <p>
    Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.
    If your company needs to pay by invoice or purchase order, see <a href="/conf/{{shortcode}}/{{year}}/convince-your-manager/#paying-by-invoice-or-purchase-order">how to buy tickets as a company</a>.
  </p>
  <p>
    We provide a certificate of attendance on request after the conference. Email us at <a href="mailto:{{email}}">{{email}}</a> and we will send you one.
  </p>
  {% if flagticketsonsale %}
  <ul>
    <li>
      <a href="https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}">Buy Corporate Ticket</a>
    </li>
  </ul>
  {% endif %}
</div>

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

{% if shirts and flaghasshirts %}

<div class="ticket" id="official-conference-shirts">
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

## Refund Policy

Refunds are offered with a 10% processing fee, up to 2 weeks before the conference.
This includes changing your in-person ticket to virtual, where we will refund the price difference,
minus the processing fee.

If you need to cancel your ticket for health or visa reasons, we will offer a 100% refund.

You can also transfer your ticket to someone else at any time. Email us at [{{email}}](mailto:{{email}}) with their name and email address.
