document.getElementById("saludar").addEventListener("click" , function(){
    let nombre = document.getElementById("nombre").value;
    let apellidos = document.getElementById("apellidos").value;
    document.getElementById("saludo").innerHTML = "Hola " + nombre + " " + apellidos;
});