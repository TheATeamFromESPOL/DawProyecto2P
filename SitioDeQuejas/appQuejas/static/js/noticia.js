(function(){

	$.ajax({
		type: "GET",
		url: "data/quejas.xml",
		dataType: "xml",
		success: obtenerQuejas
	});

})();

var paramstr = window.location.search.substr(1);
console.log(paramstr);
var paramarr = paramstr.split ("&");
var params = {};
for ( var i = 0; i < paramarr.length; i++) {
var tmparr = paramarr[i].split("=");
params[tmparr[0]] = tmparr[1];
}
var noticiaId =  params['noticia'];
//Cargar noticia solo si es igual a la variable nombre

function obtenerQuejas(data){
	$(data).find('categoria').each(function(){
		var nombreCategoria = $(this).find('nombreCategoria').text();
		var quejas = $(this).find('queja');
		for(i of quejas){
            if($(i).find('id').text()==noticiaId){
                
                console.log("entro");
                var idQueja = $(i).find('id').text();
                var titulo = $(i).find('titulo').text();
                //var fecha = $(i).find('fecha').text();
                var contenido = $(i).find('contenido').text();
                var imagen = $(i).find('imagen').text();
                var nombreUsuario = $(i).find('nombreUsuario').text();
                var conteoComentarios = 0;
                for(comentario of $(i).find('comentarios').find('comentario')){
                    conteoComentarios++;
                }
                var previaQueja = $("<div></div>").attr("class","previaConImagen border col-md-4 p-2 m-5");
                var encabezadoQueja = $("<div><div>").attr({id: idQueja, class: "encabezadoQueja"});
                encabezadoQueja.append('<h3 id="'+idQueja+'"class="tituloQueja">'+titulo+'</h3>');
                encabezadoQueja.append("<h6>"+nombreCategoria+"</h6>");
                var contenidoQueja = $("<div></div>").attr("class", "contenidoQueja");
                contenidoQueja.append('<img class="imagenQueja" src="'+imagen+'">');
               contenidoQueja.append('<p class="textoQueja">'+contenido+"</p>");
                
                var pieQueja = $("<div></div>").attr("class","pieQueja align-self-baseline");
                pieQueja.append('<p class="mr-auto d-flex "><br><strong>Posteado por:  </strong><a href="#home" class="mr-auto"> '+' '+nombreUsuario+'</a></p>')
                
                previaQueja.append(encabezadoQueja);
                previaQueja.append(contenidoQueja);
                previaQueja.append(pieQueja);
                previaQueja.appendTo("#noticia");
            // Comentarios
                var comentarios=$("<div></div>").attr("class", "post-comment");

                var cs=$("<div></div>").attr("class", "CS3");

                var tab=$("<div></div>").attr("class", "tab-bar clearfix");
                var tabNumber=$("<div></div>").attr("class", "tab-bar-left");

                tabNumber.append("<h6>"+conteoComentarios+" Comentarios"+"</h6>");
                
                tab.append(tabNumber);        
                
                var comm=$("<div></div>").attr("class", "comment-embed");
                var comentar=$("<div></div>").attr("class", "comment-box first");
                
                var avatar=$("<div></div>").attr("class", "avatar");
                var imagContainer=$("<div></div>").attr("class", "image-container");
                imagContainer.append("<a href='javascript:void(0)' target='_blank'><img src='https://accounts-cdn.9gag.com/media/default-avatar/1_0_100_v0.jpg'></a>");
                avatar.append(imagContainer);
                comentar.append(avatar);

                var payLoad=$("<div></div>").attr("class", "payload");
                
                var textArea=$("<div></div>").attr("class", "textarea-container");
                var text=$("<div></div>");
                text.append('<textarea placeholder="Deja Tu Comentario" class="post-text-area focus"></textarea>')
                textArea.append(text);
                var accion= $("<div></div>").attr("class", "action");
                var rhs = $("<div></div>").attr("class", "rhs");
                rhs.append('<a href="javascript:void(0);" class="cmnt-btn size-10 submit-comment">Comentar</a>');
                accion.append(rhs);
                payLoad.append(textArea);
                payLoad.append(accion);
                comentar.append(avatar);
                comentar.append(payLoad);
                comm.append(comentar);
                           
                var contenidosComme=$("<div></div>");
                for(comentario of $(i).find('comentarios').find('comentario')){
                    var conteni=$("<div></div>");
                    var comentar=$("<div></div>").attr("class", "comment-entry");
                    var avatar=$("<div></div>").attr("class", "avatar");
                    var imagContainer=$("<div></div>").attr("class", "image-container");
                    imagContainer.append("<a href='javascript:void(0)' target='_blank'><img src='https://accounts-cdn.9gag.com/media/avatar/39207959_100_7.jpg'></a>");
                    avatar.append(imagContainer);
                    var payLoad=$("<div></div>").attr("class", "payload");
                    var info=$("<div></div>").attr("class", "info");
                    info.append('<p><a href="javascript:void(0)" target="_blank" class="username">'+$(comentario).find('usuarioComentario').text()+'</a> </p>')
                    payLoad.append(info);
                    payLoad.append('<div class="content">'+$(comentario).find('contenidoComentario').text()+'</div>')
                    comentar.append(avatar);
                    comentar.append(payLoad);
                    conteni.append(comentar);
                    contenidosComme.append(conteni)
                    comm.append(contenidosComme)
                    //var media=$("<div></div>").attr("class", "media");
                    //media.append('<a href="javascript:void(0)" target="_blank" class="img-embed"><img src="https://img-comment-fun.9cache.com/media/aZg1Lb9/aDVRob7V_700w_0.jpg"></a>')
                    

                }
                cs.append(tab);
                cs.append(comm);
                comentarios.append(cs);
                previaQueja.append(comentarios)

            }
            else{

            }
		}
	})
}
