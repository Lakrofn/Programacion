const boton = document.getElementById("boton");
const resultado = document.getElementById("resultado");

// Primero registramos el escuchador.
boton.addEventListener("miEvento", function () {
    console.log("Se ha recibido miEvento");
    resultado.textContent = "Evento personalizado recibido.";
});

// Después lo lanzamos manualmente al pulsar el botón.
boton.addEventListener("click", function () {
    const evento = new CustomEvent("miEvento");
    boton.dispatchEvent(evento);
});
