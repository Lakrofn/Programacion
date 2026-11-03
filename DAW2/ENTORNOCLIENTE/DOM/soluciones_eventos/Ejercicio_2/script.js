const resultado = document.getElementById("resultado");
// El enunciado propone detectar keydown sobre document.body.
document.body.addEventListener("keydown", function (event) {
    const mensaje = `Tecla: ${event.key} | Código: ${event.code}`;
    resultado.textContent = mensaje;
    console.log(mensaje);
    // Si se exige expresamente un aviso emergente, sustituir console.log
    // por alert(mensaje). Se evita por comodidad al probar muchas teclas.
});
// Comparación opcional con keyup:
document.body.addEventListener("keyup", function (event) {
    console.log("Tecla soltada:", event.key);
});
