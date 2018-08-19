(function(){
})();

$("#botonEnviar").click(clicEnviar);

function clicEnviar(){
	if(confirm("¿Seguro de enviar?")){
		alert("Mensaje enviado");
		location.reload(true);
	}else{
		alert("Mensaje no enviado");
	}
}