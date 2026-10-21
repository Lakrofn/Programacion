document.getElementById("isertar").addEventListener("click", function() {
    let lista = document.getElementById("lista");
    let texto = prompt("Introduce el texto a añadir");
    if (texto) {
        let li = document.createElement("li");
        li.textContent = texto;
        lista.appendChild(li);
    }
});

document.getElementById("borrarPrimero").addEventListener("click", function() {
    let lista = document.getElementById("lista");
    let primero = lista.firstChild;
    lista.removeChild(primero);
});

document.getElementById("borrarUltimo").addEventListener("click", function() {
    let lista = document.getElementById("lista");
    let ultimo = lista.lastChild;
    lista.removeChild(ultimo);
});