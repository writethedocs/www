# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the source for [www.writethedocs.org](https://www.writethedocs.org), the Write the Docs community website. It's a Sphinx-based static site that uses reStructuredText and Markdown content, Jinja2 templating, and YAML data files for conference configuration. Hosted on Read the Docs.

## Build Commands

All build commands run from the `docs/` directory using `make` (not raw `sphinx-build`):

- **Build site:** `cd docs && uv run make html`
- **Live preview:** `cd docs && uv run make livehtml` (serves at http://127.0.0.1:8888)
- **Clean build:** `cd docs && make clean && uv run make html`
- **Compile SCSS:** `sass --style=compressed --no-source-map docs/_static/conf/scss/main-YYYY.scss docs/_static/conf/css/main-YYYY.min.css`

Python 3.12 is required. Dependencies: `uv sync`

## CI Checks (GitHub Actions)

All run on push/PR to `main`:
- **Ubuntu Build** (`ubuntu.yml`): Sphinx build + htmlproofer link checking (internal links only, with `--swap-urls` to treat `writethedocs.org` URLs as local)
- **Validate YAML** (`validate_yaml.yml`): Runs `docs/_scripts/validate-yaml.sh` with yamale schema validation
- **Spellcheck** (`spellcheck.yml`): codespell with ignore list at `codespell/ignore.txt`
- **Vale** (`vale.yml`): Prose linting with configs at `vale/vale.ini`, `vale/guide.ini`, `vale/news.ini`

Pre-commit hooks validate YAML files in `docs/_data/` (yamllint, check-yaml, trailing whitespace, schema validation with yamale).

## Architecture

### Content Processing Pipeline

All RST/MD files are processed through Jinja2 before Sphinx renders them (`_ext/core.py:render_rst_with_jinja`). This means Jinja tags (`{{ }}`, `{% %}`) work in any content file. Conference pages get their YAML config injected as Jinja context automatically based on the URL path pattern `conf/<city>/<year>/`.

### Conference Data System

Each conference (2020+) has three YAML data files in `docs/_data/`:
- `<city>-<year>-config.yaml` — configuration, feature flags (`flag*`), dates, buttons, sponsors
- `<city>-<year>-sessions.yaml` — speaker/talk data
- `<city>-<year>-schedule.yaml` — schedule with slugs referencing sessions

YAML schemas for validation: `docs/_data/schema-config.yaml`, `schema-schedule.yaml`, `schema-sessions.yaml`

Pre-2020 conferences use a different naming convention (`config-<city>-<year>.yaml`).

### Templates

Year-specific HTML templates in `docs/_templates/<year>/` (base.html, index.html, generic.html, menu-*.html). Pages specify their template via `:template: <year>/generic.html` metadata in RST.

### Custom Sphinx Extensions (`docs/_ext/`)

- `core.py` — Jinja rendering of RST, conference YAML context loading, template override system
- `filters.py` — Custom Jinja filters (e.g., speaker photo paths)
- `meetups.py` — `meetup-listing` directive
- `atom_absolute.py` — Rewrites atom feed URLs to absolute

### Styling

Per-year SCSS files at `docs/_static/conf/scss/main-<year>.scss` compile to `docs/_static/conf/css/main-<year>.min.css`. Uses UIKit CSS framework (via CDN). Both SCSS source and compiled CSS must be committed.

### Blog/News

Uses the `ablog` extension. News posts go in `docs/conf/<city>/<year>/news/` with `.. post::` directive and `:tags: <city>-<year>` for filtering via `.. postlist::` on conference index pages.

## Key Conventions

- Content files support both `.rst` and `.md` (via myst-parser)
- Conference pages use `:orphan:` directive (not in a toctree)
- Feature flags in config YAML control what sections display (e.g., `flagtickets`, `flagcfp`, `flaghasschedule`)
- Conference talk videos are hosted on the [Write the Docs YouTube channel](https://www.youtube.com/c/WritetheDocs)
