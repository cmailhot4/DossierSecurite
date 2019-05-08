$( "#boutonGauche" ).click(function() {
    $('#flashID').attr("align","left");
});
$( "#boutonDroite" ).click(function() {
    $('#flashID').attr("align","right");
});
$( "#boutonChangerImage" ).click(function() {
    var image = $('#flashID').attr("src");
    if(image === "img/flash.jpg"){
        $('#flashID').attr("src","img/flash2.jpg");
    }
    else{
        $('#flashID').attr("src","img/flash.jpg");
    }
});
$( "#boutonEnleverImage" ).click(function() {
    $('#flashID').fadeOut("slow", function () {
    });
});
$( "#boutonAjouterImage" ).click(function() {
    $('#flashID').fadeIn("slow", function () {
    });
});
$( "#boutonAjouterAttribut" ).click(function() {
    $('#flashID').attr("alt","Photo de flash");
});
$( '#boutonNuke' ).click(function() {
    $('body').html('<img src="img/download.jpg" width="100%"></img>');
});
$( "#boutonDupliquer" ).click(function() {
    $('#flashID').clone().insertAfter($('#flashID'));
});
$( "#boutonAjouterTitre" ).click(function() {
    $('#flashID').before('<h1>FLASH JQUERY</h1>');
});
$( "#boutonRalentir" ).click(function() {
    $('#flashID').remove().$('#flashID');
});
var compteur = 2;
$( "#boutonTeleport" ).click(function() {
    if(compteur%2 === 0){
        $('#boutonNuke').after($('#flashID'));
        compteur++;
    }
    else{

        $('#boutonGauche').before($('#flashID'));
        compteur++;
    }
});
$( "#boutonVitesseSupreme" ).click(function() {
    var temps = 0;
    while(temps <= 5){
        $('#flashID').fadeOut(500).fadeIn(500);
        temps++;
    }
});