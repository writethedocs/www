# Write the Docs — Opportunities Report

A prioritized assessment of how to add value to the Write the Docs community
through its website and surrounding assets, with attention to what AI can
feasibly implement.

Prepared: 2026-06-04. Scope: the `writethedocs/www` repository, its build and
CI tooling, content structure, and ~230 open/closed GitHub issues.

---

## 1. Executive summary

Write the Docs sits on assets that are rare on the open web: an authoritative,
vendor-neutral **Guide** to documentation; **10+ years of conference talks**; a
unique annual **salary survey**; and an active **Slack community**. The website
is a healthy Sphinx static site, but these assets are under-leveraged — the
talk archive is barely discoverable, the Guide has no learning path, community
knowledge evaporates in Slack, and the site never checks its own outbound links.

The highest-leverage work falls into two layers:

- **Strategic ("think bigger"):** turn the existing assets into durable,
  discoverable, trustworthy resources. This is exactly the kind of structuring,
  summarizing, and tagging work AI is well-suited to.
- **Tactical:** a backlog of bounded, verifiable fixes (accessibility, SEO,
  broken links, automation of manual steps) that an AI can largely own.

The recommended starting points are the **conference talk archive** (strategic,
high AI-leverage) and a **bundle of low-risk mechanical fixes** (tactical,
CI-verifiable).

---

## 2. Strategic opportunities ("bigger" value)

Ordered by value × AI-leverage. Most require some human/community judgment;
each note calls out the split.

### 2.1 Make the talk archive usable — transcribe, summarize, tag
**Why:** Hundreds of talks span 10+ years, but discovery is poor (the archive is
barely sortable — issue #1976) and the Topics page is hand-maintained. This is a
recorded history of the field that almost no one can search.
**What:** Generate transcripts, short summaries, and topic tags for the back
catalog; produce per-talk pages that are searchable, linkable, captioned
(accessibility), and strong for SEO.
**AI split:** AI can largely own this. Humans spot-check quality.
**Verdict:** Highest-leverage starting point.

### 2.2 Turn the Guide into a guided learning experience
**Why:** The Guide is the crown jewel but is a flat set of mixed RST/MD pages
with no path through it, some stale content (API section — #2171), and no
tagging (#952). Multiple issues are really asking for this: #1085, #527, #1717,
#1399.
**What:** Role-based learning paths ("developer handed the docs",
"career-changer", "docs-team lead"), cross-linked topics, and a gap analysis of
stale/missing content.
**AI split:** AI does tagging, cross-linking, gap analysis, and first-draft
restructuring; a human editor owns the information architecture.

### 2.3 Capture recurring Slack wisdom as canonical answers
**Why:** The same questions recur forever in an ephemeral medium ("what tool?",
"how do I learn git?", "convince my manager"). A curated, living FAQ turns that
into permanent web content — a more tractable version of the long-requested
community blog (#1767).
**AI split:** AI clusters recurring questions and drafts answers from existing
Guide content; humans curate. Needs community buy-in for ongoing curation.

### 2.4 Make the salary survey interactive and comparable
**Why:** Unique data presented as static prose; #2102 already asked for better
presentation. It is a reason people visit the site.
**What:** A filterable, year-over-year explorer (region, role, experience).
**AI split:** Bounded data + frontend project AI can largely own; survey design
choices benefit from a human.

### 2.5 Position WTD as the authoritative source for the AI era
**Why:** WTD's content is exactly what is being ingested into LLMs now. WTD
could deliberately become the trusted, citable source on documentation
practices.
**What:** Clean structured content, an `llms.txt`, schema.org markup, stable
canonical URLs — so AI answers about documentation trace back to WTD.
**AI split:** Low-effort, high-strategic-payoff; AI can largely own it.

> Honest caveat: WTD runs on volunteer time. The best bets are ones where AI
> does the heavy lifting and leaves humans only the judgment calls — which is
> why 2.1 and 2.5 lead.

---

## 3. Tactical improvements (prioritized)

Ordered by value × how cleanly an AI can implement them (bounded scope,
verifiable by the build/CI, low ambiguity).

### Tier 1 — High value, low ambiguity

1. **Catch broken external links before users do.** The most recurring issue
   class: expired Slack invites (#2419, #2250, #2238), dead CDC links (#1734),
   stale API/git links (#2137, #2009), older "fix broken links" tickets (#1079,
   #1334). Root cause: htmlproofer runs with `--disable-external=true`, so CI
   never checks outbound links. Add a scheduled (weekly), non-blocking
   external-link-check workflow that opens an issue on failure, plus a one-time
   sweep of current dead links.
2. **Enforce image alt text (accessibility).** htmlproofer sets
   `--ignore-missing-alt=true`, and sponsor/footer logos across
   `_templates/2019–2024/sponsors*.html` have missing or empty `alt=`. Add
   descriptive alt text, then flip the flag to enforce.
3. **Fix the 404-page home/breadcrumb links (#2033).** On 404 pages the logo and
   breadcrumb point to `#`, trapping lost users.
4. **Add SEO/social metadata to the main site, not just conference pages.**
   OG/Twitter tags exist only in conference `base.html`; the main `layout.html`
   (Guide, Topics, etc.) has none. Wire `sphinxext-opengraph` defaults into the
   Alabaster layout. Also add schema.org `Event` JSON-LD to conference pages
   (#1026).
5. **Repo hygiene quick wins.** Dead Greenkeeper badge in `README.md` (service
   shut down 2020); `footer.html` "contribute" link points to the `master`
   branch though the default is now `main`.
6. **Add a `CONTRIBUTING.md` (#1152).** Long-requested. Synthesize from the
   README, `AGENTS.md`/`CLAUDE.md`, and the style guide; also reduces the
   build-setup confusion seen in #2214.

### Tier 2 — Medium effort, clear payoff

7. **Replace manual config flags with automatic logic.** Show sponsors only when
   sponsor data exists (#2053); auto-link the current/upcoming conference on the
   landing page by iterating config YAML + dates (#1680); move the announcement
   banner's hardcoded if/elif date ranges out of `conf.py` into config YAML.
8. **Sort the video archive by date (#1976).**
9. **Content freshness pass.** API section is outdated (#2171). Scope as
   "draft PR for human review," not autonomous merge.
10. **Image performance.** Only ~13 WebP vs ~983 PNG/JPG. Convert with
    fallbacks; add font `preload` and script `defer`.

### Tier 3 — Larger / structural (AI-assisted, human-steered)

- RST→MyST Markdown conversion of the Guide (#1509) — mechanical but large diff,
  needs review.
- Template de-duplication — 2019–2024 conference template sets are
  near-identical copies; consolidation reduces maintenance but risks per-year
  regressions.
- Speaker/session restructure (#2026) — an IA/design decision.

---

## 4. Not recommended for autonomous AI work

These need community/maintainer decisions, not code:

- **Translations** (#1155) — ongoing human commitment.
- **Community blog platform** (#1767) — strategy + curation.
- **Guide IA restructure** (#1085, #527) — editorial ownership.
- **Analytics choice** (#1871) — effectively resolved; the site already uses
  privacy-first SimpleAnalytics.
- **Meetup/swag operational processes** (#1744, #1177) — org logistics.

---

## 5. Tech-debt notes (for context)

Observed during review; mostly absorbed into the items above:

- `conf.py` hardcodes announcement-banner date ranges and carries a Windows
  UTF-8 monkeypatch against `sphinxcontrib.datatemplates` internals (fragile if
  the library changes).
- Schema carries unused fields (`hex`, `hex_contrast`, `templatecode`) flagged
  for deletion.
- `atom_absolute.py` hardcodes ~34 feed tags that need manual updates.
- `_ext/meetup_events.py` has an unresolved FIXME (country filter) and a TODO
  (cron output).
- CI build is strict (`-W --keep-going`), which is good — it means most of the
  Tier 1 fixes are self-verifying.

---

## 6. Recommended next steps

1. **Prototype the talk archive (2.1)** — build the transcription / summary /
   tagging pipeline and generate a few example talk pages to show the shape
   before committing.
2. **Ship a Tier 1 mechanical bundle** — 404 links (#3), repo hygiene (#5), and
   alt-text enforcement (#2): independent, low-risk, verified by the existing
   build.
3. **Add the external-link-check workflow (Tier 1 #1)** as a standalone PR.

Items 2 and 3 are safe to do now. Item 1 and the other strategic bets benefit
from a quick check-in with the WTD team before investing.
