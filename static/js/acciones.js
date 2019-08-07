$(document).ready(function(){
	var ajax = function(method, url, data = null) {
      var xhttp = new XMLHttpRequest();
      return new Promise((resolve, reject) => {
          xhttp.onreadystatechange = function() {
              if (this.readyState == 4 && this.status == 200) {
                  resolve(this.responseText);
              }
          };
          xhttp.open(method, url, true);           if (data != null) {
              xhttp.send(JSON.stringify(data));
          } else {
              xhttp.send();
          }       });
  };

	$(".fa").click(function(){
		
		if ($(this).attr("class").split(" ")[1]=='fa-toggle-off') {
			$(this).removeClass('fa-toggle-off');
			$(this).addClass('fa-toggle-on');
			// console.log();
			actualizar_status($(this).find("input").attr('value'));
		}
		else {
			if ($(this).attr("class").split(" ")[1]=='fa-toggle-on') {
				$(this).removeClass('fa-toggle-on');
				$(this).addClass('fa-toggle-off');
				actualizar_status($(this).find("input").attr('value'));
			}
		}
	});

	$('.Eliminar').click(function(){
		console.log("-------------------------");
		eliminar_tarea($(this).attr('value'));
	});

	actualizar_status= function(pk){
		ajax("GET", '/tareas/tarea/actualizar/?pk='+pk ).then(function(response) {
			console.log(response);
			location.reload();
		});
	}
	eliminar_tarea= function(pk){
		ajax("GET", '/tareas/tarea/eliminar/?pk='+pk ).then(function(response) {
			console.log(response);
			location.reload();
		});	
	}
});