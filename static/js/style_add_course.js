const data = document.currentScript.dataset;
const server_data = data.data;

$(document).ready(function(){
    for(var i = 0; i < server_data["lessons"]; i++) {
        var html = document.getElementById("lesson" + toString(i));
        html.style.top = 30 + 10 * i;

        html = document.getElementById("lesson" + toString(i) + "_del");
        html.style.top = 28 + 10 * i;

        html = document.getElementById("lesson" + toString(i) + "_edit");
        html.style.top = 28 + 10 * i;
    }

    for(var i = 0; i < server_data["exercises"]; i++) {
        var html = document.getElementById("exercise" + toString(i));
        html.style.top = 30 + 10 * i;

        html = document.getElementById("exercise" + toString(i) + "_del");
        html.style.top = 28 + 10 * i;

        html = document.getElementById("exercise" + toString(i) + "_edit");
        html.style.top = 28 + 10 * i;
    }

    for(var i = 0; i < server_data["homeworks"]; i++) {
        var html = document.getElementById("homework" + toString(i));
        html.style.top = 30 + 10 * i;

        html = document.getElementById("homework" + toString(i) + "_del");
        html.style.top = 28 + 10 * i;

        html = document.getElementById("homework" + toString(i) + "_edit");
        html.style.top = 28 + 10 * i;
    }
});