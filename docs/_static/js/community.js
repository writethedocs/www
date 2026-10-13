// Community pages: search from the header.
//
// On small screens the search box is at the top of the slide-in menu, so the
// header's search button opens the menu with the search box focused.
document.querySelectorAll('.community-search-open').forEach((button) => {
  button.addEventListener('click', openMenuSearch);
});

function openMenuSearch() {
  if (typeof UIkit === 'undefined') return;
  const input = document.getElementById('community-search-menu');
  UIkit.util.once(document.getElementById('community-menu'), 'shown', () => input.focus());
  UIkit.offcanvas('#community-menu').show();
}

// Press "/" to search, as on most docs sites. Opens the search box over the
// header menu on wide screens, or the slide-in menu on small ones. On the
// search page it focuses the page's own search box. Sphinx's built-in "/"
// shortcut is turned off in conf.py, because it can't open either of those.
document.addEventListener('keydown', (event) => {
  if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey) return;
  const target = event.target;
  if (target.isContentEditable || ['INPUT', 'TEXTAREA', 'SELECT'].includes(target.tagName)) return;
  if (typeof UIkit === 'undefined') return;

  event.preventDefault();
  const pageInput = document.querySelector('#search-documentation ~ form input[name="q"]');
  const drop = document.querySelector('.community-search-drop');
  if (pageInput) {
    pageInput.focus();
  } else if (drop && drop.parentElement.offsetParent !== null) {
    UIkit.drop(drop).show();  // focuses the box: it has autofocus
  } else {
    openMenuSearch();
  }
});
