
$(document).ready(function(){
    $(".newtitle").attr("disabled", true);
    $(".apellido").attr("disabled", true);
    

    $( "#cmbopciones" ).change( function() { 
        if(($('#cmbopciones').val()=='Ver')){
            $("#crud").show();
            $("#agg").hide();
            $(".bt_update").hide();
            $(".bt_eliminar").hide();
            $(".newtitle").attr("disabled", true);
            $(".apellido").attr("disabled", true);
        }
        if(($('#cmbopciones').val()=='Agregar')){
            $("#crud").hide();
            $("#agg").show();
            $(".bt_update").hide();
            $(".bt_eliminar").hide();
            $(".newtitle").attr("disabled", true);
            $(".apellido").attr("disabled", true);
        }
        if(($('#cmbopciones').val()=='Modificar')){
            $("#agg").hide();
            $("#crud").show();
            $(".bt_update").show();
            $(".bt_eliminar").hide();
            $(".newtitle").attr("disabled", false);
            $(".apellido").attr("disabled", false);

        } 
        if(($('#cmbopciones').val()=='Eliminar')){
          
            $("#agg").hide();
            $("#crud").show();
            $(".bt_update").hide();
            $(".bt_eliminar").show();
            
            
            $(".newtitle").attr("disabled", true);
            $(".apellido").attr("disabled", true);





                    
                    








            
        } 
    });        
});