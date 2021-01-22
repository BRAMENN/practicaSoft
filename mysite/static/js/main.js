
      function guardarDatos(){
        var form = new FormData(document.getElementById("form-cliente"));
        console.log(form.get('Abuscar'));
        $.ajax({
          data: {'busqueda': form.get('Abuscar')},
          url: '/listClients/',
          type: 'get',
          success: function(data){
            
            var html = ""
            for(var i=0; i<data.length; i++){
              html += 
              '<li class="list-group-item">'+
                  '<div class="persona" >'+
                    '<div class="foto">'+
                      '<img src="' +data[i].fields.imge+ '" alt="">'+
                    '</div>'+

                    '<div class="cont1">'+
                      '<div class="nombre"><strong>' +data[i].fields.name+ '</strong></div>'+
                      '<div class="correo">' +data[i].fields.email+ '</div>'+
                    '</div>'+

                    '<div class="cont2">'+
                      '<div class="fechas">' +data[i].fields.birth+ ' | '+ data[i].fields.creation_day +'</div>'+
                      '<div class="botones">'+
                        '<button type="button" class="btn btn-primary">Editar</button>'+
                        '<button type="button" class="btn btn-danger">Eliminar</button>'+
                      '</div>'+
                    '</div>'+
                  '</div>'+
              '</li>'
            }
            
            $('#cliente').html(html);
          }
        });
    }
