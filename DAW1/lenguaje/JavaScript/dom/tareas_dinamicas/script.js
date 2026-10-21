let tarea = document.getElementById("tarea");
let añadir = document.getElementById("añadir");
let lista = document.getElementById("lista");
let borrar = document.getElementById("limpiar");


/* boton de añadir tarea */
añadir.addEventListener("click", function(){
    if(tarea.value.trim() !== ""){
        let li = document.createElement("li");
        let span = document.createElement("span");
        span.textContent = tarea.value;
        let eliminar = document.createElement("button");
        eliminar.textContent = "Eliminar";
        let editar = document.createElement("button");
        editar.textContent = "Editar";

         /* boton de editar tarea */
        editar.addEventListener("click", function(){
            let tareaEditada = document.createElement("input");
            tareaEditada.type = "text";
            tareaEditada.value = span.textContent;

            li.replaceChild(tareaEditada, span);

            tareaEditada.focus();

            editar.textContent = "Guardar";

            editar.addEventListener("click", function(){
                if(tareaEditada.value.trim() !== ""){
                    span.textContent = tareaEditada.value;
                    editar.textContent = "Editar";
                    li.replaceChild(span, tareaEditada);
                }
            });
        });

        /* boton de borrar tarea */
        eliminar.addEventListener("click", function(){
            li.remove();
        });

        lista.appendChild(li);
        li.appendChild(span);
        li.appendChild(editar);
        li.appendChild(eliminar);
        tarea.value = "";
    }

    
});



/* boton de borrar todo */
borrar.addEventListener("click", function(){
    lista.innerHTML = "";
});

editar.addEventListener("click", () => {
    span.style.textDecoration = "line-through";
});
