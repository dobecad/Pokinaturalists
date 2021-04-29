

var logo = document.getElementById('back');
var animation = bodymovin.loadAnimation({
container: logo,
renderer: 'svg',
loop: false,
autoplay: false,
prerender: true,
path: '/pokinaturalist/static/backpack.json'
});
if(logo)
{
    console.log("here");
}

logo.addEventListener("mouseenter", function () {
    console.log("mouse enters");
    animation.play();
});

logo.addEventListener("mouseleave", function () {
    console.log("mouse leave");
    animation.stop();
});