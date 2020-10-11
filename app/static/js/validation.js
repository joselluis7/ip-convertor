//PUT HERE SOME FORM VALIDATION
$(document).ready(function(){

    $('#submitButton').click(function(){
        if (($('#maskInput').val() == "") || ($('#ipInput').val() == "")){
            $('#validateModal').modal('toggle')
            console.log('Agora teste vazio')
            return false
        }else{
            console.log('Agora teste vazio')
            $('#validateModal').modal('toggle')
            return true
        }
    }); 
}); 

/*
$('form').on('submit', function(event){
    console.log('Agora teste entrou')
    $.ajax({
        type: 'POST',
        dataType: "json",
        contentType: "application/json",
        data:JSON.stringify(data_dict),
        url: 'https://localhost:5000/calc',
        success: function(data){
            console.log('Agora teste ')
        }
    });
    event.preventDefault();
});    
*/