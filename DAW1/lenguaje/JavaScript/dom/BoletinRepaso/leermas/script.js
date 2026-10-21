/*quitar la clase de oculto y añadir la clase de visible al span*/

document.getElementsByClassName("enlace")[0].addEventListener("click", function () {
    document.getElementsByClassName("adicional")[0].classList.remove("oculto");
    document.getElementsByClassName("adicional")[0].classList.add("visible");
});
document.getElementsByClassName("enlace")[1].addEventListener("click", function () {
    document.getElementsByClassName("adicional")[0].classList.remove("visible");
    document.getElementsByClassName("adicional")[0].classList.add("oculto");
});
