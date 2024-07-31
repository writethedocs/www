document.addEventListener("DOMContentLoaded", function() {
  var submenuLinks = document.querySelectorAll(".simple > li > ul > li > a");

  submenuLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      var parentLi = this.parentElement;
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
  });
});



