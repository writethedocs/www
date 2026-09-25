# Docs-as-Code Tools Matrix — Contributor Guide

New to contributing? Start with the [Write the Docs contributing guide](../contributing) before making changes.

The tools matrix is a community-curated comparison of documentation tools used in docs-as-code workflows, covering static site generators, hosted platforms, API doc tools, AI writing assistants, and more.

## How to edit this page

### Location of this page

```text
docs/guide/tools/docs-as-code-tools-matrix.rst
```

> **Note:** The JavaScript in the RST has hardcoded column indices. If any columns are added, removed, or reordered, `docs-as-code-tools-matrix.rst` must also be updated. See [Adding or removing a column](#adding-or-removing-a-column) below.

### Location of the CSV file

The tool rows and column data are managed in:

```text
docs/_data/tools.csv
```

---

## Column structure

The CSV has 33 columns. **Order matters** — each column maps directly to a zero-based index used in the JavaScript.

| # | Column | Accepted values |
|---|--------|-----------------|
| 0 | Tool | Tool name |
| 1 | URL | Full URL |
| 2 | Category | See [Category values](#category) below |
| 3 | Description | Free text |
| 4 | Cost | `Free (Open-source)`, `Freemium`, `Freemium, Free (Open-source)`, `Free (Open-source), Pay-to-use`, `Free (Open-source), Pay-to-host`, `Pay-to-use` |
| 5 | Business Model | `Open-source / Donations`, `Open-core`, `VC-backed SaaS`, `Subscription`, `Part of Larger Product` |
| 6 | Maintained By | `Community`, `Company`, `Solo Maintainer` |
| 7 | Maintenance | `Yes`, `Partial`, `No` |
| 8 | Markup Language | e.g. `Markdown`, `MDX`, `reStructuredText, Markdown`, `AsciiDoc`, `XML, DITA`, `HTML, Markdown` |
| 9 | Content Model | `Static`, `Dynamic`, `Hybrid` |
| 10 | Authoring Workflow Model | Comma-separated from: `Local files + CLI`, `Git-synced`, `In-browser editor`, `AI-assisted`, `API Spec-driven`, `IDE-integrated`, `Annotated source code` |
| 11 | Visual Editor | `Yes`, `Partial`, `No` |
| 12 | Content Reuse | `Yes`, `No` |
| 13 | Dark Mode | `Yes`, `No` |
| 14 | Output Formats | e.g. `HTML`, `HTML, PDF`, `HTML, PDF, ePub`, `HTML, JSON` |
| 15 | Publishing & Delivery | Comma-separated from: `Deploy automation`, `Edge/CDN-friendly`, `Preview environments`, `Multi-environment`, `Release gating` |
| 16 | CI/CD | `Yes`, `No` |
| 17 | Incremental Builds | `Yes`, `No` |
| 18 | Custom Domain | `Yes`, `No` |
| 19 | Multi-repo Support | `Yes`, `No` |
| 20 | Versioning | `Yes`, `No` |
| 21 | Private/Gated Docs | `Yes`, `No` |
| 22 | i18n | `Yes`, `No` |
| 23 | Search | `Built-in (Client-side)`, `Built-in (Server-side)`, `Pluggable`, `None` |
| 24 | Plugin Ecosystem | `Yes`, `Partial`, `No` |
| 25 | Theming Control | `Yes`, `Partial`, `No` |
| 26 | Auth / Security Methods | Comma-separated from: `RBAC`, `SSO (SAML 2.0)`, `OIDC / OAuth`, `SCIM`, `2FA / TOTP`, `Password (shared)`, `Secret Link`, `Token / HTTP Header`, `Custom Auth Backend`, `Git-provider SSO`, `LDAP`, `On-prem / Air-gapped`, `DIY / None built-in` |
| 27 | Security Notes | Free text (no filter dropdown) |
| 28 | AI Authoring | `Yes`, `Partial`, `No` |
| 29 | AI End-User Q&A | Comma-separated from: `Built-in AI chat/search`, `MCP server`, `llms.txt provided`, `Kapa.ai / Inkeep / similar embed`, `Algolia Ask AI, llms.txt provided`, `External / DIY integration only` |
| 30 | AI Pricing & Models | Free text. Format: `billing · models` (e.g. `Included in plan · Claude, OpenAI`). Use `BYOK` for bring-your-own-key. |
| 31 | AI Tooling Origin | `First-party (built-in)`, `Third-party only`, `Hybrid (first-party + 3rd-party)`, `None` |
| 32 | Local Models Supported | `Yes`, `No`, `Unknown` |

### Category

Category is a comma-separated list. Use only values from this list:

`AI`, `API Docs`, `DevOps`, `Framework`, `IDE`, `Knowledge Management`, `PaaS`, `Platform`, `Static Site Generator`

---

## Adding a new tool

1. Open `docs/_data/tools.csv`
2. Add a new row in alphabetical order by tool name
3. Provide values for all 33 columns — use `""` (empty) for unknown fields
4. All values must be double-quoted
5. Multi-value fields use comma-separated values within the quotes (e.g. `"Framework, Static Site Generator"`)
6. Update the tool count in `docs-as-code-tools-matrix.rst` (line 6: `"comparison of N documentation tools"`)

## Editing an existing tool

Open `docs/_data/tools.csv`, find the tool's row, and update the relevant cells. Refer to the accepted values table above for categorical columns.

## Adding or removing a column

1. Add or remove the column in `docs/_data/tools.csv` — header row and every data row
2. Open `docs/guide/tools/docs-as-code-tools-matrix.rst` and update:
   - The `visible: false, targets: [...]` array — indices of all hidden columns
   - The `forEach([...])` array — indices of all columns with filter dropdowns (exclude URL, Description, Security Notes)
   - The `prefixes` map in `columnText` if the column belongs to an Author/Pub/Scale group (indices 9–22)
   - The comment on the line starting `// Default visible:`
3. Reordering columns shifts all subsequent indices — update every index reference above

## Editing the glossary

The glossary lives at the bottom of `docs-as-code-tools-matrix.rst`, starting at the `.. _tools-matrix-glossary:` anchor. Add, remove, or update entries there directly. Entries are grouped by the column they relate to.

---

## Building and previewing

All build commands run from the `docs/` directory:

```bash
# Live preview (recommended)
cd docs && uv run make livehtml
# Serves at http://127.0.0.1:8888

# One-off build
cd docs && uv run make html
```

Python 3.12 and `uv` are required. Run `uv sync` to install dependencies.
