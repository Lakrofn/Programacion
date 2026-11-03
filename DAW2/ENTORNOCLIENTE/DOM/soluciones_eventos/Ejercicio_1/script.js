// 1.1: clic sobre un botón
const boton = document.getElementById("boton");
boton.addEventListener("click", function () {
    console.log("Se ha pulsado el botón");
});

// 1.2: cambiar una clase CSS cuando entra o sale el ratón
const enlace = document.getElementById("enlace");
enlace.addEventListener("mouseenter", function () {
    enlace.classList.add("resaltado");
});
enlace.addEventListener("mouseleave", function () {
    enlace.classList.remove("resaltado");
});

// 1.3: coordenadas del puntero sobre la zona visible de la ventana
const coordenadas = document.getElementById("coordenadas");
document.body.addEventListener("mousemove", function (event) {
    coordenadas.textContent = `X: ${event.clientX} | Y: ${event.clientY}`;
});
