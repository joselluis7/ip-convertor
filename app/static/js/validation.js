//PUT HERE SOME FORM VALIDATION
$(document).ready(function(){
    console.log('teste')
    $('#submitButton').click(function(){
        if (($('#maskInput').val() == "") && ($('#ipInput').val() == "")){
            $('#validateModal').modal('toggle')
            return false
        }else{
            return true

        }
    });
    /**
    $('form').on('submit', function(event){
        $.ajax({
            data:{
                ip: $('#inputSearch').val(),
                mask: $('#inputSearch').val()
            },
            type: 'POST',
            url: '/'
        })
        .done(function(data){
            if (data.error){
                $('#emailLabel').text(data);
            }
            else{
                $('.collapse').collapse();
                //$('.collapse').text(data.name).show()
                $('#nameLabel').text(data.name);
                $('#biLabel').text(data.bi);
                $('#biLabel').text(data.morada);
            }
        });
        event.preventDefault();
    });
    */
}); 
