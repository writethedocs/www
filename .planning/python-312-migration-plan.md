# Python 3.12 Migration Plan

**Repository**: writethedocs.org
**Current Python**: 3.9.21 (EOL October 2025)
**Target Python**: 3.12.12
**Branch**: py-312-migration
**Estimated Total Time**: 12-16 hours over 1-2 weeks
**Date Created**: 2025-01-24

---

## Executive Summary

This plan migrates the Write the Docs website from Python 3.9 (EOL) to Python 3.12, based on intelligence from the Read the Docs codebase showing that:
- Python 3.11 was reverted as RTD's default due to production issues
- Python 3.12 is what RTD uses for their own infrastructure
- lxml has critical system library compatibility issues requiring careful handling

**Critical Success Factors**:
1. Use Python 3.12 (not 3.11) - RTD's proven choice
2. Pin lxml to 5.3.2 (RTD's exact version) - highest risk dependency
3. Comprehensive manual testing (no automated test suite exists)
4. Test on Windows and Linux (different build behaviors)

---

## Phase 1: Preparation & Research (2-3 hours)

**Objective**: Document baseline, review breaking changes, set up test environment

### Task 1.1: Document Current State (30 min)

- [ ] Run full local build and capture output
  ```bash
  cd docs
  make clean html 2>&1 | tee ../baseline-build.log
  ```
- [ ] Check for existing warnings/deprecations
- [ ] Take screenshots of key pages:
  - Homepage
  - Latest conference page (e.g., Portland 2025)
  - Blog archive
  - Video section
  - Guide section
- [ ] Document current build time
- [ ] Check disk space usage of `_build/`

**Deliverable**: `baseline-build.log`, screenshots in `.planning/screenshots/before/`

### Task 1.2: Review Breaking Changes (1 hour)

Read and summarize relevant changes from:
- [ ] Python 3.10 Release Notes: https://docs.python.org/3/whatsnew/3.10.html
- [ ] Python 3.11 Release Notes: https://docs.python.org/3/whatsnew/3.11.html
- [ ] Python 3.12 Release Notes: https://docs.python.org/3/whatsnew/3.12.html
- [ ] myst-parser CHANGELOG: 0.18.0 → 4.0.1
  - https://myst-parser.readthedocs.io/en/latest/develop/_changelog.html
- [ ] Werkzeug Migration Guide: 0.16.1 → 3.x
  - https://werkzeug.palletsprojects.com/en/stable/changes/
- [ ] lxml release notes: 4.8.0 → 5.3.2
  - https://lxml.de/changes-5.3.2.html

**Deliverable**: `breaking-changes-summary.md` in `.planning/`

### Task 1.3: Set Up Test Environment (1 hour)

- [ ] Install Python 3.12 locally
  ```bash
  # macOS (Homebrew)
  brew install python@3.12

  # Ubuntu/Debian
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt update
  sudo apt install python3.12 python3.12-venv
  ```
- [ ] Create test virtual environment
  ```bash
  python3.12 -m venv venv-py312-test
  source venv-py312-test/bin/activate
  python --version  # Verify 3.12.x
  ```
- [ ] Install current dependencies (baseline test)
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Attempt baseline build with Python 3.12
  ```bash
  cd docs
  make clean html
  ```
- [ ] Document any immediate failures

**Deliverable**: Notes on baseline compatibility, initial error log if any

---

## Phase 2: Configuration Updates (1-2 hours)

**Objective**: Update all Python version pins to 3.12

### Task 2.1: Update Version Control Files (15 min)

- [ ] Update `.python-version`
  ```diff
  -3.9.21
  +3.12.12
  ```

**Files**: `.python-version`

### Task 2.2: Update Read the Docs Config (15 min)

- [ ] Update `.readthedocs.yaml`
  ```diff
  build:
    os: ubuntu-22.04
    tools:
  -   python: "3.9"
  +   python: "3.12"
  ```

**Files**: `.readthedocs.yaml`

### Task 2.3: Update CI/CD Workflows (30 min)

- [ ] Update Ubuntu workflow
  ```diff
  # .github/workflows/ubuntu.yml
  -    - name: Set up Python 3.9
  +    - name: Set up Python 3.12
       uses: actions/setup-python@v5
       with:
  -      python-version: 3.9
  +      python-version: "3.12"
  ```

- [ ] Update Windows workflow
  ```diff
  # .github/workflows/windows.yml
  -    - name: Set up Python 3.9
  +    - name: Set up Python 3.12
       uses: actions/setup-python@v5
       with:
  -      python-version: 3.9
  +      python-version: "3.12"
  ```

**Files**: `.github/workflows/ubuntu.yml`, `.github/workflows/windows.yml`

### Task 2.4: Commit Configuration Changes (15 min)

- [ ] Review all changes
  ```bash
  git diff
  git status
  ```
- [ ] Commit configuration updates
  ```bash
  git add .python-version .readthedocs.yaml .github/workflows/
  git commit -m "Update Python version to 3.12 in all configs

  - Update .python-version: 3.9.21 → 3.12.12
  - Update .readthedocs.yaml: python 3.9 → 3.12
  - Update CI workflows (ubuntu.yml, windows.yml) to Python 3.12

  Related to Python 3.9 EOL (October 2025) and security updates.
  Based on Read the Docs infrastructure best practices."
  ```

**Deliverable**: Configuration files updated and committed

---

## Phase 3: Dependency Updates (2-3 hours)

**Objective**: Update requirements.txt with compatible versions

### Task 3.1: Backup Current Requirements (5 min)

- [ ] Create backup
  ```bash
  cp requirements.txt requirements.txt.py39.bak
  git add requirements.txt.py39.bak
  git commit -m "Backup Python 3.9 requirements before migration"
  ```

### Task 3.2: Update Critical Dependencies (1 hour)

Read current `requirements.txt` and update systematically:

**Priority 1 - Critical System Dependencies (HIGH RISK)**:
- [ ] lxml: `4.8.0` → `5.3.2` (RTD's pinned version)
- [ ] Add xmlsec pin: `xmlsec==1.3.14` (required with lxml upgrade)

**Priority 2 - Python 3.12 Compatibility**:
- [ ] myst-parser: `0.18.0` → `4.0.1` (RTD's version)

**Priority 3 - Security Updates**:
- [ ] Werkzeug: `0.16.1` → `3.1.3` (fix CVEs)
- [ ] ablog: `0.10.31` → `0.11.11` (replace yanked version)

**Priority 4 - General Updates**:
- [ ] docutils: `0.17.1` → `0.21.2` (stay compatible with Sphinx 5.x)
- [ ] sphinx-autobuild: `2021.3.14` → `2024.10.3` (maintenance updates)

**Priority 5 - Removals**:
- [ ] Remove `pathlib==1.0.1` (stdlib since Python 3.4)

**Keep Stable**:
- [ ] Sphinx: Keep at `5.3.0` (actively tested by RTD with Python 3.12)
- [ ] PyYAML: Keep at `6.0.2` (stable)
- [ ] matplotlib: Keep at `3.9.4` (recent, compatible)

Create updated `requirements.txt`:
```python
# Core Sphinx
Sphinx==5.3.0
docutils==0.21.2
sphinx_autobuild==2024.10.3

# Markup parsers
myst-parser==4.0.1

# Extensions
ablog==0.11.11
sphinxcontrib.datatemplates==0.11.0
sphinxemoji==0.3.1
sphinx-notfound-page==1.1.0
sphinxext-opengraph==0.9.1

# System dependencies (CRITICAL)
lxml==5.3.2
xmlsec==1.3.14

# Data processing
PyYAML==6.0.2
pytz==2024.2
yamale==4.0.4
yamllint==1.26.3
ruamel.yaml==0.18.14

# Utilities
csvkit==2.1.0
meetup-api==0.1.1
urllib3[secure]==2.2.3
markdown==3.7
Werkzeug==3.1.3

# Visualization
matplotlib==3.9.4
```

### Task 3.3: Test Dependency Installation (30 min)

- [ ] Activate test environment
  ```bash
  source venv-py312-test/bin/activate
  ```
- [ ] Install updated dependencies
  ```bash
  pip install --upgrade pip setuptools wheel
  pip install -r requirements.txt 2>&1 | tee .planning/pip-install.log
  ```
- [ ] Check for compilation errors (especially lxml)
- [ ] Verify all packages installed
  ```bash
  pip list > .planning/installed-packages.txt
  pip check
  ```

### Task 3.4: Commit Dependency Updates (15 min)

- [ ] Review changes
  ```bash
  git diff requirements.txt
  ```
- [ ] Commit requirements.txt
  ```bash
  git add requirements.txt
  git commit -m "Update dependencies for Python 3.12 compatibility

  Critical updates:
  - lxml: 4.8.0 → 5.3.2 (RTD's pinned version, fixes CVEs)
  - xmlsec: Add 1.3.14 pin (required with lxml upgrade)
  - myst-parser: 0.18.0 → 4.0.1 (Python 3.12 support)
  - Werkzeug: 0.16.1 → 3.1.3 (fix multiple CVEs)
  - ablog: 0.10.31 → 0.11.11 (replace yanked version)
  - docutils: 0.17.1 → 0.21.2 (compatibility update)
  - sphinx-autobuild: 2021.3.14 → 2024.10.3 (maintenance)

  Removed:
  - pathlib: stdlib since Python 3.4

  Kept stable:
  - Sphinx: 5.3.0 (actively tested by RTD with Python 3.12)"
  ```

**Deliverable**: Updated requirements.txt, installation log, package list

---

## Phase 4: Code Cleanup (1-2 hours)

**Objective**: Remove Python 2 compatibility code

### Task 4.1: Remove `from __future__` Imports (30 min)

Edit 5 files to remove unnecessary imports:

1. **docs/_ext/core.py**
   ```diff
   -from __future__ import print_function
   ```

2. **docs/_ext/videos.py**
   ```diff
   -from __future__ import print_function
   ```

3. **docs/_ext/atom_absolute.py**
   ```diff
   -from __future__ import unicode_literals
   ```

4. **docs/_scripts/make-email.py**
   ```diff
   -from __future__ import print_function
   ```

5. **docs/_scripts/export_json.py**
   ```diff
   -from __future__ import print_function
   ```

**Files**: 5 files in `docs/_ext/` and `docs/_scripts/`

### Task 4.2: Replace `six` Imports (15 min)

- [ ] Edit `docs/_ext/atom_absolute.py`
  ```diff
  -from six.moves.urllib.parse import urljoin
  +from urllib.parse import urljoin
  ```
- [ ] Verify `six` is not in requirements.txt (it's not, likely transitive)
- [ ] Check if any other files import `six`
  ```bash
  grep -r "from six" docs/
  grep -r "import six" docs/
  ```

**Files**: `docs/_ext/atom_absolute.py`

### Task 4.3: Simplify pathlib Imports (15 min)

- [ ] Edit `docs/_ext/core.py`
  ```diff
  -try:
  -    from pathlib import PurePath
  -except ImportError:
  -    from pathlib2 import PurePath
  +from pathlib import PurePath
  ```

**Files**: `docs/_ext/core.py`

### Task 4.4: Remove builtins Import (15 min)

- [ ] Edit `docs/_ext/videos.py`
  ```diff
  -from builtins import str
  ```
  (Just delete the line - `str` is a builtin in Python 3)

**Files**: `docs/_ext/videos.py`

### Task 4.5: Commit Code Cleanup (15 min)

- [ ] Review all changes
  ```bash
  git diff docs/_ext/ docs/_scripts/
  ```
- [ ] Run quick syntax check
  ```bash
  python3.12 -m py_compile docs/_ext/*.py
  python3.12 -m py_compile docs/_scripts/*.py
  ```
- [ ] Commit changes
  ```bash
  git add docs/_ext/ docs/_scripts/
  git commit -m "Remove Python 2 compatibility code for Python 3.12

  - Remove 'from __future__' imports (5 files)
  - Replace 'six.moves.urllib.parse' with 'urllib.parse'
  - Simplify pathlib imports (remove pathlib2 fallback)
  - Remove unnecessary 'from builtins import str'

  All these compatibility shims are unnecessary for Python 3.12."
  ```

**Deliverable**: Cleaned up Python code, committed

---

## Phase 5: Local Testing - Basic Build (2-3 hours)

**Objective**: Verify site builds successfully with Python 3.12

### Task 5.1: Clean Build Test (30 min)

- [ ] Activate Python 3.12 environment
  ```bash
  source venv-py312-test/bin/activate
  python --version  # Confirm 3.12.x
  ```
- [ ] Clean previous build
  ```bash
  cd docs
  make clean
  ```
- [ ] Build documentation
  ```bash
  make html 2>&1 | tee ../.planning/build-py312-clean.log
  ```
- [ ] Check exit code: `echo $?` (should be 0)
- [ ] Review output for:
  - Build errors
  - Deprecation warnings
  - Extension import failures
  - Theme rendering issues
- [ ] Note build time (compare to baseline)

**Success Criteria**: Build completes with exit code 0

**Deliverable**: `build-py312-clean.log`

### Task 5.2: Live Preview Test (30 min)

- [ ] Start live preview server
  ```bash
  cd docs
  make livehtml
  ```
- [ ] Access http://127.0.0.1:8888
- [ ] Check for server errors in terminal
- [ ] Test auto-rebuild: edit a file and verify rebuild triggers
- [ ] Stop server (Ctrl+C)

**Success Criteria**: Server starts, pages load, auto-rebuild works

### Task 5.3: Manual Page Review (1 hour)

Visit and inspect key pages in browser:

**Homepage** (docs/index.rst):
- [ ] Page loads without errors
- [ ] Navigation menu renders
- [ ] Images load
- [ ] Links work

**Latest Conference** (e.g., docs/conf/portland/2025/):
- [ ] Conference page loads
- [ ] Sponsor logos display
- [ ] Schedule renders (if flaghasschedule=true)
- [ ] Speaker listings (if flagspeakersannounced=true)
- [ ] Check date/time formatting

**Blog Archive** (docs/blog/archive/):
- [ ] Blog index loads
- [ ] Post listings display
- [ ] Tags work
- [ ] Categories work
- [ ] Individual blog posts load

**Guide Section** (docs/guide/):
- [ ] Guide index loads
- [ ] Table of contents renders
- [ ] Code examples display correctly
- [ ] Admonitions (notes, warnings) render

**Search**:
- [ ] Search page accessible
- [ ] Try a test search query

**Atom Feeds** (affected by Werkzeug update):
- [ ] Access /blog/atom.xml
- [ ] Verify valid XML (check in browser or validator)
- [ ] Confirm entries present

**Deliverable**: Checklist completed, screenshots of key pages in `.planning/screenshots/after/`

### Task 5.4: Check for Deprecation Warnings (30 min)

- [ ] Review build log for deprecation warnings
  ```bash
  grep -i "deprecat" .planning/build-py312-clean.log
  grep -i "warning" .planning/build-py312-clean.log
  ```
- [ ] Document any warnings found
- [ ] Research if warnings are critical or can be deferred
- [ ] Create issues for warnings that need addressing

**Deliverable**: `deprecation-warnings.md` in `.planning/`

---

## Phase 6: Extended Testing - Videos & Conference Data (2-3 hours)

**Objective**: Test complex features (video generation, conference schedules)

### Task 6.1: Video Build Test (1.5 hours)

**Warning**: This is slow (~100+ pages)

- [ ] Enable video build
  ```bash
  cd docs
  export BUILD_VIDEOS=True
  make clean html 2>&1 | tee ../.planning/build-py312-videos.log
  ```
- [ ] Monitor for errors during video generation
- [ ] Check video pages created in `_build/html/conf/*/videos/`
- [ ] Verify video pages for recent conference (2024/2025)
- [ ] Spot-check 5-10 video detail pages:
  - YouTube embed works
  - Speaker info displays
  - Talk abstract renders
  - Links to schedule work

**Success Criteria**: Videos build without errors, pages display correctly

**Deliverable**: `build-py312-videos.log`, notes on video functionality

### Task 6.2: Conference Schedule Testing (1 hour)

Test timezone handling and date formatting:

- [ ] Find a conference with multi-timezone schedule (check config YAML for `tz2`)
- [ ] Load schedule page
- [ ] Verify times display in both timezones (if applicable)
- [ ] Check date formatting (12h vs 24h based on config)
- [ ] Verify schedule items align with YAML data
- [ ] Test break times display correctly

**Files to check**:
- `docs/_ext/core.py` (lines 119-161: timezone logic)
- Conference schedule pages

**Success Criteria**: Schedules render accurately with correct timezone conversions

### Task 6.3: YAML Data Processing Test (30 min)

- [ ] Run YAML validation
  ```bash
  cd docs/_scripts
  ./validate-yaml.sh 2>&1 | tee ../../.planning/yaml-validation.log
  ```
- [ ] Verify all YAML files pass schema validation
- [ ] Check that conference data loads correctly in pages

**Success Criteria**: All YAML validates successfully

**Deliverable**: `yaml-validation.log`

---

## Phase 7: Cross-Platform Testing (1-2 hours)

**Objective**: Verify Windows compatibility

### Task 7.1: Review Windows Monkeypatch (15 min)

- [ ] Read `docs/conf.py` Windows monkeypatch (search for "monkeypatch")
- [ ] Understand what it's fixing (UTF-8 encoding for datatemplates)
- [ ] Verify the monkeypatch is still present
- [ ] Check if Python 3.12 UTF-8 mode affects this (PEP 686)

**Research**: Python 3.12 defaults to UTF-8 mode on Windows (PEP 686)
- This may make the monkeypatch unnecessary
- Keep it for backward compatibility unless it causes issues

### Task 7.2: Local Windows Testing (Optional, 1 hour)

**If you have access to Windows machine**:

- [ ] Install Python 3.12 on Windows
- [ ] Clone repository
- [ ] Create virtual environment
  ```powershell
  python -m venv venv-py312-test
  .\venv-py312-test\Scripts\Activate.ps1
  ```
- [ ] Install dependencies
  ```powershell
  pip install -r requirements.txt
  ```
- [ ] Build documentation
  ```powershell
  cd docs
  .\make.bat html
  ```
- [ ] Check for encoding errors
- [ ] Document results

**If no Windows access**: Rely on CI testing (next phase)

**Deliverable**: Notes on Windows compatibility or note to test via CI

---

## Phase 8: CI/CD Testing (1 hour)

**Objective**: Verify GitHub Actions builds pass

### Task 8.1: Push Branch to GitHub (15 min)

- [ ] Review all commits
  ```bash
  git log --oneline origin/main..HEAD
  ```
- [ ] Push branch
  ```bash
  git push -u origin py-312-migration
  ```

### Task 8.2: Monitor CI Builds (30 min)

- [ ] Navigate to GitHub Actions
- [ ] Watch Ubuntu build workflow
  - Check Python 3.12 installation
  - Monitor build output
  - Verify html-proofer passes
  - Download HTML artifact if build succeeds
- [ ] Watch Windows build workflow
  - Check for encoding errors
  - Monitor for Windows-specific failures
  - Verify build completes

**Success Criteria**: Both Ubuntu and Windows builds pass

### Task 8.3: Review CI Artifacts (15 min)

- [ ] Download Ubuntu build artifact (HTML)
- [ ] Unzip and spot-check pages locally
- [ ] Compare to local build output
- [ ] Document any differences

**Deliverable**: CI build success confirmation, artifact review notes

---

## Phase 9: Read the Docs Preview (1-2 hours)

**Objective**: Test on actual RTD infrastructure

### Task 9.1: Create Pull Request (15 min)

- [ ] Create PR on GitHub
  ```
  Title: Upgrade to Python 3.12 for EOL and security updates

  Description:
  ## Summary
  Upgrades Python from 3.9 (EOL October 2025) to 3.12 based on Read the Docs infrastructure best practices.

  ## Changes
  - Python: 3.9.21 → 3.12.12
  - lxml: 4.8.0 → 5.3.2 (RTD's pinned version, fixes CVEs)
  - myst-parser: 0.18.0 → 4.0.1 (Python 3.12 compatibility)
  - Werkzeug: 0.16.1 → 3.1.3 (fixes CVE-2023-23934, CVE-2023-25577, CVE-2024-49766, CVE-2024-49767, CVE-2024-34069)
  - ablog: 0.10.31 → 0.11.11 (replace yanked version)
  - Remove Python 2 compatibility code

  ## Testing
  - ✅ Local build successful (Linux/macOS)
  - ✅ Video generation tested
  - ✅ Conference schedules validated
  - ✅ YAML validation passes
  - ✅ CI builds pass (Ubuntu + Windows)
  - ⏳ RTD preview pending

  ## Rationale
  Based on analysis of Read the Docs infrastructure:
  - Python 3.11 was reverted as RTD default due to production issues
  - Python 3.12 is what RTD uses for their own infrastructure
  - lxml 5.3.2 is RTD's pinned version to avoid system library conflicts

  ## Rollback Plan
  If issues occur, revert to Python 3.9 by merging main into this branch.
  ```
- [ ] Label PR: `infrastructure`, `dependencies`
- [ ] Mark as draft if not ready for final review

### Task 9.2: Monitor RTD Build (30 min)

- [ ] Check RTD build status on PR (should auto-trigger)
- [ ] Click "View docs" link when build completes
- [ ] Review RTD build log:
  - Python installation time
  - lxml compilation output
  - Extension imports
  - Build warnings/errors
- [ ] Document build time on RTD vs local

**Success Criteria**: RTD build succeeds, preview site loads

### Task 9.3: RTD Preview Site Review (45 min)

**Systematically test preview site** (similar to local testing):

- [ ] Homepage
- [ ] Latest conference page
- [ ] Blog archive and individual posts
- [ ] Video archive (if built)
- [ ] Guide section
- [ ] Search functionality
- [ ] Atom/RSS feeds

**Compare to production** (www.writethedocs.org):
- [ ] Visual comparison (layout, styling)
- [ ] Functionality comparison
- [ ] Check for missing assets
- [ ] Verify no broken internal links

**Deliverable**: RTD preview approval, comparison notes

---

## Phase 10: Final Validation & Documentation (1-2 hours)

**Objective**: Final checks and documentation

### Task 10.1: Link Checking (30 min)

**If you have Ruby/htmlproofer installed**:

- [ ] Install Ruby dependencies
  ```bash
  bundle install
  ```
- [ ] Run htmlproofer on local build
  ```bash
  cd docs
  bundle exec htmlproofer --ignore-files "/404/,/2013/,/2014/,/2015/,/2016/,/2017/,/search\/index.html/,/archive\/tag\/index/" \
    --allow-hash-href=true --enforce-https=false --ignore-missing-alt=true --disable-external=true _build/html \
    2>&1 | tee ../.planning/htmlproofer.log
  ```
- [ ] Review broken links
- [ ] Fix any internal broken links found

**Success Criteria**: No new broken internal links (external links may vary)

**Deliverable**: `htmlproofer.log`

### Task 10.2: Vale Linting (30 min)

**If you have Vale installed**:

- [ ] Run Vale on guide content
  ```bash
  vale --config=vale/guide.ini docs/guide/ > .planning/vale-guide.log
  ```
- [ ] Run Vale on general content
  ```bash
  vale --config=vale/vale.ini docs/ > .planning/vale-general.log
  ```
- [ ] Compare to baseline (should be similar)
- [ ] No need to fix prose issues (not related to Python upgrade)

**Deliverable**: Vale logs showing no regression

### Task 10.3: Update CLAUDE.md (15 min)

- [ ] Add Python 3.12 note to CLAUDE.md
  ```markdown
  ## Python Version

  This project uses **Python 3.12** (as of 2025).

  - See `.python-version` for exact version
  - Python 3.9 was EOL October 2025
  - Python 3.12 chosen based on RTD infrastructure (not 3.11 due to known issues)
  - Key pinned dependencies: lxml==5.3.2, xmlsec==1.3.14 (RTD's versions)
  ```

**Files**: `CLAUDE.md`

### Task 10.4: Create Migration Summary (15 min)

- [ ] Create `.planning/migration-summary.md` with:
  - What was changed
  - What was tested
  - Known issues (if any)
  - Recommended monitoring post-deploy
  - Rollback procedure

**Deliverable**: `migration-summary.md`

---

## Phase 11: Deployment (30 min - 1 hour)

**Objective**: Merge to main and monitor production

### Task 11.1: Pre-Merge Checklist (15 min)

Verify all completed:
- [ ] All config files updated
- [ ] requirements.txt updated
- [ ] Python 2 code removed
- [ ] Local build passes
- [ ] Video build passes
- [ ] YAML validation passes
- [ ] CI builds pass (Ubuntu + Windows)
- [ ] RTD preview looks good
- [ ] No new deprecation warnings
- [ ] Documentation updated

### Task 11.2: Merge to Main (15 min)

- [ ] Update PR from draft to ready for review (if draft)
- [ ] Request review from maintainer (if required)
- [ ] Address any review comments
- [ ] Squash and merge (or regular merge per repo conventions)
  ```
  Title: Upgrade to Python 3.12 for EOL and security updates

  Merged from py-312-migration branch.
  Tested on local, CI, and RTD preview.
  ```

### Task 11.3: Monitor Production Build (30 min)

- [ ] Watch RTD production build
- [ ] Check build log for errors
- [ ] Verify www.writethedocs.org loads
- [ ] Spot-check key pages:
  - [ ] Homepage
  - [ ] Latest conference
  - [ ] Blog
  - [ ] Guide
- [ ] Monitor for error reports (if any issue tracker/Slack)

**Success Criteria**: Production site builds and loads normally

### Task 11.4: Announce (Optional, 15 min)

If there's a team communication channel:
- [ ] Announce Python upgrade completion
- [ ] Note any expected behavior changes (should be none)
- [ ] Provide contact for issues

**Deliverable**: Successful production deployment

---

## Rollback Procedure

**If production issues occur:**

### Immediate Rollback (5-10 min)

1. Create revert branch
   ```bash
   git checkout main
   git pull
   git checkout -b revert-py312
   ```

2. Revert merge commit
   ```bash
   git revert -m 1 <merge-commit-hash>
   ```

3. Push and create emergency PR
   ```bash
   git push -u origin revert-py312
   # Create PR, get approval, merge immediately
   ```

4. RTD will auto-deploy revert

### Investigation

5. Capture production logs from RTD
6. Reproduce issue locally
7. Fix in py-312-migration branch
8. Retry deployment

---

## Success Metrics

### Build Metrics
- [ ] Build completes successfully (exit code 0)
- [ ] Build time comparable to Python 3.9 baseline (±20%)
- [ ] No new errors or warnings
- [ ] All pages generate correctly

### Functionality Metrics
- [ ] Homepage loads
- [ ] Conference pages render with correct data
- [ ] Blog posts display
- [ ] Video archive works (if applicable)
- [ ] Search functions
- [ ] Feeds validate (atom.xml)

### Quality Metrics
- [ ] No new broken internal links
- [ ] Vale linting shows no regression
- [ ] YAML validation passes
- [ ] CI/CD passes on all platforms

### Security Metrics
- [ ] CVEs resolved:
  - ✅ Werkzeug CVE-2023-23934
  - ✅ Werkzeug CVE-2023-25577
  - ✅ Werkzeug CVE-2024-49766
  - ✅ Werkzeug CVE-2024-49767
  - ✅ Werkzeug CVE-2024-34069
  - ✅ lxml CVE-2022-2309
  - ✅ lxml CVE-2021-43818
- [ ] No new security warnings from pip-audit or safety

---

## Known Issues & Workarounds

### Issue 1: lxml Compilation on Some Systems
**Symptom**: lxml fails to compile during pip install
**Workaround**: Install system dependencies first
```bash
# macOS
brew install libxml2 libxslt

# Ubuntu/Debian
sudo apt-get install libxml2-dev libxslt1-dev

# Then retry pip install
```

### Issue 2: Video Build Timeout
**Symptom**: Video build takes >10 minutes
**Expected**: This is normal, videos generate ~100+ pages
**Workaround**: Skip video build for development (`BUILD_VIDEOS=False`)

### Issue 3: Windows UTF-8 Encoding
**Symptom**: Encoding errors on Windows
**Note**: Monkeypatch in conf.py should handle this
**Workaround**: If issues persist, verify Python 3.12 UTF-8 mode enabled

---

## Post-Deployment Monitoring (First 48 Hours)

### Automated Monitoring
- [ ] Watch RTD build logs for errors
- [ ] Check for broken link reports (if automated)
- [ ] Monitor any error tracking service

### Manual Checks
- [ ] Day 1: Check homepage, latest conference, blog
- [ ] Day 2: Check search, feeds, older conference pages
- [ ] Day 3: Final verification, close monitoring

### Community Feedback
- [ ] Watch for issue reports
- [ ] Monitor social media mentions
- [ ] Check any support channels

---

## Lessons Learned (To Be Filled Post-Migration)

### What Went Well
-

### What Could Be Improved
-

### Unexpected Issues
-

### Time Variance
- Estimated: 12-16 hours
- Actual: _____ hours
- Variance: _____

---

## References

- Python 3.12 Release Notes: https://docs.python.org/3/whatsnew/3.12.html
- Read the Docs Build Configuration: https://docs.readthedocs.io/en/stable/config-file/v2.html
- Sphinx Documentation: https://www.sphinx-doc.org/
- myst-parser Changelog: https://myst-parser.readthedocs.io/en/latest/develop/_changelog.html
- Werkzeug Changes: https://werkzeug.palletsprojects.com/en/stable/changes/
- lxml Documentation: https://lxml.de/

---

## Contact

**Migration Lead**: [Your Name]
**Date Started**: [To be filled]
**Date Completed**: [To be filled]
**Status**: Planning Phase

---

**End of Migration Plan**
