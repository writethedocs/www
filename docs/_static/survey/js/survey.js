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

