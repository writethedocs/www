"""Drop Sphinx warnings we intentionally ignore.

Some of our shared jinja-included content is rendered verbatim into multiple
conference pages (e.g. Portland 2026 and Berlin 2026 both include the shared
``talk-recording-guide.rst``). When the hosting page is a MyST markdown file,
``{eval-rst}`` + ``{% include %}`` causes each section heading inside the
shared content to register a duplicate hyperlink target in Sphinx's std
domain, producing ``duplicate label <name>, other instance in ...`` warnings.

These shared sections are not referenced via cross-references — they only need
to render as headings on the page — so the duplicates are harmless. We drop
the specific warnings via a logging filter rather than mangling the shared
source, which also lets us enable ``-W`` in CI without false failures.
"""

from __future__ import annotations

import logging
import re


# Labels that originate from shared jinja-included content and can safely
# collide across pages. Keep this list as narrow as possible.
_SUPPRESSED_DUPLICATE_LABELS: frozenset[str] = frozenset(
    {
        # docs/code-of-conduct.rst, included by conf/*/2026/code-of-conduct.md
        "code of conduct",
        # docs/include/conf/portland/speaking-tips-2025.rst, included by
        # conf/{portland,berlin}/2026/speaker-info.md
        "presentation resources",
        "inclusive language",
        # docs/include/conf/virtual/talk-recording-guide.rst, included by
        # conf/{portland,berlin}/2026/talk-recording-guidelines.md
        "video requirements",
        "audio requirements",
        "recommended software",
        "tips & tricks",
    }
)

_DUPLICATE_LABEL_RE = re.compile(
    r"^duplicate label (?P<name>.+?), other instance in "
)


class DuplicateLabelFilter(logging.Filter):
    """Drop ``duplicate label ...`` warnings for known-safe labels."""

    def filter(self, record: logging.LogRecord) -> bool:
        match = _DUPLICATE_LABEL_RE.match(record.getMessage())
        if match and match.group("name") in _SUPPRESSED_DUPLICATE_LABELS:
            return False
        return True


def setup(app):
    # Attach the filter to the root sphinx logger so it covers all child
    # loggers (sphinx.domains.std emits the duplicate label warning, but the
    # exact logger name could change across Sphinx versions).
    logging.getLogger("sphinx").addFilter(DuplicateLabelFilter())
    return {"parallel_read_safe": True, "parallel_write_safe": True}
