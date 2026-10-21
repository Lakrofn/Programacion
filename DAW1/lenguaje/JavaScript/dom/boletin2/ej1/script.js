let info = document.getElementById("info");
let parrafos = document.getElementsByTagName("p");
let enlaces = document.getElementsByTagName("a");

let numeroParrafos = parrafos.length;

let textoSegundoParrafo = parrafos[1].textContent;

let numeroEnlaces = enlaces.length;

let primerEnlace = enlaces[0].textContent;

let penultimoEnlace = enlaces[numeroEnlaces - 2].textContent;

let enlacesPrimerParrafo = parrafos[0].getElementsByTagName("a");

info.innerHTML =
    "Hay " + numeroParrafos + " párrafos.<br>" +
    "El texto del segundo parrafo es:  " + textoSegundoParrafo + " <br>" +
    "Hay " + numeroEnlaces + " enlaces.<br>" +
    "El primer enlace es " + primerEnlace + ".<br>" +
    "El penúltimo enlace es " + penultimoEnlace + ".<br>" +
    "El primer párrafo tiene " + enlacesPrimerParrafo.length + " enlaces.";