// Agregar elementos
document.getElementById("agregar").addEventListener("click", function () {
    let input = document.getElementById("nuevoElemento");
    let lista = document.getElementById("lista");

    if (input.value.trim() !== "") {
        let li = document.createElement("li");
        li.textContent = input.value;
        lista.appendChild(li);
    }
});

// Borrar elemento por posición
document.getElementById("borrarElemento").addEventListener("click", function () {
    let lista = document.getElementById("lista");
    let posicionInput = document.getElementById("posicionBorrar");
    let mensaje = document.getElementById("mensaje");

    let posicion = parseInt(posicionInput.value);

    if (!isNaN(posicion) && posicion > 0 && posicion <= lista.children.length) {
        let elementoBorrado = lista.children[posicion - 1].textContent;
        lista.removeChild(lista.children[posicion - 1]);

        mensaje.textContent = "Se eliminó el elemento en la posición " + posicion + ": " + elementoBorrado;
    } else {
        mensaje.textContent = "Posición inválida.";
    }

    posicionInput.value = "";
});