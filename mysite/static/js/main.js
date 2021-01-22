var $ = JQuery.noConflict();
function listaClientes(){
    $.ajax({
        url: "/list/",
        type: "get",
        dataType: "json",

        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    })
}

$(document).ready(function(){
    listaClientes();
});