document.addEventListener("DOMContentLoaded", function() {
    
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


  /* scroll handler for top level sections

  const topLevelSections = document.querySelectorAll('main > section > section[id]');  // Select all top-level sections
  console.log(topLevelSections);  // Debugging: Check if sections are selected

  const options = {
    root: null,  // Viewport
    threshold: 0.2  // Trigger when 20% of the section is in view
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      
      console.log(entry);  // Debugging: Check the entry being observed
      
      const targetLink = document.querySelector(`a[href="#${entry.target.id}"]`);  // Find the corresponding link in the nav

      if (targetLink) {
        // Find the parent <li> of the anchor element (even if it's wrapped in <p>)
        const parentLi = targetLink.closest('li');  // This will find the correct <li> element

        // Traverse up one level to get the <li> that contains the submenu <ul>
        const parentLiWithSubmenu = parentLi.parentElement.closest('li');

        // Find the submenu <ul> inside the parent <li> that contains the submenu
        const parentUl = parentLiWithSubmenu ? parentLiWithSubmenu.querySelector('ul') : null;

        // Check if section is in view and expand the submenu
        if (entry.isIntersecting) {
          targetLink.classList.add('current');  // Highlight the active section link

          // Expand the parent submenu if it's collapsed
          if (parentUl && !parentLiWithSubmenu.classList.contains('active')) {
            parentLiWithSubmenu.classList.add('active');  // Trigger submenu open
          }
        } else {
          targetLink.classList.remove('current');  // Remove the highlight

          // Collapse the submenu only when it's not the current one
          if (parentUl && parentLiWithSubmenu.classList.contains('active')) {
            parentLiWithSubmenu.classList.remove('active');  // Trigger submenu close
          }
        }
      }
    });
  }, options);

  // Observe each top-level section
  topLevelSections.forEach(section => observer.observe(section)); */



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
var tocLinks = document.getElementsByClassName('mobile-nav');
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

}); // DOMContentLoaded 

