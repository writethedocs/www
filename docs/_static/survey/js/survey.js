document.addEventListener("DOMContentLoaded", function() {
  
  /* internal navigation */
  var submenuLinks = document.querySelectorAll(".simple > li > ul > li a");
  submenuLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      var parentLi = this.closest("li"); 
      var siblings = parentLi.parentElement.children;
      // Hide other submenus
      for (var i = 0; i < siblings.length; i++) {
        if (siblings[i] !== parentLi) {
          siblings[i].classList.remove("active");
        }
      }
      // Toggle current submenu
      parentLi.classList.toggle("active");
    });
 

    // other survey results jump menu
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
  });


});