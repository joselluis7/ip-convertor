//PUT HERE SOME FORM VALIDATION
$(document).ready(function(){
    $('#form').submit(function(event){
        if (($('#maskInput').val() == "") || ($('#ipInput').val() == "")){
            $('#validateModal').modal('toggle')
            return false;
        }
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
                console.log("worked")
                //$('#teste').html("Angola") //See before
            },
            error: function(){
                console.log("something got wrong")
            }
        });
        event.preventDefault()
    });    
});   
