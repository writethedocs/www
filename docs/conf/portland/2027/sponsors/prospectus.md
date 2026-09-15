---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
banner: _static/conf/images/headers/2026/prospectus.jpg
---

# Sponsorship Prospectus

## Introduction

Welcome to the Write the Docs {{ city }} {{ year }} sponsorship prospectus. We're excited to work with the organizations in our community to build the best documentation conference in {{ year }}.

Write the Docs {{ city }} is a **three day conference** held on {{ date.short }} focusing on documentation systems, tech writing theory, and information delivery. We expect {{ about.attendees }} attendees at the conference this year.

<ul class="key-facts">
  <li><strong>{{ about.attendees }}</strong><span>attendees</span></li>
  <li><strong>{{ about.audience[0].percent }}%</strong><span>{{ about.audience[0].label }}</span></li>
  <li><strong>{{ about.ticket_mix[0].percent }}%</strong><span>{{ about.ticket_mix[0].label }}</span></li>
</ul>

{% if flagrunofshow %}

If you're an existing sponsor looking for next steps, check out our [Sponsorship Information page](/conf/{{shortcode}}/{{year}}/sponsors/information/).

{% endif %}

## Sponsorship Packages

All packages can be customized, so let us know what you need!

### Compare packages

<table class="benefit-matrix">
<thead>
  <tr>
    <th></th>
    <th scope="col"><a href="#package-keystone">Keystone</a><small>{{sponsorship.keystone.price}}</small></th>
    <th scope="col"><a href="#package-patron">Patron</a><small>{{sponsorship.patron.price}}</small></th>
    <th scope="col"><a href="#package-publisher">Publisher</a><small>{{sponsorship.publisher.price}}</small></th>
    <th scope="col"><a href="#package-supporter">Supporter</a><small>{{sponsorship.second_draft.price}}</small></th>
  </tr>
</thead>
<tbody>
  <tr>
    <th scope="row">Conference tickets</th>
    <td>{{sponsorship.keystone.tickets}}</td>
    <td>{{sponsorship.patron.tickets}}</td>
    <td>{{sponsorship.publisher.tickets}}</td>
    <td>{{sponsorship.second_draft.tickets}}</td>
  </tr>
  <tr>
    <th scope="row">Listing on the conference website</th>
    <td>250 words</td>
    <td>150 words</td>
    <td>100 words</td>
    <td>Logo</td>
  </tr>
  <tr>
    <th scope="row">Name in conference emails</th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
  </tr>
  <tr>
    <th scope="row">Swag on the conference swag table</th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
  </tr>
  <tr>
    <th scope="row">Main stage introduction</th>
    <td>60 seconds</td>
    <td>30 seconds</td>
    <td>Thank-you slide</td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Reserved Unconference session or Writing Day project</th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Logo on intermission slides and talk videos</th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Sponsor booth, both conference days</th>
    <td>Premium booth</td>
    <td>Booth</td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Dedicated social media post</th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Sponsorship of a primary conference event</th>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Large logo on print, slides, and videos</th>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
  </tr>
  <tr>
    <th scope="row">Email promotion to our conference list</th>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
  </tr>
</tbody>
<tbody>
  <tr class="group"><th scope="rowgroup" colspan="5">Add-ons</th></tr>
  <tr>
    <th scope="row">Additional tickets<small>{{sponsorship.extra_ticket.price}} each</small></th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
  </tr>
  <tr>
    <th scope="row"><a href="#addon-lightning-talks">Lightning Talks sponsorship</a><small>{{sponsorship.lightning_talks.price}}, limit 2</small></th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
  </tr>
  <tr>
    <th scope="row"><a href="#addon-opportunity-grants">Opportunity Grants sponsorship</a><small>{{sponsorship.opportunity_grants.price}}, limit 2</small></th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
  </tr>
  <tr>
    <th scope="row"><a href="/conf/{{shortcode}}/{{year}}/sponsors/activations/">Activations</a><small>Priced individually</small></th>
    <td><span class="yes">✓</span></td>
    <td><span class="yes">✓</span></td>
    <td><span class="no">–</span></td>
    <td><span class="no">–</span></td>
  </tr>
</tbody>
</table>

<div class="announcement" style="background-color:white;">
    <div class="uk-container">
    <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="mailto:sponsorship@writethedocs.org?subject=Sponsoring%20Write%20the%20Docs%20{{city}}%20{{year}}">Email us about sponsoring</a>
    </div>
</div>

<details class="package" id="package-keystone">
<summary><span class="name">Keystone</span><span class="price">{{sponsorship.keystone.price}}</span><span class="limit">Limit 3</span></summary>

The **Keystone** sponsorship highlights you as the primary sponsor of the conference. You get all in-person benefits, and the best placement for all physical spaces.

Keystone can be customized to fit your goals. Booth sponsors can add activations such as a sponsored headshot booth, an attendee lounge, and catering opportunities like the welcome reception or a branded coffee break. See our [sponsorship activations](/conf/{{shortcode}}/{{year}}/sponsors/activations/) page for the full list.

<h4>Benefits</h4>

- {{sponsorship.keystone.tickets}} tickets, with additional available to purchase at a discounted rate of {{sponsorship.extra_ticket.price}}/ticket.
- Most visible **sponsorship booth** for the entire conference (Monday & Tuesday). Monitor included in booth. Booths placed in order of purchase.
- Sponsorship of a primary Write the Docs conference event (Unconference, Writing Day, or Social Event).
- **60 second introduction** on the main stage introducing your company.
- Large logo on print material.
- Large logo included in intermission slides and on talk videos.
- Logo and long description (250 words) on the conference website.
- Name in all conference email promotion.
- Dedicated social media post.
- One email promotion to our conference email list. Includes logo and 2 paragraphs of copy.
- Display promotional “Swag” items on the conference swag table (provided by sponsor).

</details>

<details class="package" id="package-patron">
<summary><span class="name">Patron</span><span class="price">{{sponsorship.patron.price}}</span></summary>

The **Patron** package is great for a larger company to get in front of our attendees. It gives you a dedicated booth for the entire length of the conference.

Patron sponsors can also add [activations](/conf/{{shortcode}}/{{year}}/sponsors/activations/) such as a sponsored headshot booth, an attendee lounge, or catering at a social event.

<h4>Benefits</h4>

- {{sponsorship.patron.tickets}} tickets, with additional available to purchase at a discounted rate of {{sponsorship.extra_ticket.price}}/ticket.
- A **sponsorship booth** for the entire conference (Monday & Tuesday). Monitor rental available for {{sponsorship.monitor_rental.price}}.
- **30 second introduction** on the main stage introducing your company.
- Dedicated social media post.
- Logo included in intermission slides and on talk videos.
- Logo and description (150 words) on the conference website.
- Name in conference email promotion.
- Display promotional “Swag” items on the conference swag table (provided by sponsor).

</details>

<details class="package" id="package-publisher">
<summary><span class="name">Publisher</span><span class="price">{{sponsorship.publisher.price}}</span></summary>

The **Publisher** package is for companies that want to engage with attendees without staffing a booth. You get a place in the program and visibility across the conference.

<h4>Benefits</h4>

- {{sponsorship.publisher.tickets}} tickets, with additional available to purchase at a discounted rate of {{sponsorship.extra_ticket.price}}/ticket.
- A **reserved Unconference session or Writing Day project**, listed on the published schedule under your company's name. Lead a discussion, run a workshop, or get attendees contributing to your docs.
- Logo on the sponsor thank-you slide during the main stage sponsor introductions.
- Logo included in intermission slides and on talk videos.
- Logo and description (100 words) on the conference website.
- Name included in all conference emails to attendees.
- Display promotional "Swag" items on the conference swag table (provided by sponsor).

</details>

<details class="package" id="package-supporter">
<summary><span class="name">Supporter</span><span class="price">{{sponsorship.second_draft.price}}</span></summary>

The **Supporter** package gives you visibility on the conference website and in communications. It's a great package for a startup or small company.

<h4>Benefits</h4>

- {{sponsorship.second_draft.tickets}} tickets, with additional available to purchase at a discounted rate of {{sponsorship.extra_ticket.price}}/ticket.
- Logo on the conference website.
- Name included in all conference emails to attendees.
- Display promotional (“Swag”) items on the conference swag table (provided by sponsor).

</details>

## Other Sponsorship Opportunities

The following add-ons increase your visibility at the event. Lightning Talks sponsorship requires a Supporter package or higher; Opportunity Grants can be sponsored independently.

<details class="package" id="addon-lightning-talks">
<summary><span class="name">Lightning Talks</span><span class="price">{{sponsorship.lightning_talks.price}}</span><span class="limit">Limit 2</span></summary>

Sponsor one day of Lightning Talks, where attendees have 5 minutes to share something they are excited about working on. You will have 60 seconds at the start to introduce your company. Requires a Supporter package or higher.

<h4>Benefits</h4>

- **60 second introduction** on the main stage introducing your company.
- Logo will be shown on the stage during all staff presentations as a Lightning Talk sponsor.
- Logo on the conference website.
- Name included in welcome announcement in email newsletters and social media.

</details>

<details class="package" id="addon-opportunity-grants">
<summary><span class="name">Opportunity Grants</span><span class="price">{{sponsorship.opportunity_grants.price}}</span><span class="limit">Limit 2</span></summary>

Provide additional funding for our Opportunity Grant program, which supports equity and accessibility and provides funding for low-income, marginalized people to attend the conference. These individuals would otherwise not be able to attend.

<h4>Benefits</h4>

- Logo will be shown onstage during opening and closing staff presentations as a grant sponsor.
- Logo on the conference website.
- Name included in welcome announcement in email newsletters and social media.
- Display promotional "Swag" items on the conference swag table (provided by sponsor).

</details>

## Demographics

Our audience is primarily from companies in the software industry.

Each conference is attended by:

<div class="share-bar">
{% for share in about.audience %}  <span class="seg seg-{{ loop.index }}" style="width: {{ share.percent }}%;" title="{{ share.label }} ({{ share.percent }}%)"></span>
{% endfor %}</div>
<ul class="share-legend">
{% for share in about.audience %}  <li><i class="seg-{{ loop.index }}"></i>{{ share.label }} <b>{{ share.percent }}%</b></li>
{% endfor %}</ul>

Each conference we sell:

<div class="share-bar">
{% for share in about.ticket_mix %}  <span class="seg seg-{{ loop.index }}" style="width: {{ share.percent }}%;" title="{{ share.label }} ({{ share.percent }}%)"></span>
{% endfor %}</div>
<ul class="share-legend">
{% for share in about.ticket_mix %}  <li><i class="seg-{{ loop.index }}"></i>{{ share.label }} <b>{{ share.percent }}%</b></li>
{% endfor %}</ul>

## Why Sponsor

By supporting a Write the Docs event, your company will gain visibility and credibility with front-line documentarians, and valuable insights that will help you get the most out of your own documentation efforts. If you're hiring for docs positions, Write the Docs is also an excellent opportunity to meet top-notch talent.

We work hard to keep ticket prices affordable for a broad range of attendees. Your sponsorship makes it possible for all sorts of documentarians to attend our events, whether they're a freelancer, a student or out of work. Becoming a sponsor demonstrates your commitment to and support of good documentation, and the people who build it.

## No attendee information is shared with sponsors

**We do not share any attendee information with sponsors.** As part of our sponsorships, we allow sponsors to send messages to attendees, but we do not share any personal information about attendees.

## Inquiries

For more information on getting the most out of your sponsorship, see our [Sponsorship Information page](/conf/{{shortcode}}/{{year}}/sponsors/information/).

Please direct all inquiries to our sponsorship team at <sponsorship@writethedocs.org>.

<div class="announcement" style="background-color:white;">
    <div class="uk-container">
    <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="mailto:sponsorship@writethedocs.org?subject=Sponsoring%20Write%20the%20Docs%20{{city}}%20{{year}}">Email our sponsorship team</a>
    </div>
</div>

```{raw} html
<script>
// Links in the comparison table point at these collapsible blocks; open the one
// a visitor lands on, so the link shows the detail rather than a closed summary.
(function () {
  function openTarget() {
    var el = document.getElementById(window.location.hash.slice(1));
    if (el && el.tagName === 'DETAILS' && !el.open) {
      el.open = true;
      el.scrollIntoView();
    }
  }
  window.addEventListener('hashchange', openTarget);
  openTarget();
})();
</script>
```
