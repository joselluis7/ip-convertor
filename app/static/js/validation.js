//PUT HERE SOME FORM VALIDATION
$(document).ready(function(){
    $('#submitButton').click(function(){
        if ($('#maskInput').val() == ""){
            $('#validateModal').modal('toggle')
            return false
        }else{
            return true

        }
    });
});
