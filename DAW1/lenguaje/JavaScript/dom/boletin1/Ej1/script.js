let nombre = document.getElementById("nombre");
let edad = document.getElementById("edad");

document.getElementById("insertar").addEventListener("click", function(){
    console.log("Hola " + nombre.value + " tu edad es " + edad.value + " y el año que viene tendras " + (Number(edad.value) + 1) + " años");
});