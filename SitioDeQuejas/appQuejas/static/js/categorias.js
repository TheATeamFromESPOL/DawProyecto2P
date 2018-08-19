(function(){
	$.ajax({
		type: "GET",
		url: "data/quejas.xml",
		dataType: "xml",
		success: cargarCategorias
	});
})();
/*
var itemsMenu = document.querySelectorAll('a[class*="list-group-item"]');
var itemsContenido = document.querySelectorAll('div[id^="cont-"]');


function activar(ja){
	for(i of itemsMenu){
		if(i == ja){
			i.classList.add("active");
		}else{
			i.classList.remove("active");
		}
	}

	for(j of itemsContenido){
		j.classList.remove("d-flex");
		j.classList.remove("d-none");
		if(j.id.includes(ja.id)){
			j.classList.add("d-flex");
		}else{
			j.classList.add("d-none");
		}
	}
}
*/

function cargarCategorias(data){
	$(data).find('categoria').each(function(){
		var nombreCategoria = $(this).find('nombreCategoria').text();
		var quejas = $(this).find('queja');
		for(i of quejas){
			var idQueja = $(i).find('id').text();
			var titulo = $(i).find('titulo').text();
			var fecha = $(i).find('fecha').text();
			var contenido = $(i).find('contenido').text();
			var imagen = $(i).find('imagen').text();
			var nombreUsuario = $(i).find('nombreUsuario').text();
			var conteoComentarios = 0;
			for(comentario of $(i).find('comentarios').find('comentario')){
				conteoComentarios++;
			}
			var previaQueja = $("<div></div>").attr("class", "previaConImagen col-md-3 p-1 align-self-stretch d-flex flex-column");
			var encabezadoQueja = $("<div><div>").attr({id: idQueja, class: "encabezadoQueja"});
			encabezadoQueja.append('<h3 id="'+idQueja+'"class="tituloQueja">'+titulo+'</h3>');
			encabezadoQueja.append("<h6>"+nombreCategoria+"</h6>");
			var contenidoQueja = $("<div></div>").attr("class", "contenidoQueja");
			contenidoQueja.append('<img class="imagenQueja" src="'+imagen+'">');
			if(contenido.length>=120){
				contenidoQueja.append('<p class="textoQueja">'+contenido.slice(0,117)+"...</p>");
			}else{
				contenidoQueja.append('<p class="textoQueja">'+contenido+"</p>");
			}
			var pieQueja = $("<div></div>").attr("class","pieQueja align-self-baseline");
			if(nombreUsuario.length>=20){
				pieQueja.append('<p class="mr-auto d-flex"><br><strong>Posteado por: </strong><a href="#home" class="mr-auto">'+nombreUsuario.slice(0,17)+'...</a></p>')
			}else{
				pieQueja.append('<p class="mr-auto d-flex "><br><strong>Posteado por: </strong><a href="#home" class="mr-auto">'+nombreUsuario+'</a></p>')
			}
			pieQueja.append('<button type="button" class="btn btn-primary bg-primary ml-auto"> Comentar <span class="badge badge-light">'+conteoComentarios+'</span></button>');
			previaQueja.append(encabezadoQueja);
			previaQueja.append(contenidoQueja);
			previaQueja.append(pieQueja);
			if(nombreCategoria=="Barrios/Ciudadelas"){
				previaQueja.appendTo("#cont-Barrios\\/Ciudadelas");
			}else if(nombreCategoria=="Casas/Terrenos abandonados"){
				previaQueja.appendTo("#cont-Casas\\/TerrenosAbandonados");
			}else if(nombreCategoria=="Pandillas"){
				previaQueja.appendTo("#cont-Pandillas");
			}else if(nombreCategoria=="Calles/Carreteras"){
				previaQueja.appendTo("#cont-Calles\\/Carreteras");
			}else if(nombreCategoria=="Señales de tránsito"){
				previaQueja.appendTo("#cont-SeñalesDeTránsito");
			}else if(nombreCategoria=="Animales callejeros"){
				previaQueja.appendTo("#cont-AnimalesCallejeros");
			}else if(nombreCategoria=="Basura en las calles"){
				previaQueja.appendTo("#cont-BasuraEnLasCalles");
			}
		}
	})
	var quejas=$(".encabezadoQueja").find('*').click(cargarNoticia);
}

function cargarNoticia(){
    var noticiaId=$(this).attr('id');
    window.location="noticia.html?noticia="+noticiaId;
}

