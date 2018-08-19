(function(){
	/*console.log("ccbjkb")
	#$.ajax({
		type: "GET",
		url: "/ajax/enviarQuejas/",
		dataType: "json",
		success: obtenerQuejas
	});*/
	
})();
/*
function cargarNoticia(){
    var pk=$(this).attr('id');
    window.location="noticia/"+pk;
}

function obtenerQuejas(data){
	for(var queja of data) {
		var idQueja = queja.id;
		var titulo = queja.titulo;
		var nombreCategoria = queja.categoria
		var fecha = queja.fechaCreacion;
		var contenido = queja.descripcion;
		var imagen = queja.imagen;
		var nombreUsuario = queja.usuario;
		var conteoComentarios = 0;
		var previaQueja = $("<div></div>").attr("class", "previaConImagen col-md-3 p-1 align-self-stretch d-flex flex-column");
		var encabezadoQueja = $("<div></div>").attr("class", "encabezadoQueja");
		encabezadoQueja.append('<div class="tituloQueja"> <h3 id="'+idQueja+'">'+titulo+'</h3></div>');
		encabezadoQueja.append("<h6>"+nombreCategoria+"</h6>");
		var contenidoQueja = $("<div></div>").attr("class", "contenidoQueja");
		contenidoQueja.append('<img class="imagenQueja" src="'+imagen+'">');
		if(contenido.length>=120){
			contenidoQueja.append('<p class="textoQueja">'+contenido.slice(0,117)+"...</p>");
		}else{
			contenidoQueja.append('<p class="textoQueja">'+contenido+"</p>");
		}
		var pieQueja = $("<div></div>").attr("class","pieQueja align-self-baseline");
		
		
		pieQueja.append('<p class="mr-auto d-flex "><br><strong>Posteado por: </strong><a href="#home" class="mr-auto">'+nombreUsuario+'</a></p>')
		
		pieQueja.append('<button type="button" class="btn btn-primary bg-primary ml-auto"> Comentar <span class="badge badge-light">'+conteoComentarios+'</span></button>');
		previaQueja.append(encabezadoQueja);
		previaQueja.append(contenidoQueja);
		previaQueja.append(pieQueja);
		previaQueja.appendTo("#conjuntoDeQuejas");
	}
	#$(".tituloQueja").find('*').click(cargarNoticia);			

}*/