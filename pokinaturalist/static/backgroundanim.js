var params = {
    container: document.getElementById('backAnim'),
    renderer: 'svg',
    loop: true,
    autoplay: true,
    rendererSettings:{progressivLoad:false},
    path: 'static/world.json'
};

var lodanim = bodymovin.loadAnimation(params)