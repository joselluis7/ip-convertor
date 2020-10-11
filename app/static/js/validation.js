//PUT HERE SOME FORM VALIDATION
$(document).ready(function(){

    $('#submitButton').click(function(){
        if (($('#maskInput').val() == "") || ($('#ipInput').val() == "")){
            $('#validateModal').modal('toggle')
            console.log('Agora teste vazio')
            return false
        }else{
            $('#validateModal').modal('toggle')
            return true
        }
    }); 

    $('form').submit( function(event){
        var ip = {
            ipValue: $("#ipInput").val(),
            maskValue:$("#maskInput").val()
        }
        $.ajax({    
            type: 'POST',
            dataType: "json",
            contentType: "application/json",
            url: '/',
            data:JSON.stringify(ip),
            success: function(data){
                console.log('Agora funcionou ')
                //put here the write html
                
            }
        });
    });    
});   
