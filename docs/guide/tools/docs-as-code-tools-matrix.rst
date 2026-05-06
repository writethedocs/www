.. _docs-as-code-tools-matrix:

Documentation Tools Matrix
==========================

A community-curated comparison of 27 documentation tools used in docs-as-code workflows,
covering static site generators, hosted platforms, API doc tools, AI writing assistants, and more.

**How to use this table:**

- **Search** — the search box filters across all visible columns
- **Column filters** — every column has a multi-select filter; click to select one or more values
- **Columns button** — show or hide additional columns grouped by category (authoring, publishing, scale, security, AI, and more)
- :ref:`Glossary <tools-matrix-glossary>` — definitions for column values, categories, and abbreviations used in this table
- :doc:`How to edit this page <docs-as-code-tools-matrix-contributing>` — add a tool, update an entry, or modify columns

.. raw:: html

   <link rel="stylesheet" type="text/css" href="../../../_static/css/datatables/dataTables.dataTables.min.css">
   <link rel="stylesheet" type="text/css" href="../../../_static/css/datatables/buttons.dataTables.min.css">
   <style>
     table.datatable tbody td { vertical-align: top; }
     table.datatable tbody td:nth-child(3) {
       font-size: 0.85em;
       max-width: 300px;
     }
     div.dt-buttons { margin-bottom: 8px; }
   </style>

.. csv-table::
   :class: datatable
   :header-rows: 1
   :file: ../../_data/tools.csv

.. raw:: html

   <script src="../../../_static/js/datatables/jquery.min.js"></script>
   <script src="../../../_static/js/datatables/dataTables.min.js"></script>
   <script src="../../../_static/js/datatables/dataTables.buttons.min.js"></script>
   <script src="../../../_static/js/datatables/buttons.colVis.min.js"></script>
   <script>
   function initToolsMatrix() {
     // Sphinx csv-table wraps every cell in a <p> tag — unwrap before DataTables reads the table
     document.querySelectorAll('table.datatable td, table.datatable th').forEach(function (cell) {
       var p = cell.querySelector('p');
       if (p && cell.childElementCount === 1) {
         while (p.firstChild) { cell.insertBefore(p.firstChild, p); }
         p.remove();
       }
     });

     // Default visible: Tool (0), Category (2), Description (3), Cost (4), Markup Language (8)
     // Hidden by default: URL (1), Business Model (5) ... Local Models Supported (32)
     new DataTable('table.datatable', {
       dom: 'Bfrtip',
       buttons: [{
         extend: 'colvis',
         text: 'Columns',
         columnText: function (dt, idx, title) {
           var prefixes = {
             9: 'Author: ', 10: 'Author: ', 11: 'Author: ', 12: 'Author: ', 13: 'Author: ',
             14: 'Pub: ', 15: 'Pub: ', 16: 'Pub: ', 17: 'Pub: ', 18: 'Pub: ',
             19: 'Scale: ', 20: 'Scale: ', 21: 'Scale: ', 22: 'Scale: '
           };
           return (prefixes[idx] || '') + title;
         }
       }],
       pageLength: 25,
       columnDefs: [
         {
           targets: 0,
           render: function (data, type, row) {
             if (type !== 'display') return data;
             var url = (row[1] || '').trim();
             if (!url) return data;
             var a = document.createElement('a');
             a.href = url;
             a.target = '_blank';
             a.rel = 'noopener';
             a.textContent = data;
             return a.outerHTML;
           }
         },
         { visible: false, targets: [1, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32] }
       ],
       initComplete: function () {
         var api = this.api();
         [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32].forEach(function (colIdx) {
           var col = api.column(colIdx);
           var header = col.header();
           makeColumnFilter(col, header);
         });
       }
     });
   }

   function makeColumnFilter(col, header) {
     var seen = {}, vals = [];
     col.data().each(function (d) {
       String(d).split(',').forEach(function (v) {
         v = v.trim();
         if (v && !seen[v]) { seen[v] = true; vals.push(v); }
       });
     });
     vals.sort();
     if (vals.length === 0) return;

     var wrapper = document.createElement('div');
     wrapper.style.cssText = 'position:relative;margin-top:4px;';

     var btn = document.createElement('button');
     btn.type = 'button';
     btn.textContent = 'All';
     btn.style.cssText = 'width:100%;font-size:0.82em;font-weight:normal;padding:2px 4px;box-sizing:border-box;cursor:pointer;text-align:left;';

     var panel = document.createElement('div');
     panel.style.cssText = 'display:none;position:absolute;z-index:9999;background:#fff;border:1px solid #ccc;padding:4px;min-width:150px;max-height:200px;overflow-y:auto;box-shadow:0 2px 4px rgba(0,0,0,0.15);';

     var checkboxes = [];
     vals.forEach(function (v) {
       var label = document.createElement('label');
       label.style.cssText = 'display:flex;align-items:center;gap:4px;padding:2px 0;font-size:0.82em;white-space:nowrap;cursor:pointer;font-weight:normal;';
       var cb = document.createElement('input');
       cb.type = 'checkbox';
       cb.value = v;
       label.appendChild(cb);
       label.appendChild(document.createTextNode(v));
       panel.appendChild(label);
       checkboxes.push(cb);
       cb.addEventListener('change', updateFilter);
     });

     function updateFilter() {
       var selected = checkboxes
         .filter(function (c) { return c.checked; })
         .map(function (c) { return c.value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); });
       if (selected.length === 0) {
         col.search('', false, false).draw();
         btn.textContent = 'All';
       } else {
         col.search(selected.join('|'), true, false).draw();
         btn.textContent = selected.length + ' selected';
       }
     }

     btn.addEventListener('click', function (e) {
       e.stopPropagation();
       document.querySelectorAll('.col-filter-open').forEach(function (p) {
         if (p !== panel) { p.style.display = 'none'; p.classList.remove('col-filter-open'); }
       });
       var isOpen = panel.classList.contains('col-filter-open');
       panel.style.display = isOpen ? 'none' : 'block';
       panel.classList.toggle('col-filter-open', !isOpen);
     });

     document.addEventListener('click', function () {
       panel.style.display = 'none';
       panel.classList.remove('col-filter-open');
     });

     wrapper.appendChild(btn);
     wrapper.appendChild(panel);
     header.appendChild(wrapper);
   }

   if (document.readyState === 'loading') {
     document.addEventListener('DOMContentLoaded', initToolsMatrix);
   } else {
     initToolsMatrix();
   }
   </script>

.. _tools-matrix-glossary:

Glossary
--------

**Docs-as-code** — Treating documentation like software: storing content in Git, reviewing changes via pull requests, and publishing through automated CI/CD pipelines.

**Category**

- **API Docs** — Tools built around or outputting API reference documentation from machine-readable specs (OpenAPI, etc.).
- **DevOps** — Tooling designed to fit inside engineering workflows: CI/CD pipelines, repo automation, environment parity.
- **Framework** — A toolkit you assemble into your own docs site. You bring the hosting and deployment plumbing.
- **IDE** — Docs tooling that runs inside a developer editor (e.g. JetBrains) rather than as a hosted service.
- **Knowledge Management (KM)** — Tools focused on organizing internal or external knowledge bases, not just product documentation.
- **PaaS** — Platform as a Service. A hosting layer that builds and deploys your docs for you; you own the content and site.
- **Platform** — A hosted product providing an end-to-end docs experience: authoring, hosting, search, analytics, auth, and versioning in one place.
- **Static Site Generator (SSG)** — Builds static HTML files from source content at build time. No server-side rendering at request time.

**Content Model**

- **Static** — Content is compiled into fixed HTML at build time and served directly from a CDN or file server.
- **Dynamic** — Content is rendered or assembled server-side at request time, supporting personalization, gating, and live data.
- **Hybrid** — Combines both: some content is pre-built, some is rendered or fetched at runtime.

**Markup Language**

- **DITA** — Darwin Information Typing Architecture. An XML-based structured authoring standard built around modular topics and maps, typically used in enterprise CCMS environments.
- **MDX** — Markdown with embedded JSX/React components. Enables interactive or dynamic elements inside otherwise static Markdown files.

**Business Model**

- **Open-core** — The core tool is open-source; advanced features (enterprise auth, analytics, hosting) are offered as a paid product.

**Authoring Workflow Model**

- **AI-assisted** — The tool has built-in AI features that help write or generate content during authoring.
- **API Spec-driven** — Documentation is generated from or tightly coupled to a machine-readable API spec (e.g. OpenAPI).
- **IDE-integrated** — Authoring happens inside a developer IDE rather than a browser or CLI.

**Search**

- **Built-in (Client-side)** — Search index is compiled at build time and runs in the browser. Fast with no server required, but limited at large scale.
- **Built-in (Server-side)** — Search runs on the host's server infrastructure. Scales better and supports access-aware results.
- **Pluggable** — No built-in search; designed to integrate with an external search provider (Algolia, Elasticsearch, etc.).

**Auth / Security Methods**

- **RBAC** — Role-Based Access Control. Permissions are assigned by role (editor, viewer, admin) rather than per user.
- **SAML 2.0 / SSO** — Security Assertion Markup Language. Enterprise single sign-on that delegates authentication to an identity provider (Okta, Azure AD, Google Workspace, etc.).
- **OIDC / OAuth** — OpenID Connect / OAuth 2.0. Modern protocols for authentication and authorization, often used for provider login (GitHub, Google) or API access.
- **SCIM** — System for Cross-domain Identity Management. Automates user provisioning and deprovisioning from your identity provider.
- **Secret Link** — Access granted by sharing a private URL rather than requiring a login.

**AI Pricing & Models**

- **BYOK** — Bring Your Own Key. The tool uses AI capabilities but requires you to supply your own API key (OpenAI, Anthropic, etc.). You are billed directly by the AI provider.

**AI End-User Q&A**

- **llms.txt** — A proposed standard (``/llms.txt``) that provides a structured, LLM-friendly summary of a site's content to improve AI-generated answers about the documentation.
- **MCP server** — Model Context Protocol server. An interface that lets AI agents query or interact with a tool's data in a structured way.

**AI Tooling Origin**

- **First-party (built-in)** — AI features are built and maintained directly by the tool vendor.
- **Third-party only** — AI capabilities come entirely from an external service (e.g. Algolia AI, Kapa.ai).
- **Hybrid** — Combines the vendor's own AI features with one or more third-party AI integrations.

.. toctree::
   :hidden:

   docs-as-code-tools-matrix-contributing
