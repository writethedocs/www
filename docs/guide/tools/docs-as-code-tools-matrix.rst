.. _docs-as-code-tools-matrix:

Documentation Tools Matrix
==========================

A community-curated comparison of 27 documentation tools used in docs-as-code workflows,
covering static site generators, hosted platforms, API doc tools, AI writing assistants, and more.

**How to use this table:**

- **Search** — the search box filters across all visible columns
- **Column dropdowns** — every column has a filter dropdown; hidden columns get their dropdown when revealed
- **Columns button** — show or hide additional columns (Maintenance, Content Model, Visual Editor, i18n, Versioning, CI/CD, Search, Output Formats, and more)

.. raw:: html

   <link rel="stylesheet" type="text/css" href="../../../_static/css/datatables/dataTables.dataTables.min.css">
   <link rel="stylesheet" type="text/css" href="../../../_static/css/datatables/buttons.dataTables.min.css">
   <style>
     table.datatable thead th select {
       display: block;
       width: 100%;
       margin-top: 4px;
       font-size: 0.82em;
       font-weight: normal;
       padding: 2px 4px;
       box-sizing: border-box;
     }
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

     // Default visible: Tool (0), Category (2), Description (3), Cost (4), Markup Language (5), Learning Curve (6)
     // Hidden by default: URL (1), Maintenance (7), Content Model (8) ... AI Authoring (18)
     new DataTable('table.datatable', {
       dom: 'Bfrtip',
       buttons: [{ extend: 'colvis', text: 'Columns' }],
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
         { visible: false, targets: [1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] }
       ],
       initComplete: function () {
         var api = this.api();
         // Add per-column dropdowns for all categorical columns (hidden cols get them too; appear when revealed)
         [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18].forEach(function (colIdx) {
           var col = api.column(colIdx);
           var header = col.header();
           var select = document.createElement('select');
           var seen = {};
           var vals = [];
           col.data().each(function (d) {
             String(d).split(',').forEach(function (v) {
               v = v.trim();
               if (v && !seen[v]) { seen[v] = true; vals.push(v); }
             });
           });
           vals.sort();
           select.add(new Option('All', ''));
           vals.forEach(function (v) { select.add(new Option(v, v)); });
           header.appendChild(select);
           select.addEventListener('change', function () {
             col.search(this.value ? this.value : '', false, false).draw();
           });
         });
       }
     });
   }

   if (document.readyState === 'loading') {
     document.addEventListener('DOMContentLoaded', initToolsMatrix);
   } else {
     initToolsMatrix();
   }
   </script>
