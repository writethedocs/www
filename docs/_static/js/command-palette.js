// Command palette: Cmd+K / Ctrl+K opens a modal listing the current page's
// headings so visitors can jump straight to a section.
(function () {
    "use strict";

    var overlay = null;
    var input = null;
    var list = null;
    var items = [];      // {el, text, level, id, anchorText}
    var matches = [];    // currently visible matches
    var activeIndex = 0;

    function collectHeadings() {
        var headings = document.querySelectorAll(
            ".body h1[id], .body h2[id], .body h3[id], .body h4[id], .body h5[id], .body h6[id]"
        );
        var collected = [];
        for (var i = 0; i < headings.length; i++) {
            var h = headings[i];
            // Strip Sphinx's pilcrow permalink so the heading text is clean.
            var clone = h.cloneNode(true);
            var perma = clone.querySelector("a.headerlink");
            if (perma) {
                perma.parentNode.removeChild(perma);
            }
            var text = clone.textContent.replace(/\s+/g, " ").trim();
            if (!text) continue;
            collected.push({
                el: h,
                text: text,
                level: parseInt(h.tagName.substring(1), 10),
                id: h.id
            });
        }
        return collected;
    }

    function buildOverlay() {
        overlay = document.createElement("div");
        overlay.className = "wtd-cmdk-overlay";
        overlay.setAttribute("role", "dialog");
        overlay.setAttribute("aria-modal", "true");
        overlay.setAttribute("aria-label", "Jump to section");
        overlay.hidden = true;

        var panel = document.createElement("div");
        panel.className = "wtd-cmdk-panel";

        input = document.createElement("input");
        input.type = "text";
        input.className = "wtd-cmdk-input";
        input.setAttribute("placeholder", "Jump to a section on this page…");
        input.setAttribute("aria-label", "Filter headings");
        input.setAttribute("autocomplete", "off");
        input.setAttribute("spellcheck", "false");

        list = document.createElement("ul");
        list.className = "wtd-cmdk-list";
        list.setAttribute("role", "listbox");

        var hint = document.createElement("div");
        hint.className = "wtd-cmdk-hint";
        hint.innerHTML =
            '<span><kbd>↑</kbd><kbd>↓</kbd> navigate</span>' +
            '<span><kbd>↵</kbd> jump</span>' +
            '<span><kbd>Esc</kbd> close</span>';

        panel.appendChild(input);
        panel.appendChild(list);
        panel.appendChild(hint);
        overlay.appendChild(panel);

        overlay.addEventListener("click", function (e) {
            if (e.target === overlay) close();
        });

        input.addEventListener("input", function () {
            render(input.value);
        });

        input.addEventListener("keydown", function (e) {
            if (e.key === "ArrowDown") {
                e.preventDefault();
                move(1);
            } else if (e.key === "ArrowUp") {
                e.preventDefault();
                move(-1);
            } else if (e.key === "Enter") {
                e.preventDefault();
                select(activeIndex);
            } else if (e.key === "Escape") {
                e.preventDefault();
                close();
            }
        });

        document.body.appendChild(overlay);
    }

    function matchScore(text, query) {
        // Returns -1 for no match, otherwise a lower score = better match.
        // Prefer prefix matches, then word-start matches, then substring.
        var lower = text.toLowerCase();
        var q = query.toLowerCase();
        if (!q) return 0;
        if (lower.indexOf(q) === 0) return 0;
        if (lower.indexOf(" " + q) !== -1) return 1;
        var idx = lower.indexOf(q);
        if (idx !== -1) return 2 + idx / 100;
        // Loose subsequence match for fuzzy typing.
        var ti = 0;
        for (var i = 0; i < q.length; i++) {
            ti = lower.indexOf(q.charAt(i), ti);
            if (ti === -1) return -1;
            ti++;
        }
        return 100;
    }

    function render(query) {
        list.innerHTML = "";
        query = (query || "").trim();
        var scored = [];
        for (var i = 0; i < items.length; i++) {
            var s = matchScore(items[i].text, query);
            if (s !== -1) scored.push({ item: items[i], score: s });
        }
        if (query) {
            scored.sort(function (a, b) { return a.score - b.score; });
        }
        matches = scored.map(function (x) { return x.item; });
        activeIndex = 0;

        if (matches.length === 0) {
            var empty = document.createElement("li");
            empty.className = "wtd-cmdk-empty";
            empty.textContent = "No headings match.";
            list.appendChild(empty);
            return;
        }

        for (var j = 0; j < matches.length; j++) {
            var m = matches[j];
            var li = document.createElement("li");
            li.className = "wtd-cmdk-item wtd-cmdk-level-" + m.level;
            li.setAttribute("role", "option");
            li.dataset.index = String(j);

            var level = document.createElement("span");
            level.className = "wtd-cmdk-level";
            level.textContent = "H" + m.level;

            var label = document.createElement("span");
            label.className = "wtd-cmdk-label";
            label.textContent = m.text;

            li.appendChild(level);
            li.appendChild(label);

            li.addEventListener("mouseenter", function (e) {
                setActive(parseInt(e.currentTarget.dataset.index, 10));
            });
            li.addEventListener("click", function (e) {
                select(parseInt(e.currentTarget.dataset.index, 10));
            });
            list.appendChild(li);
        }
        setActive(0);
    }

    function setActive(idx) {
        if (matches.length === 0) return;
        if (idx < 0) idx = matches.length - 1;
        if (idx >= matches.length) idx = 0;
        activeIndex = idx;
        var children = list.querySelectorAll(".wtd-cmdk-item");
        for (var i = 0; i < children.length; i++) {
            if (i === idx) {
                children[i].classList.add("is-active");
                children[i].setAttribute("aria-selected", "true");
                scrollIntoViewIfNeeded(children[i]);
            } else {
                children[i].classList.remove("is-active");
                children[i].setAttribute("aria-selected", "false");
            }
        }
    }

    function scrollIntoViewIfNeeded(el) {
        var parent = el.parentNode;
        var top = el.offsetTop;
        var bottom = top + el.offsetHeight;
        if (top < parent.scrollTop) {
            parent.scrollTop = top;
        } else if (bottom > parent.scrollTop + parent.clientHeight) {
            parent.scrollTop = bottom - parent.clientHeight;
        }
    }

    function move(delta) {
        setActive(activeIndex + delta);
    }

    function select(idx) {
        var target = matches[idx];
        if (!target) return;
        close();
        // Update the URL and scroll to the heading.
        history.pushState(null, "", "#" + target.id);
        target.el.scrollIntoView({ behavior: "smooth", block: "start" });
        // Briefly focus the heading for screen readers.
        var prevTabIndex = target.el.getAttribute("tabindex");
        target.el.setAttribute("tabindex", "-1");
        target.el.focus({ preventScroll: true });
        if (prevTabIndex === null) {
            setTimeout(function () { target.el.removeAttribute("tabindex"); }, 1000);
        }
    }

    function open() {
        if (!overlay) buildOverlay();
        items = collectHeadings();
        if (items.length === 0) return;
        overlay.hidden = false;
        document.documentElement.classList.add("wtd-cmdk-open");
        input.value = "";
        render("");
        // Focus on the next tick so the keystroke that opened us isn't typed in.
        setTimeout(function () { input.focus(); }, 0);
    }

    function close() {
        if (!overlay || overlay.hidden) return;
        overlay.hidden = true;
        document.documentElement.classList.remove("wtd-cmdk-open");
    }

    function isTypingTarget(el) {
        if (!el) return false;
        var tag = el.tagName;
        return tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || el.isContentEditable;
    }

    document.addEventListener("keydown", function (e) {
        if ((e.key === "k" || e.key === "K") && (e.metaKey || e.ctrlKey)) {
            // Don't hijack browser search or other text inputs.
            e.preventDefault();
            if (overlay && !overlay.hidden) {
                close();
            } else {
                open();
            }
            return;
        }
        if (e.key === "/" && !isTypingTarget(document.activeElement)) {
            // Slash is a common shortcut on doc sites — bind it too.
            e.preventDefault();
            open();
        }
    });
})();
