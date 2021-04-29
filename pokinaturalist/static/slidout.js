/* Open when someone clicks on the span element */


function openNav() {
    var trainer = document.getElementsByClassName("leaflet-marker-icon leaflet-zoom-animated leaflet-interactive")[0];
    if(trainer)
    {
        console.log("found trainer");
    }
    document.getElementById("myNav").style.width = "100%";
    trainer.style.display = "none";
  }
  
  /* Close when someone clicks on the "x" symbol inside the overlay */
  function closeNav() {
    var trainer = document.getElementsByClassName("leaflet-marker-icon leaflet-zoom-animated leaflet-interactive")[0];
    document.getElementById("myNav").style.width = "0%";
    trainer.style.display = "block";
  }