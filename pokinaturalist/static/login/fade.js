
 var elem = document.getElementById('welcome');

setTimeout(function() {
    elem.style.visibility = 'hidden';
    elem.style.opacity = '0';
    elem.style.transition = '5s';
    elem.style.opacity = '1';

}, 1250)