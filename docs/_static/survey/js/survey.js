document.addEventListener("DOMContentLoaded", function() {

  // Activate the tab containing a hash target so internal links into a non-default tab open it
  function activateTabForHash(hash) {
    if (!hash || hash.length < 2) return false;
    var target;
    try { target = document.querySelector(hash); } catch (e) { return false; }
    if (!target) return false;
    var tabContent = target.closest('.tab__content');
    if (!tabContent) return false;
    var tabWrap = tabContent.closest('.tab-wrap');
    if (!tabWrap) return false;
    var contents = tabWrap.querySelectorAll(':scope > .tab__content');
    var index = Array.prototype.indexOf.call(contents, tabContent);
    if (index < 0) return false;
    var radios = tabWrap.querySelectorAll(':scope > input.tab');
    if (!radios[index]) return false;
    if (radios[index].checked) return false;
    radios[index].checked = true;
    // Re-scroll after the tab swap shifts layout
    requestAnimationFrame(function() {
      target.scrollIntoView({ block: 'start' });
    });
    return true;
  }

  if (location.hash) activateTabForHash(location.hash);
  window.addEventListener('hashchange', function() { activateTabForHash(location.hash); });

  // Handle click to open/close the submenu
  var submenuLinks = document.querySelectorAll(".simple > li > ul > li a");  // Select all links in submenus
  submenuLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      var parentLi = this.closest("li");  // Get the closest <li> even if it's wrapped in <p>
      var siblings = parentLi.parentElement.children;
      // Toggle the current submenu when clicked
      for (var i = 0; i < siblings.length; i++) {
        if (siblings[i] !== parentLi) {
          siblings[i].classList.remove("active");
        }
      }
      parentLi.classList.toggle("active");
    });
  });


  /* other survey results jump menu */
  var currentPath = window.location.pathname;
  var jumpMenu = document.getElementById('jumpMenu');

  // Loop through each option to find a match with the current path
  for (var i = 0; i < jumpMenu.options.length; i++) {
    if (jumpMenu.options[i].value === currentPath) {
      jumpMenu.selectedIndex = i;  // Set the option as selected
      break;  // Exit the loop once a match is found
    }
  }

  // Add event listener for the "Go" button
  document.getElementById('jumpButton').addEventListener('click', function() {
    var selectedValue = jumpMenu.value;
    if (selectedValue) {
      window.location.href = selectedValue;
    } else {
      alert('Please select a valid option');
    }
  });

  // Enter key activates select box jump
  jumpMenu.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      document.getElementById('jumpButton').click();
    }
  });     


/* Show the "Back to Top" button when scrolling */
window.onscroll = function() {
  let button = document.getElementById("back-to-top");
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    button.style.display = "block";
  } else {
    button.style.display = "none";
  }
};

// Scroll to top when the button is clicked
document.getElementById("back-to-top").onclick = function() {
  window.scrollTo({ top: 0, behavior: "smooth" });
  return false;  // Prevent default action
};    

/* hamburger menu */
var burgerMenu = document.getElementById('activator');
var overlay = document.getElementById('mobile-nav');
var tocLinks = document.getElementById('mobile-nav');
burgerMenu.addEventListener('click',function(){
  this.classList.toggle("close");
  overlay.classList.toggle("overlay");
});
tocLinks.addEventListener('click',function(event){
  if (event.target && event.target.tagName === "A") {
    burgerMenu.classList.remove("close");
    overlay.classList.remove("overlay");
  }  
}); 

  // Scrollspy: track current section and update TOC highlight + accordion
  const spyLinks = document.querySelectorAll('nav.main-toc a[href^="#"]');
  const spyH2Lis = document.querySelectorAll('nav.main-toc .simple > li > ul > li');
  const spyH3Lis = document.querySelectorAll('nav.main-toc .simple > li > ul > li > ul > li');

  const spyLinkMap = new Map();
  spyLinks.forEach(link => spyLinkMap.set(link.getAttribute('href').slice(1), link));

  // Derive headings from TOC link IDs (avoids relying on a <main> ancestor that Sphinx may not nest correctly)
  const spyHeadings = [];
  spyLinkMap.forEach((link, id) => {
    const el = document.getElementById(id);
    if (el) spyHeadings.push(el);
  });
  spyHeadings.sort((a, b) => a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1);

  let spyActiveId = null;

  function updateScrollSpy() {
    const threshold = window.scrollY + 80;
    let current = null;
    for (const h of spyHeadings) {
      if (h.getBoundingClientRect().top + window.scrollY <= threshold) current = h;
      else break;
    }
    const newId = current ? current.id : null;
    if (newId === spyActiveId) return;
    spyActiveId = newId;

    spyLinks.forEach(l => l.classList.remove('toc-current'));

    if (!newId) return;

    const activeLink = spyLinkMap.get(newId);
    if (!activeLink) return;

    activeLink.classList.add('toc-current');

    // Sync accordion: close all H2- and H3-level items, then open the ones containing the active link
    spyH2Lis.forEach(li => li.classList.remove('active'));
    spyH3Lis.forEach(li => li.classList.remove('active'));
    for (const li of spyH2Lis) {
      if (li.contains(activeLink)) { li.classList.add('active'); break; }
    }
    for (const li of spyH3Lis) {
      if (li.contains(activeLink)) { li.classList.add('active'); break; }
    }
  }

  let spyTicking = false;
  window.addEventListener('scroll', function() {
    if (!spyTicking) {
      requestAnimationFrame(function() { updateScrollSpy(); spyTicking = false; });
      spyTicking = true;
    }
  }, { passive: true });

  updateScrollSpy();


  // text quotes carousel
  const carouselContainer = document.querySelector('blockquote.pull-quote > div');
  const items = carouselContainer.querySelectorAll('p');
  const nextBtn = document.getElementById('next-btn');
  const prevBtn = document.getElementById('prev-btn');
  let currentIndex = 0;

  function showItem(index) {
    items.forEach((item, i) => {
      if (i === index) {
        item.classList.add('visible');
      } else {
        item.classList.remove('visible');
      }
    });
  }

  function goNext() {
    currentIndex = (currentIndex + 1) % items.length;
    showItem(currentIndex);
  }

  function goPrev() {
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    showItem(currentIndex);
  }

  nextBtn.addEventListener('click', goNext);
  prevBtn.addEventListener('click', goPrev);

  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') {
      goNext();
    } else if (event.key === 'ArrowLeft') {
      goPrev();
    }
  });

  showItem(currentIndex);

  
}); // DOMContentLoaded 

