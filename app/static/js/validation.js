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
                //for(let i = 0; i < data.length; i++) {
                for (const property in data) {
                    console.log(data);
                
                    document.getElementById(`${property}-ip`).innerHTML = data[property].ip
                    document.getElementById(`${property}-mask`).innerHTML =  data[property].mask
                    document.getElementById(`${property}-network`).innerHTML = data[property].network
                    document.getElementById(`${property}-broadcast`).innerHTML = data[property].broadcast
                    document.getElementById(`${property}-last`).innerHTML = data[property].first_host
                    document.getElementById(`${property}-first`).innerHTML = data[property].last_host
                    if ( property == "decimal"){
                        document.getElementById(`${property}-mask`).innerHTML =  `${data[property].mask}/${data[property].prefix}`
                        document.getElementById(`${property}-hosts`).innerHTML = data[property].hosts_number
                    }        
                } 
                //$('#teste').html("Angola") //See before
            },
            error: function(){
                console.log("something got wrong")
            }
        });
        event.preventDefault()
    });    
});   
