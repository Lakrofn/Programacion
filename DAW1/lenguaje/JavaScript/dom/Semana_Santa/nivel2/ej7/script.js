let texto = document.getElementById("texto");
let body = document.getElementById("fondo");

document.getElementById("morado").addEventListener("click", function(){
    if(body.classList.contains("verde")){
        body.classList.remove("verde");
    }else if(body.classList.contains("azul")){
        body.classList.remove("azul");
    }
    body.classList.toggle("morado");
})

document.getElementById("verde").addEventListener("click", function(){
    if(body.classList.contains("morado")){
        body.classList.remove("morado");
    }else if(body.classList.contains("azul")){
        body.classList.remove("azul");
    }
    body.classList.toggle("verde");
})

document.getElementById("azul").addEventListener("click", function(){
    if(body.classList.contains("morado")){
        body.classList.remove("morado");
    }else if(body.classList.contains("verde")){
        body.classList.remove("verde");
    }
    body.classList.toggle("azul");
})

document.getElementById("cambio").addEventListener("click", function(){
    texto.classList.toggle("rojo");
})