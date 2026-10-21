let chiste = document.getElementById("chisteEdit");
let lista = document.getElementById("chistesList");
let random = document.getElementById("randomText");
let eliminar = document.getElementsByClassName("btndel");
let editar = document.getElementsByClassName("btnedit");
let span = document.getElementsByClassName("chiste");

document.getElementById("btnNew").addEventListener("click", function(){
    let botondel = document.createElement("button");
    botondel.textContent = "eliminar" ;
    span.textContent = chiste.value;
    if(chiste.value.trim() != ""){
        

        let li = document.createElement("li");
        li.textContent = chiste.value;
        chiste.value= "";
        lista.appendChild(li);
        lista.appendChild(span)
        lista.appendChild(botondel);
        lista.appendChild(editar);
    }

    
})