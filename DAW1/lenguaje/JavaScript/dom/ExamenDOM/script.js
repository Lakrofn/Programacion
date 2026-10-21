let nombre = document.getElementById("nombre");
let comentario = document.getElementById("mensaje");
let lista = document.getElementById("lista");

document.getElementById("enviar").addEventListener("click", function(){
    let editar = document.createElement("button");
    editar.textContent = "Editar";
    let eliminar = document.createElement("button");
    eliminar.textContent = "Eliminar";

    let li = document.createElement("li");
    let span1 = document.createElement("span");
    span1.textContent = nombre.value + " dice:";
    span1.classList.toggle("usuario");

    let span2 = document.createElement("span");
    span2.textContent = comentario.value;


    let salto = document.createElement("br");


    if(nombre.value.trim() != "" && comentario.value.trim() != ""){
        lista.appendChild(li);
        li.appendChild(span1);
        li.appendChild(span2);
        li.appendChild(salto);
        li.appendChild(eliminar);
        li.appendChild(editar);
        nombre.value="";
        comentario.value="";
    }
});