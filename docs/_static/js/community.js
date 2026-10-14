// Community pages: search from the header.
//
// On Read the Docs, the search addon searches the whole site as you type, in
// a window over the page. When it's on, the header's search buttons and the
// menu's search box open that window, and its own "/" shortcut replaces ours.
// Elsewhere, like a local build, the search box submits to the Sphinx search
// page.
//
// On small screens the search box is at the top of the slide-in menu, so the
// header's search button opens the menu with the search box focused.

let readTheDocsSearch = null;
const menuInput = document.getElementById('community-search-menu');

function useReadTheDocsAddons(data) {
  if (!data.addons?.search?.enabled) return;
  readTheDocsSearch = { hotkey: Boolean(data.addons.hotkeys?.search?.enabled) };
  if (menuInput) menuInput.readOnly = true;
}

// The addons announce their settings once they've loaded, and keep them for
// scripts that load later.
document.addEventListener('readthedocs-addons-data-ready', (event) => {
  useReadTheDocsAddons(event.detail.data());
});
if (window.ReadTheDocsEventData) {
  useReadTheDocsAddons(window.ReadTheDocsEventData.data());
}

function showReadTheDocsSearch() {
  document.dispatchEvent(new CustomEvent('readthedocs-search-show'));
}

// Wide screens: the search button opens the search box over the menu items,
// unless the Read the Docs search is on. Listening in the capture phase runs
// this before the box's own click handling, so it can stop it.
document.querySelectorAll('.community-search-toggle').forEach((toggle) => {
  toggle.addEventListener('click', (event) => {
    if (!readTheDocsSearch) return;
    event.preventDefault();
    event.stopPropagation();
    showReadTheDocsSearch();
  }, true);
});

document.querySelectorAll('.community-search-open').forEach((button) => {
  button.addEventListener('click', openMenuSearch);
});

// The menu's search box opens the Read the Docs search too. It's read-only
// then, so phones don't bring up a keyboard for a box you can't type in.
function openSearchFromMenu(event) {
  if (!readTheDocsSearch) return;
  if (event.type === 'keydown' && event.key !== 'Enter' && event.key.length !== 1) return;
  event.preventDefault();
  if (typeof UIkit === 'undefined') {
    showReadTheDocsSearch();
    return;
  }
  // Close the menu first: while it's open it keeps focus inside itself, and
  // the search window would fight it for focus.
  const menu = UIkit.offcanvas('#community-menu');
  UIkit.util.once(menu.$el, 'hidden', showReadTheDocsSearch);
  menu.hide();
}
if (menuInput) {
  menuInput.addEventListener('click', openSearchFromMenu);
  menuInput.addEventListener('keydown', openSearchFromMenu);
}

function openMenuSearch() {
  if (readTheDocsSearch) {
    showReadTheDocsSearch();
    return;
  }
  if (typeof UIkit === 'undefined') return;
  const menu = UIkit.offcanvas('#community-menu');
  if (menu.isToggled()) {
    menuInput.focus();
  } else {
    UIkit.util.once(menu.$el, 'shown', () => menuInput.focus());
    menu.show();
  }
}

// Press "/" to search, as on most docs sites. Opens the search box over the
// header menu on wide screens, or the slide-in menu on small ones. On the
// search page it focuses the page's own search box. Sphinx's built-in "/"
// shortcut is turned off in conf.py, because it can't open either of those.
document.addEventListener('keydown', (event) => {
  if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey) return;
  const target = event.target;
  if (target.isContentEditable || ['INPUT', 'TEXTAREA', 'SELECT'].includes(target.tagName)) return;
  if (readTheDocsSearch?.hotkey) return;  // the addon handles it
  if (typeof UIkit === 'undefined' && !readTheDocsSearch) return;

  event.preventDefault();
  const pageInput = document.querySelector('#search-documentation ~ form input[name="q"]');
  const drop = document.querySelector('.community-search-drop');
  if (readTheDocsSearch) {
    showReadTheDocsSearch();
  } else if (pageInput) {
    pageInput.focus();
  } else if (drop && drop.parentElement.offsetParent !== null) {
    UIkit.drop(drop).show();  // focuses the box: it has autofocus
  } else {
    openMenuSearch();
  }
});
