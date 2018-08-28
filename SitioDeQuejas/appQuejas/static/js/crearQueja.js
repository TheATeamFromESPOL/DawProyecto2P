(function(){
})();

$("#botonNuevaQueja").click(hacerQueja);
$("#cerrarCuadroQueja").click(cerrarNuevaQueja);
$("#botonEnviarQueja").click(agregar);
function hacerQueja(){
	console.log("si coge")
	$("#nuevaQueja").fadeIn();
	categorias();
    //botones para ver/eliminar

}
function agregar(){
	console.log("entra boton enviar");
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={}
<<<<<<< HEAD
    inforepo ={}
=======
    info.id;
>>>>>>> 6e68dd65de551a109e324f7a7cc2b5fef5db2bd3
    info.titulo=$("#inputTitulo").val(),
    info.categoria=Number($("#selectCategoria").val()),
    info.imagen="imagenRuta";
    info.descripcion=$("#explicacionQueja").val();
    info.usuario=$(".userId").attr("id");
    info.usuario=2;
    inforepo.nombreCategoria=$("#selectCategoria").val(),
    inforepo.usuarioId=2;
    console.log(info)
    console.log(inforepo)
    $.ajax({
        url: "/ajax/administarQuejas/",
        type:"POST",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
        	console.log("exito enviar");
            alert("queja cargada con éxito");
            cerrarNuevaQueja();
        },
        error : function(xhr, status) {
        	console.log("error");
            alert(xhr['responseJSON']);
        },
    });
    $.ajax({
        url: "ajax/CategoriaReporte/",
        type:"POST",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:inforepo,
        success :function(respuesta) {
            console.log("exito enviar");
            alert("queja cargada con éxito");
            cerrarNuevaQueja();
        },
        error : function(xhr, status) {
            console.log("error");
            alert(xhr['responseJSON']);
        },
    });
	
}

function cerrarNuevaQueja(){
	console.log("hace clic");
	$("#selectCategoria option").remove();
	$("#nuevaQueja").fadeOut();
}
function categorias(){
    $.ajax({
        url: "/ajax/categorias/",
        type:"GET",    
        dataType : 'json',
        success: cargarCategorias,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar las Categorias.');
        }
    });
}
function cargarCategorias(data){

    for (categoria of data) {
    	opcionCategoria = '<option value='+categoria.id+'>' + categoria.nombre + '</option>';
    	$('#selectCategoria').append(opcionCategoria);
    }
}