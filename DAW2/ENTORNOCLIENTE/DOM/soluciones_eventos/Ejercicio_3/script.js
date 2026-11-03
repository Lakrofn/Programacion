const lista = document.getElementById("lista");
const resultado = document.getElementById("resultado");

// Un único escuchador en el UL; el clic sobre un LI burbujea hasta él.
lista.addEventListener("click", function (event) {
    const elemento = event.target;
    if (elemento.tagName !== "LI") return;

    console.log("Elemento pulsado:", elemento.textContent);
    console.log("target:", event.target);
    console.log("currentTarget:", event.currentTarget);

    // Criterio explícito de nivel: UL = 1, LI = 2.
    // Recorremos los padres desde el elemento pulsado hasta el UL.
    let nivel = 1;
    let actual = elemento;
    while (actual !== lista && actual.parentElement !== null) {
        actual = actual.parentElement;
        nivel++;
    }
    resultado.textContent = `${elemento.textContent}: nivel ${nivel} (UL = 1)`;
    console.log("Nivel dentro de la lista:", nivel);
});
