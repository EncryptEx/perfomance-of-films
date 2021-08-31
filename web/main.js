var a = 0;
var b = 0;
var c = 0;
var d = 0;
$(document).ready(function() {
    $("#submit").on("click", function() {
        var condiciones = $("#switch1").is(":checked");
        if (!condiciones) {
            var a = true;
            event.preventDefault();
        } else {
        	var a = false;
        }
        var condicioness = $("#switch2").is(":checked");
        if (!condicioness) {
            var b = true;
            event.preventDefault();
        } else {
        	var b = false;
        }
        var condicionesa = $("#switch3").is(":checked");
        if (!condicionesa) {
            var c = true;
            event.preventDefault();
        } else {
        	var c = false;
        }
        var condicionesd = $("#switch4").is(":checked");
        if (!condicionesd) {
            var d = true;
            event.preventDefault();
        } else {
        	var d = false;
        }
        eel.setsteps(a,b,c,d);
    });
});
