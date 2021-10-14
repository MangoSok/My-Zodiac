$(document).ready(function(){
    // $.get("http://localhost:5000/data", {}, function(response){
        
    //     $("#results").html(response.name + " is " + response.age + " years old");
    // });


    $("#btn").click(function(){
        var date = $("#nameInput").val();

        // alert("Will get zodiac " + date);

        $.get("/zodiac", {"date" : date}, function(response){
            $("#results").html(response.sign + response.comment);
        })
    });

});