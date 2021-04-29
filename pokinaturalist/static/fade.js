
$(document).ready(function(){
    $('#pokedex video').bind('ended', function(){
        $(this).parent().fadeOut('slow')
    });
    $('#main').hide().delay(5000).fadeIn(200);
});