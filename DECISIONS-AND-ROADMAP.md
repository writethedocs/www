# Write the Docs — Decision Memos & Roadmap

Bridges the strategy (`BOARD-OFFSITE-BRIEF.md`) to action. **Part 1** works each of
the six board decisions into a short memo with options, trade-offs, and a
*proposed* default. **Part 2** sequences the work into a phased roadmap.

The recommendations are **starting positions for debate, not predetermined
outcomes** — the board decides. They exist so the offsite can react to a concrete
proposal rather than start from a blank page.

Prepared: 2026-06-04. Evidence is sourced in `EXTERNAL-CONTEXT.md`.

---

## Part 1 — Decision memos

### Decision 1 — Focus: which two pillars this year?
**Options:** any two of A (lead the AI transition), B (content infrastructure),
C (sustainability), D (access/reach).
**Trade-offs:** A and B are mission-and-moment aligned and highly AI-leverageable
(low volunteer cost). C is an enabler — it *creates* capacity but pays off later.
D is values-aligned and good for growth but needs human/organizer effort.
**Proposed default: B + A.** B is the lowest-regret, compounding investment (it
makes the existing canon work harder and is mostly automatable); A rides the
moment and is on-mission. Fund **C as a continuous background thread** (automation
reduces load as a by-product of B), and stage D once capacity exists.
**Reversible?** Yes — focus can be re-set next cycle; nothing here burns bridges.

### Decision 2 — AI posture and content policy
**Options:** (a) avoid AI internally; (b) use AI freely; (c) use AI with
disclosure + human sign-off.
**Evidence:** publisher/newsroom norm is converging on — assistive AI needs no
disclosure, **generative AI must be disclosed and human-reviewed, and AI does not
replace staff/voice**. Transparency protects trust.
**Proposed default: (c), written down.** Adopt a short public policy: AI may
assist production (drafting, tagging, summarizing, social); **a human edits and
signs off on anything published; community voice stays human; disclose AI
assistance** (e.g. a footer note, as WTD already does on these very documents).
This both relieves volunteer load and models good practice for a community whose
members face the same question.
**Reversible?** The policy is easy to tighten or loosen; getting *a* stance out
early is the win.

### Decision 3 — Editorial ambition beyond the newsletter
**Options:** (a) status quo (monthly newsletter only); (b) **curated** community
publication (editorial review, style guide, themes); (c) open contributor
platform (anyone publishes).
**Evidence:** curated models (freeCodeCamp, CSS-Tricks, Smashing) yield consistent
quality and build a "canon"; open platforms (dev.to) get volume but variable
quality and higher moderation load. WTD already runs a curated engine
(newsletter + Topics) — option (b) is an *extension*, not a new thing.
**Proposed default: (b), incrementally.** Grow the existing engine into a light
curated publication — invite community contributions under editorial review,
reuse the newsletter/Topics infrastructure, and let AI handle production drudgery.
Avoid (c): an open free-for-all adds moderation burden and brand risk that a
volunteer org can't absorb.
**Reversible?** Start small (a few curated pieces); scale only if it sustains.

### Decision 4 — Funding model
**Options:** (a) status quo (sponsorship + tickets); (b) add a supporter/
membership tier; (c) diversify into grants/partnerships; (d) some mix.
**Evidence:** diversified portfolios and **tiered membership** improve community
sustainability; **engaged communities raise ~60% more**; fiscal hosts (e.g. Open
Source Collective) provide infrastructure without building it in-house.
**Proposed default: pilot (b) + pursue (c) opportunistically.** Test a low-effort
**supporter tier** (recognition, not gated content — stays true to the open
ethos) and keep strengthening sponsor value (the marketing report's sponsor
one-pager + recap). Goal: reduce concentration risk and, ideally, fund **one
part-time coordinator** — the single highest-leverage capacity unlock.
**Reversible?** A pilot tier can be wound down; no structural lock-in.

### Decision 5 — Internationalization
**Options:** (a) decline clearly; (b) **enable** community-led translation/locales
without owning it; (c) invest in official translations.
**Context:** the most persistently requested, repeatedly deferred item (#1155, 33+
comments), now amplified by global expansion (Kenya). Option (c) is a large,
ongoing human commitment a volunteer org struggles to sustain.
**Proposed default: (b).** Provide a clear, supported path for community-led
locale efforts (tooling, guidelines, a home on the site) without WTD committing
to maintain translations. Honors demand and global growth while matching
capacity. Decide explicitly either way — silence is its own (poor) answer.
**Reversible?** Yes; can escalate to (c) if a locale community proves durable.

### Decision 6 — Shared success scorecard
**Options:** (a) no formal metrics; (b) a small shared scorecard.
**Proposed default: (b).** Agree ~6 metrics — Slack/newsletter signups,
conference attendance, CFP submissions, sponsor renewals, newsletter growth,
social/citation reach — with a privacy-first stance (UTMs + aggregates, no
invasive tracking). Review at a 12-month checkpoint. Without this, future
decisions stay anecdotal.
**Reversible?** Trivially adjustable; the discipline is the point.

---

## Part 2 — Roadmap

A phased view. The **"first 90 days" set is low-regret regardless of which pillars
win** — it's cheap, mostly automatable, and useful under any strategy. Later
phases assume the proposed B+A focus; swap accordingly if the board chooses
differently.

### Now (0–90 days) — low-regret foundations
*Mostly AI-implementable with human sign-off.*
- **Fix funnel leaks:** monitor the Slack invite + add external link checking;
  templated OG/social images so nothing ships without a preview.
  *(Marketing §2.1; Improvements T1.)*
- **Accessibility/SEO basics:** enforce alt text, add site-wide social metadata,
  fix the 404-page links.
  *(Improvements T1.2–T1.4, #2033.)*
- **Publish the AI-assisted-content policy** (Decision 2) — one page, models the
  practice.
- **Stand up the scorecard** (Decision 6) — UTM conventions + a simple dashboard.
- **Prototype the flagship (Pillar B):** transcribe/summarize/tag a handful of
  talks to prove the talk-archive pattern before scaling.

### Next (3–9 months) — build the content infrastructure (Pillar B) + AI voice (Pillar A)
- **Talk archive at scale:** roll transcription/tagging across the back catalog;
  make it searchable; auto-maintain the Topics graph. *(S2.1, S2.2.)*
- **Repurposing pipeline:** turn the 94-issue newsletter archive + new talks into
  social/threads/quote cards — distribution for content that already exists.
  *(Marketing §4.1.)*
- **GEO/citability pass:** structured, self-contained, schema-marked content so
  WTD becomes a cited source. *(S2.5 — no `llms.txt` bet.)*
- **A WTD point of view on AI + docs (Pillar A):** a standing content theme and
  conference programming; pilot the curated publication (Decision 3).

### Later (9–18 months) — sustainability and reach (Pillars C, D)
- **Capacity:** if funding allows, the part-time coordinator (Decision 4); deepen
  automation of the manual marketing/editorial chores.
- **Funding pilot:** launch and evaluate the supporter tier; ship the sponsor
  value one-pager + post-conf recaps.
- **Access/reach (Pillar D):** enable community-led locales (Decision 5); promote
  opportunity grants earlier; support global expansion (Kenya and beyond).
- **Review:** 12-month checkpoint against the scorecard; re-pick focus.

### Sequencing logic
1. **Stop the leaks first** — cheap, immediate, compounding.
2. **Then build the asset** (content infrastructure) — the durable advantage.
3. **Then the voice** (AI leadership) — rides the asset and the moment.
4. **Sustainability and reach throughout** — automation funds capacity; capacity
   funds ambition.

---

## How this connects

- Strategy & decisions framing → `BOARD-OFFSITE-BRIEF.md`
- Evidence behind every recommendation → `EXTERNAL-CONTEXT.md`
- Concrete backlog items the roadmap draws on → `MARKETING-REPORT.md`,
  `IMPROVEMENTS-REPORT.md`
- Overview & one-page summary → `STRATEGY-PACK.md`
