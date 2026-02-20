# CSS Styling Fixes for Conference Pages

## Overview
This guide helps with fixing CSS styling issues on Write the Docs conference pages.

## Common Issues and Solutions

### Double-Spaced List Items (News Links, etc.)

**Problem**: List items appear with excessive spacing (double-spaced) on conference home pages.

**Root Cause**: The `postlist` directive (from ablog) generates `<li>` elements containing `<p>` (paragraph) elements. Browser default paragraph margins create extra spacing between list items.

**Solution**: Add a CSS rule to remove paragraph margins within the affected list items.

#### Example Fix
For the Portland 2026 conference page, the fix was applied to `docs/_static/conf/scss/main-2026.scss`:

```scss
.news-block {
    background-color: #F7F7F7;

    .uk-container {
        padding: 48px 24px;

        // Remove paragraph margins in news list items to fix double-spacing
        .postlist .ablog-post p {
            margin: 0;
        }

        // ... rest of styles
    }
}
```

#### Steps to Apply Fix

1. **Identify the SCSS file**: Conference pages use year-specific SCSS files located in `docs/_static/conf/scss/`:
   - `main-2026.scss` for 2026 conferences
   - `main-2025.scss` for 2025 conferences
   - etc.

2. **Add the CSS rule**: Within the `.news-block .uk-container` section, add:
   ```scss
   .postlist .ablog-post p {
       margin: 0;
   }
   ```

3. **Compile SCSS to CSS**: 
   ```bash
   # Install sass if not already installed
   npm install -g sass
   
   # Compile the SCSS file (from docs/_static/conf/scss/ directory)
   cd docs/_static/conf/scss
   sass main-YYYY.scss ../css/main-YYYY.min.css --style=compressed --no-source-map
   ```

4. **Rebuild and verify**:
   ```bash
   cd docs
   make html
   ```

5. **View the changes**: Start a local server to view the rendered page:
   ```bash
   cd docs/_build/html
   python3 -m http.server 8888
   # Visit http://localhost:8888/conf/[city]/[year]/ in browser
   ```

## Conference Page Architecture

### Directory Structure
```
docs/
├── _static/
│   └── conf/
│       ├── scss/          # Source SCSS files
│       │   ├── main-2026.scss
│       │   ├── main-2025.scss
│       │   └── ...
│       └── css/           # Compiled CSS files
│           ├── main-2026.min.css
│           ├── main-2025.min.css
│           └── ...
└── conf/
    ├── portland/
    │   └── 2026/
    │       ├── index.rst  # Home page with postlist directive
    │       └── news/
    └── [other-cities]/
```

### Key Files for News Section
- **RST file**: `docs/conf/[city]/[year]/index.rst` - Contains the `postlist` directive
- **SCSS file**: `docs/_static/conf/scss/main-[year].scss` - Styles for the year
- **CSS file**: `docs/_static/conf/css/main-[year].min.css` - Compiled CSS (must be regenerated after SCSS changes)

### CSS Class Structure for News Section
```html
<div class="news-block">
  <div class="uk-container">
    <ul class="postlist">
      <li class="ablog-post">
        <p>...</p>  <!-- This <p> has default margins causing spacing issues -->
      </li>
    </ul>
  </div>
</div>
```

## Build System Notes

### Prerequisites
1. Python dependencies: Install from `requirements.txt`
2. SASS compiler: `npm install -g sass`

### Build Commands
```bash
# Full build
cd docs && make html

# Build with live reload (if sphinx-autobuild is installed)
cd docs && make livehtml
```

## Troubleshooting

### CSS Changes Not Appearing
- Ensure you compiled SCSS to CSS after making changes
- Clear browser cache or do a hard refresh (Ctrl+Shift+R)
- Verify the correct CSS file is being loaded in the HTML output

### Year-Specific Styling
- Each conference year typically has its own SCSS file
- Different years may have different layouts (e.g., 2026 uses simple list, earlier years use card-based layout)
- Always check the specific year's SCSS before applying fixes

## Related Issues
- Browser default margins on paragraph elements
- ablog postlist directive HTML structure
- Conference page template inheritance

## Reference
- Original fix: PR fixing Portland 2026 news links spacing
- Commit: aec44d8 (Fix double-spaced news links on Portland 2026 home page)
