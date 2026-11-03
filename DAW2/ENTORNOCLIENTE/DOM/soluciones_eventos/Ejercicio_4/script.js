const formulario = document.getElementById("formulario");
const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const mensaje = document.getElementById("mensaje");

// Escuchador del evento personalizado.
formulario.addEventListener("formularioEnviado", function () {
    console.log("Evento formularioEnviado recibido");
    mensaje.textContent = "Formulario validado y enviado correctamente (simulación).";
});

formulario.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita la navegación o recarga predeterminada.
    const nombreValor = nombre.value.trim();
    const correoValor = correo.value.trim();

    if (nombreValor === "" || correoValor === "") {
        mensaje.textContent = "Error: nombre y correo no pueden estar vacíos.";
        return;
    }
    // Validación básica adicional del formato del correo.
    if (!correo.checkValidity()) {
        mensaje.textContent = "Error: escribe un correo electrónico válido.";
        return;
    }

    // No hay servidor: el envío es una simulación local.
    const evento = new CustomEvent("formularioEnviado");
    formulario.dispatchEvent(evento);
});
