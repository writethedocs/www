# Write the Docs — Marketing & Growth Report

A companion to `IMPROVEMENTS-REPORT.md`, viewed through a marketing lens: how to
grow attendance, strengthen the speaker and sponsor pipelines, and deepen
year-round community engagement. Cross-references to the improvements report use
**S#** (strategic bets) and **T#** (tactical tiers); GitHub issues are linked
where they already capture a thread.

Prepared: 2026-06-04. Scope: conference + community marketing surfaces in
`writethedocs/www` (CFP, tickets, sponsorship, press kit, newsletter, Slack,
social, talk archive).

---

## 1. Framing: the WTD funnel

Write the Docs already has the surfaces of a strong marketing funnel — they're
just not instrumented or connected. Mapping what exists onto a standard funnel
shows where the leaks and opportunities are:

| Stage | Existing surfaces | Biggest opportunity |
| --- | --- | --- |
| **Awareness** | Talk archive, Guide, podcast, social (Twitter/LinkedIn/Bluesky), press kit | Turn the talk archive + Guide into an inbound engine (S2.1, S2.5) |
| **Consideration** | Conference index, schedule, speaker pages, "Convince Your Manager", opportunity grants | ROI/testimonial content; richer social previews |
| **Conversion** | `tickets.rst`, CFP (`cfp.rst`, email templates), sponsorship prospectus | Urgency, automation, and fixing funnel leaks |
| **Retention** | Newsletter, Slack, meetups, welcome-wagon, badge-flair | Year-round engagement between conferences |
| **Advocacy** | Recap posts, speaker promotion, alumni | Make sharing and speaker amplification effortless |

The recurring theme: WTD relies on **manual, one-off marketing effort** (hand-built
social posts, manually linked conferences, ad-hoc recaps). Most of this is
automatable, which is where AI adds leverage.

---

## 2. Conference growth

### 2.1 Plug the funnel leaks (highest ROI, do first)
- **Expired Slack invite** (#2419, #2250, #2238) is a broken top-of-funnel for
  the single largest community-growth surface — people who *want* to join can't.
  Monitor the invite link and alert on expiry (ties to **T1.1** link checking).
- **Missing/!inconsistent social preview images** (#2704 — survey results shipped
  with no OG image) mean low click-through when talks, schedules, and recaps are
  shared. A templated OG-image system (see §5) fixes this site-wide.
- These are small fixes with outsized marketing impact: every share and every
  signup currently leaks value.

### 2.2 Attendee conversion
- **"Convince Your Manager" as a real conversion asset.** Pair each conference's
  page with **testimonials** (long-requested #419) and a one-page ROI summary
  (what attendees take back to their teams). AI can draft from past recap posts
  and talk themes; humans supply real quotes.
- **Urgency & lifecycle automation.** The config already has
  `flagticketsonsale` / `flagsoldout` / `flagspeakersannounced`. Drive automatic
  early-bird countdowns, "tickets selling fast", and a current-conference banner
  on the landing page (**T2.7**, #1680). Add calendar invites / reminders (#1519).
- **Opportunity grants** are a values *and* growth lever — promote them earlier
  and more visibly to widen the top of the attendee funnel.

### 2.3 Speaker pipeline (CFP marketing)
- The CFP machinery exists (`cfp.rst`, `cfp-email-templates.rst`,
  `example-proposal.rst`) but recruitment is manual. Opportunities:
  - **Auto-generated, shareable CFP and "I'm speaking at WTD" social cards**
    (the speaker social-pic work in #2104 is the foundation — extend it to CFP
    promotion and speaker self-promotion).
  - **Diversity outreach**: pair CFP promotion with opportunity grants and
    targeted amplification to broaden the speaker pool.
  - **Proposal helpers**: a checklist / examples page (and AI-assisted feedback)
    lowers the barrier for first-time speakers — directly grows submissions.

### 2.4 Sponsor value & retention (revenue)
The `sponsorship/` section (`index`, `jobs`, `newsletter`, `slack`, `website`)
sells placements, but sponsors buy **audience and outcomes**. Strengthen the
offer:
- **Audience one-pager**: who attends (roles, seniority, geography) — derivable
  from the salary survey demographics + analytics. Makes the prospectus concrete.
- **Post-conference sponsor recap**: impressions, booth/expo engagement, logo
  reach — turns one-time sponsors into renewing ones.
- **Better logo visibility & measurement**: sponsor inclusion should be
  data-driven (#2053, **T2.7**), and the prospectus should state real numbers.
- This is the most direct path to **funding the community's volunteer-run work.**

---

## 3. Community growth & retention (year-round)

The conferences are pulse events; the community has to live between them.
- **Onboarding**: fix the Slack join flow (§2.1), then improve first-run
  experience — Slack etiquette/welcome content (#631), a clear "start here."
- **Belonging mechanics already exist** (welcome-wagon, badge-flair) — extend
  them and surface them in marketing.
- **Meetups ↔ conference cross-promotion**: an accurate, lively meetups map
  (depends on resolving stale-meetup review #1744 and the Meetup API FIXME
  #1067) is both a growth and a retention surface.
- **Newsletter as the retention backbone**: it already runs monthly (94 issues)
  on Mailchimp with basic segmentation (Monthly + NA/EU/AU announcements). The
  win isn't building it — it's *using* it harder: optimize signup placement,
  add speaker/sponsor/organizer segments, run a conference lifecycle sequence,
  and feed the repurposing pipeline (§4.1). Recap posts (e.g. the Portland
  thanks-recap) are good — make them a repeatable template, not a one-off.

---

## 4. Content marketing engine

WTD already operates a genuinely strong content engine — it's just under-promoted
and run entirely on manual editorial effort. Understanding it is key to the whole
strategy.

### 4.1 The existing flywheel: Slack → Newsletter → Topics
This is the crown jewel and it already works:
- **Slack** (ephemeral) is distilled monthly into the **Newsletter** — **94
  issues since 2017**, each a curated digest where the best community discussions
  become standalone, evergreen articles (e.g. "AI and the need for product
  knowledge", "Capitalizing Feature Names").
- Every article closes with **"See more WTD resources about [topic]"**, linking
  into the **Topics page** (`topics.rst`, ~930 lines) — a hand-maintained
  **content graph** that cross-references newsletter articles (📰) and
  conference talks (🎥) by theme. This is a real, vendor-neutral knowledge base
  and an internal-linking/SEO asset most communities would envy.
- Distributed via **Mailchimp** with segmentation already in place (Monthly
  Newsletter + NA/EU/AU conference announcements).

The opportunity is **not to build this — it's to amplify it and cut the manual
burden:**
- **Repurpose every newsletter article** into social cards, threads, and quote
  graphics (one issue → ~5 social posts). The content is already written; it's
  just not being distributed beyond email.
- **Automate Topics-page upkeep.** Today it's hand-curated, so talks lag behind
  (#1332) and discoverability is limited (#1298, #952). AI tagging (S2.2) keeps
  the graph current and lets it power on-site search and "related content."
- **Surface the archive.** 94 issues of evergreen advice are buried in the blog;
  promote "from the archive" content and make Topics a featured destination.

### 4.2 Amplify with the talk archive and Guide
- **Talk archive as evergreen inbound (S2.1).** Transcribed, summarized, tagged
  talks are SEO gold and feed the same repurposing pipeline as the newsletter —
  and auto-tagging finally keeps the Topics graph complete.
- **Guide as authority/inbound (S2.2, S2.5).** The Guide already ranks; role-based
  paths plus clean, structured, citable content (GEO best-practice — not the
  unproven `llms.txt`) make WTD the source AI answers cite on documentation — the
  best long-term brand marketing there is.
- **Unified repurposing pipeline**: one source (talk *or* newsletter article) →
  Topics entry + quote cards + social thread + podcast cross-promo. AI can draft
  the whole chain; editors approve.

---

## 5. Social & brand consistency

- **Templated OG/social-image system.** WTD already generates `social_description`
  (2026) and speaker social pics (#2104). Generalize this into a consistent
  social-card system for every page type (talk, schedule, recap, CFP, sponsor)
  so nothing ships without a preview (closes the #2704 class of problem).
- **Cross-platform posting.** Bluesky was recently added alongside
  Twitter/LinkedIn; a "talk of the week" / speaker-spotlight series with
  auto-generated cards keeps channels active with low human effort.
- **Brand freshness.** Keep press kits current (#1078) and visual identity
  consistent across per-year conference templates (de-duplication, **T3**).

---

## 6. Measurement (so marketing can improve)

Marketing without measurement is guesswork. WTD uses privacy-first
SimpleAnalytics (good), but there's no shared funnel view.
- Define a small KPI set: signups, ticket conversions, CFP submissions, sponsor
  renewals, newsletter growth, social CTR.
- Adopt **UTM conventions** for campaigns so the existing analytics can attribute
  traffic to channels.
- A lightweight per-conference dashboard (or even a recap doc) closes the loop
  and informs the next cycle.

---

## 7. Prioritized marketing backlog

Ordered by value × AI-implementability, consistent with the improvements report.

| # | Initiative | Effort | AI role | Refs |
| --- | --- | --- | --- | --- |
| 1 | Fix Slack-invite + social-image funnel leaks | Low | AI owns | #2419, #2704, T1.1 |
| 2 | Templated OG/social-card system for all page types | Med | AI owns | #2104, #2704, T1.4 |
| 3 | Conference lifecycle automation (countdown, banner, reminders) | Med | AI owns | #1680, #1519, T2.7 |
| 4 | Repurpose newsletter archive → social/topics (amplify existing engine) | Med | AI owns | §4.1, #1332, #1298 |
| 5 | Auto-maintain Topics content graph (tagging, related content) | Med | AI owns | S2.2, #952, #1332 |
| 6 | Talk-archive content engine (transcripts → social/newsletter/topics) | High | AI owns | S2.1, #1976 |
| 7 | "Convince Your Manager" + testimonials + ROI asset | Med | AI drafts | #419 |
| 8 | CFP promotion kit + speaker self-promo cards | Med | AI owns | #2104 |
| 9 | Sponsor audience one-pager + post-conf recap | Med | AI drafts | sponsorship/, S2.4 |
| 10 | Newsletter lifecycle templates + added segments | Med | AI drafts | — |
| 11 | UTM + KPI dashboard for measurement | Low | AI owns | — |
| 12 | Community onboarding (Slack welcome, etiquette) | Low | AI drafts | #631 |

### Recommended first moves
- **Items 1–2** are pure marketing-leak fixes with sitewide payoff and clean AI
  ownership — pair them with the Tier 1 bundle in the improvements report.
- **Items 4–6** are the flywheel: they amplify WTD's *existing* Slack →
  Newsletter → Topics engine (94 issues of evergreen content already written) and
  the talk archive, compounding across awareness, retention, and advocacy. Start
  with item 4 — it's the lowest-effort, highest-leverage because the content
  already exists and only needs distribution.
- Revenue-sensitive items (**9**) and editorial items (**7, 10, 12**) should ship
  as AI-drafted PRs for human/marketing review, not autonomous merges.

---

## 8. Honest caveats

- WTD is volunteer-run; the winning plays are those where **AI does the
  production work and humans only make the calls** (cards, transcripts,
  automation) — not initiatives that commit volunteers to ongoing manual
  campaigns.
- Anything touching sponsor commitments, real testimonials, or community voice
  needs human ownership; AI accelerates the draft, it doesn't sign off.
- Measurement must stay within WTD's privacy-first stance — UTMs and aggregate
  KPIs, not invasive tracking.
