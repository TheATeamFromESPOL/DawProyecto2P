(function(){
    console.log("cdscvcv")
    $.ajax({
        type: "GET",
        url: "/ajax/cargarNoticia/",
        dataType: "json",
        success: obtenerQueja
    });
})();

function obtenerQueja(data){
	console.log("coge")
}
