/* Open when someone clicks on the span element */


function openNav() {
    var trainer = document.getElementsByClassName("leaflet-marker-icon leaflet-zoom-animated leaflet-interactive")[0];
    document.getElementById("myNav").style.width = "100%";
    fade(trainer);
  }
  
  /* Close when someone clicks on the "x" symbol inside the overlay */
  function closeNav() {
    var trainer = document.getElementsByClassName("leaflet-marker-icon leaflet-zoom-animated leaflet-interactive")[0];
    document.getElementById("myNav").style.width = "0%";
    unfade(trainer);
  }


  function fade(element) {
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.2){
            clearInterval(timer);
            element.style.opacity = '0.2';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);
}

function unfade(element) {
    var op = 0.2;  // initial opacity
    element.style.display = 'block';
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.1;
    }, 10);
}

// this is for the text box 
// retrieve the element
"use strict";
element = document.getElementById("display");

// reset the transition by...
element.addEventListener("click", function(e) {
  e.preventDefault;
  
  // -> removing the class
  element.classList.remove("typewriter");
  
  // -> triggering reflow /* The actual magic */
  // without this it wouldn't work. Try uncommenting the line and the transition won't be retriggered.
  // Oops! This won't work in strict mode. Thanks Felis Phasma!
  // element.offsetWidth = element.offsetWidth;
  // Do this instead:
  void element.offsetWidth;
  
  // -> and re-adding the class
  element.classList.add("typewriter");
}, false);