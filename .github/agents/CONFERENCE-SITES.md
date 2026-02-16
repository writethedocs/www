# Conference Sites Architecture - README for Robots

## Overview
Write the Docs hosts multiple conferences per year across different cities (Portland, Prague, Australia, Atlantic, etc.). This document explains how conference sites are structured, built, and maintained.

## Directory Structure

```
docs/
├── conf/                           # Conference content
│   ├── [city]/                     # City-specific conferences
│   │   └── [year]/                 # Year-specific content
│   │       ├── index.rst           # Conference home page
│   │       ├── news/               # News articles/blog posts
│   │       ├── speakers.rst        # Speakers page
│   │       ├── schedule.rst        # Schedule page
│   │       ├── tickets.rst         # Tickets information
│   │       ├── sponsors/           # Sponsor information
│   │       └── [other pages].rst   # Additional pages
│   └── index.rst                   # Main conferences index
│
├── _data/                          # Configuration and data files
│   ├── [city]-[year]-config.yaml  # Conference configuration
│   ├── [city]-[year]-sessions.yaml # Talk sessions data
│   ├── [city]-[year]-schedule.yaml # Schedule data
│   └── schema-*.yaml               # YAML schemas
│
├── _templates/                     # Jinja2 templates
│   ├── [year]/                     # Year-specific templates
│   │   ├── base.html              # Base template
│   │   ├── index.html             # Home page template
│   │   ├── generic.html           # Generic page template
│   │   ├── menu-desktop.html      # Desktop navigation
│   │   ├── menu-mobile.html       # Mobile navigation
│   │   ├── speakers.rst           # Speakers list template
│   │   └── sponsors.html          # Sponsors template
│   └── include/                    # Reusable template components
│
├── _static/                        # Static assets
│   └── conf/                       # Conference-specific assets
│       ├── scss/                   # SCSS source files
│       │   ├── main-[year].scss   # Year-specific styles
│       │   └── theme/             # UIKit theme files
│       ├── css/                    # Compiled CSS
│       │   └── main-[year].min.css
│       ├── images/                 # Images
│       │   ├── logos/             # Conference logos
│       │   └── headers/           # Header images
│       └── js/                     # JavaScript files
│
├── _ext/                           # Sphinx extensions
│   ├── core.py                    # Core functionality
│   ├── filters.py                 # Jinja filters
│   └── videos.py                  # Video handling
│
└── conf.py                         # Sphinx configuration

```

## Conference Page Lifecycle

### 1. Creating a New Conference

#### A. Create Configuration File
Create `docs/_data/[city]-[year]-config.yaml`:

```yaml
name: Portland              # City name
shortcode: portland         # URL shortcode
year: 2026                  # Year
city: Portland              # Display city name
local_area: Oregon          # State/region
area: North America         # Geographic area
email: portland@writethedocs.org
color: gold                 # Color theme (gold/yellow/blue)
rgb: 253,185,19            # RGB values for theming
hex: fdb913                # Hex color code
time_format: 12h           # Time format

buttons:                   # Call-to-action buttons
  top:
    - text: Buy a Ticket
      link: /tickets
  bottom:
    - text: Sponsor us
      link: /sponsors/prospectus

date:                      # Event dates and schedule
  short: May 3-5, 2026
  main: May 3-5, 2026
  day_one:
    event: Hike
    date: May 2
    summary: "..."
  # ... more date configurations

flagtickets: true          # Feature flags
flagcfp: false
flagspeaking: true
# ... more flags
```

**Key Configuration Fields:**
- `name`, `shortcode`, `year`: Core identifiers
- `color`, `rgb`, `hex`: Visual theming
- `buttons`: CTA buttons shown on pages
- `date`: Event schedule structure
- `flag*`: Feature toggles (tickets on sale, CFP open, etc.)
- `about`: Conference-specific content (attendee count, etc.)

#### B. Create Directory Structure
```bash
docs/conf/[city]/[year]/
├── index.rst              # Home page
├── news/                  # News directory
│   └── index.rst
├── speakers.rst
├── schedule.rst
├── tickets.rst
├── sponsors/
│   ├── index.rst
│   └── prospectus.rst
└── [other standard pages]
```

#### C. Create Index Page
`docs/conf/[city]/[year]/index.rst`:

```rst
:template: [year]/index.html
:banner: _static/conf/images/headers/[city]-[year]-small-group.jpg
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

:orphan:

.. title:: Home | Write the docs [City] [Year]

.. raw:: html

  <div class="news-block">
    <div class="uk-container">
      <h2>Updates from the team</h2>
      <section>
      <div class="content">

.. postlist:: 10
   :date: %B %d, %Y
   :format: {title} - {date}
   :list-style: none
   :tags: [city]-[year]

.. raw:: html

      </div>
      </section>
    </div>
  </div><!--- end news block -->
```

**Key RST Directives:**
- `:template:`: Specifies Jinja2 template to use
- `:banner:`: Header image
- `:og:image:`: Open Graph image for social media
- `:orphan:`: Don't warn about page not in toctree
- `.. postlist::`: Lists blog posts (from ablog extension)
- `.. raw:: html`: Embeds raw HTML

### 2. Templates and Theming

#### Template Hierarchy
1. **Base Template** (`_templates/[year]/base.html`):
   - HTML structure, head, scripts
   - Loads year-specific CSS: `main-[year].min.css`
   - Includes navigation menus
   - Footer structure

2. **Index Template** (`_templates/[year]/index.html`):
   - Extends base template
   - Hero section with logo and CTA buttons
   - About section
   - Schedule overview
   - News block (rendered from RST)
   - Sponsors section

3. **Generic Template** (`_templates/[year]/generic.html`):
   - Used for standard content pages
   - Page banner with title
   - Content area

#### Jinja2 Variables Available in Templates
From config file:
- `{{ name }}` - City name
- `{{ year }}` - Year as integer
- `{{ year_str }}` - Year as string
- `{{ city }}`, `{{ local_area }}` - Location
- `{{ color }}`, `{{ hex }}`, `{{ rgb }}` - Theme colors
- `{{ date.* }}` - Date configurations
- `{{ buttons.* }}` - CTA buttons
- `{{ flag* }}` - Feature flags
- `{{ about.* }}` - About information

From Sphinx:
- `{{ pathto() }}` - Generate relative paths
- `{{ meta }}` - Page metadata
- `{{ body }}` - Rendered RST content

### 3. Styling System

#### SCSS Architecture
Each year has its own SCSS file that compiles to minified CSS:
- Source: `docs/_static/conf/scss/main-[year].scss`
- Compiled: `docs/_static/conf/css/main-[year].min.css`

**SCSS Structure:**
```scss
// Variables
$base-body-font-family: 'Nunito Sans', sans-serif;
$secondary-font-family: 'Bree Serif', serif;
$main-color: #FDB913;  // Theme color

// Component styles
.hero { ... }           // Hero section
.announcement { ... }   // Announcement banner
.about { ... }          // About section
.schedule-overview { ... }  // Schedule overview
.speakers { ... }       // Speakers section
.news-block { ... }     // News/blog section
.sponsors { ... }       // Sponsors section
footer { ... }          // Footer

// Media queries for responsive design
@media (min-width: 640px) { ... }
@media (min-width: 1024px) { ... }
```

#### Compiling SCSS to CSS
```bash
# Install sass
npm install -g sass

# Compile (from docs/_static/conf/scss/)
sass main-YYYY.scss ../css/main-YYYY.min.css --style=compressed --no-source-map
```

**When to Compile:**
- After any SCSS changes
- Both source SCSS and compiled CSS must be committed

#### CSS Classes Reference
- `.hero` - Main hero section with conference logo
- `.announcement` - Top announcement bar
- `.about` - About section
- `.schedule-overview` - Schedule grid
- `.news-block` - News/updates section
- `.speakers` - Speakers grid
- `.sponsors` - Sponsors section
- `.uk-*` - UIKit framework classes

### 4. Data Files and Sessions

#### Sessions Data
`docs/_data/[city]-[year]-sessions.yaml`:
```yaml
- title: "Talk Title"
  slug: talk-slug
  series: Conference Series
  series_slug: Series-Slug
  year: 2026
  speakers:
    - name: Speaker Name
      slug: speaker-slug
      twitter: '@handle'
      website: 'https://...'
  abstract: |
    Talk description...
  youtubeId: VIDEO_ID  # Added after conference
```

#### Schedule Data
`docs/_data/[city]-[year]-schedule.yaml`:
```yaml
- time: "9:00 AM"
  title: "Doors Open"
  type: general
- time: "9:30 AM"
  title: "Opening Remarks"
  type: general
- time: "10:00 AM"
  slug: talk-slug  # Links to sessions data
  type: talk
```

### 5. Content Pages

#### Standard Pages Structure
Each conference typically includes:

**Core Pages:**
- `index.rst` - Home page
- `speakers.rst` - Speaker list
- `schedule.rst` - Event schedule
- `tickets.rst` - Ticket information
- `code-of-conduct.rst` - Code of Conduct

**Participation Pages:**
- `cfp.rst` - Call for Proposals
- `opportunity-grants.md` - Financial assistance
- `volunteer.md` - Volunteer information
- `writing-day.md` - Writing Day details
- `unconference.md` - Unconference info

**Information Pages:**
- `venue.md` - Venue details
- `visiting.md` - Travel information
- `health.md` - Health & safety
- `team.md` - Organizing team

**Sponsor Pages:**
- `sponsors/index.rst` - Current sponsors
- `sponsors/prospectus.rst` - Sponsorship info

#### Page Metadata
All pages should include:
```rst
:template: [year]/generic.html  or  [year]/index.html
:banner: _static/conf/images/headers/[image].jpg
```

### 6. News/Blog System

#### Creating News Posts
News posts use the `ablog` Sphinx extension.

**Location:** `docs/conf/[city]/[year]/news/[slug].rst`

**Format:**
```rst
:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

.. post:: December 09, 2025
   :tags: {{shortcode}}-{{year}}

Article Title
=============

Article content...
```

**Key Elements:**
- `.. post::` directive with date
- `:tags:` must match conference tag pattern: `[city]-[year]`
- Tag is used by `.. postlist::` to filter posts

#### News Display on Home Page
The home page `index.rst` uses `.. postlist::`:
```rst
.. postlist:: 10
   :date: %B %d, %Y
   :format: {title} - {date}
   :list-style: none
   :tags: portland-2026
```

This generates an HTML list (`<ul>`) with `<li>` elements containing `<p>` tags.

### 7. Sponsors

#### Adding Sponsors
1. **Add logo:** `docs/_static/conf/images/sponsors/[sponsor-name].png`
2. **Update config:** `docs/_data/[city]-[year]-config.yaml`

```yaml
sponsors:
  keystone:
    - name: Sponsor Name
      link: https://...
      brand: sponsor-name  # Matches logo filename
  patron:
    - name: ...
```

**Sponsor Tiers:**
- keystone
- patron
- publisher
- second draft
- in_kind (non-financial)

### 8. Building and Testing

#### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Build HTML
cd docs
make html

# Build with live reload
make livehtml  # Opens on http://localhost:8888

# View built site
cd _build/html
python3 -m http.server 8888
# Visit: http://localhost:8888/conf/[city]/[year]/
```

#### Common Build Commands
- `make html` - Full build
- `make clean` - Clean build artifacts
- `BUILD_VIDEOS=True make html` - Build with video pages

### 9. Feature Flags

Feature flags in config control what's displayed:

```yaml
flaghasschedule: true     # Show schedule link
flaghasspeakers: true     # Show speakers
flagtickets: true         # Tickets available
flagspeaking: true        # Show speaking info
flagcfp: false            # CFP open
flagticketsonsale: true   # Tickets on sale
flagsoldout: false        # Event sold out
flaghasshirts: true       # Shirts available
flagvideos: false         # Videos published
flaghaslightningtalks: true
flaghasunconf: true       # Unconference happening
flaghasjobfair: true      # Job fair/sponsor expo
flaghasbadgeflair: true   # Badge flair available
flaghaslivestream: false  # Livestream available
flagpostconf: false       # Conference ended
flagcancelled: false      # Conference cancelled
```

**Usage in Templates:**
```jinja
{% if flagtickets %}
  Show tickets information
{% endif %}
```

### 10. Common Workflows

#### Adding a New Conference
1. Copy previous year's config and update
2. Create directory structure
3. Create index.rst with postlist
4. Create standard pages (copy from previous year)
5. Update dates and feature flags
6. Test build locally

#### Updating Conference Status
1. Update feature flags in config
2. Update button links in config
3. Add news post announcing changes
4. Rebuild site

#### Publishing Talk Videos
1. Add `youtubeId` to sessions YAML
2. Ensure videos directory in toctree
3. Build with `BUILD_VIDEOS=True make html`
4. Commit video pages and updated data

#### Fixing Styling Issues
1. Edit `docs/_static/conf/scss/main-[year].scss`
2. Compile: `sass main-[year].scss ../css/main-[year].min.css --style=compressed`
3. Test in browser
4. Commit both SCSS and compiled CSS

### 11. Key Technologies

- **Sphinx**: Static site generator (Python-based)
- **reStructuredText (RST)**: Markup language for content
- **Jinja2**: Template engine
- **ablog**: Sphinx extension for blog functionality
- **SASS**: CSS preprocessor
- **UIKit**: CSS framework (loaded via CDN)

### 12. URL Structure

Conference URLs follow this pattern:
```
https://www.writethedocs.org/conf/[city]/[year]/[page]/
```

Examples:
- `/conf/portland/2026/` - Home page
- `/conf/portland/2026/speakers/` - Speakers page
- `/conf/portland/2026/news/welcome/` - News article
- `/conf/portland/2026/sponsors/prospectus/` - Sponsor info

### 13. Troubleshooting

#### Styles Not Updating
- Ensure SCSS is compiled to CSS
- Clear browser cache (Ctrl+Shift+R)
- Check correct CSS file is referenced in template
- Verify CSS file exists in `_build/html/_static/conf/css/`

#### Template Not Found
- Check `:template:` directive in RST file
- Verify template exists in `_templates/[year]/`
- Ensure year number matches

#### Config Values Not Showing
- Verify config file name: `[city]-[year]-config.yaml`
- Check YAML syntax (indentation matters)
- Rebuild: `make clean && make html`

#### News Posts Not Appearing
- Check `.. post::` directive has date
- Verify `:tags:` matches postlist filter
- Ensure tags field uses correct format: `[city]-[year]`

### 14. Best Practices

1. **Year-Specific Files**: Each year should have independent files (don't reuse SCSS/templates across years unless intentional)

2. **Config-Driven**: Use config file for content that changes (dates, flags, buttons) rather than hardcoding in templates

3. **Consistent Structure**: Follow established directory structure and naming conventions

4. **Test Locally**: Always build and test locally before committing

5. **Commit Both**: When updating SCSS, commit both source and compiled CSS

6. **Progressive Enhancement**: Ensure site works without JavaScript/external resources

7. **Responsive Design**: Test on mobile, tablet, desktop

8. **Accessibility**: Use semantic HTML, proper heading hierarchy, alt text

### 15. Related Documentation

- Sphinx Documentation: https://www.sphinx-doc.org/
- reStructuredText Primer: https://www.sphinx-doc.org/en/stable/rest.html
- Jinja2 Documentation: https://jinja.palletsprojects.com/
- ablog Documentation: https://ablog.readthedocs.io/
- UIKit Documentation: https://getuikit.com/docs/

### 16. Quick Reference

**Create new conference page:**
```bash
cp -r docs/conf/portland/2025 docs/conf/portland/2026
cp docs/_data/portland-2025-config.yaml docs/_data/portland-2026-config.yaml
# Edit files to update year, dates, etc.
```

**Compile SCSS:**
```bash
cd docs/_static/conf/scss
sass main-2026.scss ../css/main-2026.min.css --style=compressed --no-source-map
```

**Build site:**
```bash
cd docs
make html
```

**Test locally:**
```bash
cd docs/_build/html
python3 -m http.server 8888
```

---

## For Automated Agents

When working on conference sites:

1. **Identify the conference**: Extract city and year from the issue/path
2. **Locate config file**: `docs/_data/[city]-[year]-config.yaml`
3. **Find page files**: `docs/conf/[city]/[year]/`
4. **Check template**: Look for `:template:` directive in RST
5. **For styling**: Edit SCSS, compile to CSS, test in browser
6. **For content**: Edit RST files, rebuild with `make html`
7. **Always commit**: Both source files (SCSS/RST) and generated files (CSS/HTML)

**Common Patterns:**
- News posts: `docs/conf/[city]/[year]/news/*.rst` with `.. post::` directive
- Config-driven content: Check YAML file first
- Year-specific styles: One SCSS per year
- Feature toggles: Use `flag*` variables in config
