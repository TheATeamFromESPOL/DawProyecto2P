
$(document).ready(cambiosNav);
var contador = 1; 
function cambiosNav(){
	$('.menu_bar').click(function(){
		// $('nav').toggle(); 
		
		$('ul').removeClass("row");
		if(contador == 1){
			$('nav').animate({
				left: '0'
			});
			
			console.log("abre?")
			contador = 0;
		} else {
			
			contador = 1;
			$('nav').animate({
				left: '-100%'
			});
			$('ul').addClass("row");
		}
 
	});
 
};