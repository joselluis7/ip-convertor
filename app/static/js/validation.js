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
                document.getElementById("decimal-ip").innerHTML = data.decimal.ip
                document.getElementById("decimal-mask").innerHTML = data.decimal.mask
                document.getElementById("decimal-network").innerHTML = data.decimal.network + "/" + data.decimal.prefix
                document.getElementById("decimal-broadcast").innerHTML = data.decimal.broadcast
                console.log(data)
                
                //$('#teste').html("Angola") //See before
            },
            error: function(){
                console.log("something got wrong")
            }
        });
        event.preventDefault()
    });    
});   
