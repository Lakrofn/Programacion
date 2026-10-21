let input = document.getElementById("nuevoElemento");
let lista = document.getElementById("lista");
// Agregar elementos
document.getElementById("agregar").addEventListener("click", function () {

    if (input.value.trim() !== "") {
        let li = document.createElement("li");
        li.textContent = input.value;
        lista.appendChild(li);
        input.value = "";
    }
});

// borrar la primera posicion

document.getElementById("eliminar").addEventListener("click", function(){
    for(let i = 0; i < 10; i++){
        lista.appendChild(lista.firstChild);
    }
});