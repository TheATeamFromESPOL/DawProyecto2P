(function(){ 
		
	$.ajax({
		type: "GET",
		url: "/ajax/categorias/",
		dataType: "json",
		success: cargarEstadisticos
	});
})();

function cargarEstadisticos(data){
	console.log(data);
	var datos2={labels:[],datasets:[{label:"Estadistico por numero de quejas",data:[],backgroundColor: [],borderColor:[]}]
	}
	
	for(var categoria of data) {

		datos2["labels"].push(categoria.nombre);
		datos2["datasets"][0]["data"].push(categoria["quejas"].length);
		datos2["datasets"][0]["backgroundColor"].push(getRandomColor());
		datos2["datasets"][0]["borderColor"].push("#262726");
	
	}
	var ctx = $("#myChart");
	var myDoughnutChart = new Chart(ctx, {
		type: 'doughnut',
		data: datos2,
		options:{
			legend: {
				labels: {
					// This more specific font property overrides the global property
					fontColor: 'white',
					fontSize:15,
				}
			}
		}
	});

}
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return hexToRgbA(color);
}
function hexToRgbA(hex){
    var c;
    if(/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)){
        c= hex.substring(1).split('');
        if(c.length== 3){
            c= [c[0], c[0], c[1], c[1], c[2], c[2]];
        }
        c= '0x'+c.join('');
        return 'rgba('+[(c>>16)&255, (c>>8)&255, c&255].join(',')+',1)';
    }
    throw new Error('Bad Hex');
}