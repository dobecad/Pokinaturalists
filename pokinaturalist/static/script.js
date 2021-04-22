var params = {
    container: document.getElementById('anim'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    rendererSettings:{progressivLoad:false},
    path: 'static/data2.json'
};


var lodanim = bodymovin.loadAnimation(params)

lodanim.addEventListener("complete",function(){

    console.log('begin fadeaway')
    var op = 1;
    var element = document.getElementById('anim')
    var timer = setInterval(function () {
       if (op <= 0.1){
            clearInterval(timer);
           element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);

})

function fade_out()
{
    console.log('begin fadeaway')
    lodanim.destroy();

}
