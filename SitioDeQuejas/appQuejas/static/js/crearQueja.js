(function(){
})();

$("#botonNuevaQueja").click(hacerQueja);
$("#cerrarCuadroQueja").click(cerrarNuevaQueja);

function hacerQueja(){
	$("#nuevaQueja").fadeIn();
}

function cerrarNuevaQueja(){
	console.log("hace clic");
	$("#nuevaQueja").fadeOut();
}