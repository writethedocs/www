// Community pages: search from the header, and the newsletter signup.
//
// On Read the Docs, the search addon searches the whole site as you type, in
// a window over the page. When it's on, the header's search buttons and the
// menu's search box open that window, and its own "/" shortcut replaces ours.
// Elsewhere, like a local build, the search box submits to the Sphinx search
// page.
//
// On small screens the search box is at the top of the slide-in menu, so the
// header's search button opens the menu with the search box focused.

const menu = document.getElementById('community-menu');
const menuInput = document.getElementById('community-search-menu');
const drop = document.querySelector('.community-search-drop');
let readTheDocsSearch = null;  // the addon's search settings, once it's loaded

function useReadTheDocsAddons(data) {
  if (!data.addons?.search?.enabled) return;
  readTheDocsSearch = { hotkey: Boolean(data.addons.hotkeys?.search?.enabled) };
  // Read-only, so phones don't bring up a keyboard for a box you can't type in.
  menuInput.readOnly = true;
}

// The addons announce their settings once they've loaded, and keep them for
// scripts that load later.
document.addEventListener('readthedocs-addons-data-ready', (event) => {
  useReadTheDocsAddons(event.detail.data());
});
if (window.ReadTheDocsEventData) {
  useReadTheDocsAddons(window.ReadTheDocsEventData.data());
}

// Open search the best way this page can: the Read the Docs search window;
// on the search page, its own box; on wide screens, the box over the header
// menu; on small ones, the slide-in menu with its search box focused.
function showSearch() {
  if (readTheDocsSearch) {
    document.dispatchEvent(new CustomEvent('readthedocs-search-show'));
    return;
  }
  if (typeof UIkit === 'undefined') return;  // the menus need UIkit
  const pageInput = document.querySelector('#search-documentation ~ form input[name="q"]');
  if (pageInput) {
    pageInput.focus();
  } else if (drop.parentElement.offsetParent !== null) {
    UIkit.drop(drop).show();  // focuses the box: it has autofocus
  } else if (UIkit.offcanvas(menu).isToggled()) {
    menuInput.focus();
  } else {
    UIkit.util.once(menu, 'shown', () => menuInput.focus());
    UIkit.offcanvas(menu).show();
  }
}

// Wide screens: the search button opens the box over the menu items by
// itself, through UIkit. When the Read the Docs search is on, this runs
// first (in the capture phase) and opens that instead.
document.querySelector('.community-search-toggle').addEventListener('click', (event) => {
  if (!readTheDocsSearch) return;
  event.preventDefault();
  event.stopPropagation();
  showSearch();
}, true);

// Small screens: the search button next to the menu button.
document.querySelector('.community-search-open').addEventListener('click', showSearch);

// The menu's search box opens the Read the Docs search too. The menu closes
// first: while it's open it keeps focus inside itself, and the search window
// would fight it for focus.
function searchFromMenu(event) {
  if (!readTheDocsSearch) return;
  if (event.type === 'keydown' && event.key !== 'Enter' && event.key.length !== 1) return;
  event.preventDefault();
  UIkit.util.once(menu, 'hidden', showSearch);
  UIkit.offcanvas(menu).hide();
}
menuInput.addEventListener('click', searchFromMenu);
menuInput.addEventListener('keydown', searchFromMenu);

// Newsletter page: tick the event announcements for your region, going by
// your timezone. Each checkbox lists the timezone prefixes it covers in
// data-timezones. You can untick it before you subscribe.
const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
for (const box of document.querySelectorAll('input[data-timezones]')) {
  if (box.dataset.timezones.split(' ').some((zone) => timezone.startsWith(zone))) {
    box.checked = true;
  }
}

// Press "/" to search, as on most docs sites. Sphinx's built-in "/" shortcut
// is turned off in conf.py, because it can't open any of these.
document.addEventListener('keydown', (event) => {
  if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey) return;
  const target = event.target;
  if (target.isContentEditable || ['INPUT', 'TEXTAREA', 'SELECT'].includes(target.tagName)) return;
  if (readTheDocsSearch?.hotkey) return;  // the addon handles it
  event.preventDefault();
  showSearch();
});
