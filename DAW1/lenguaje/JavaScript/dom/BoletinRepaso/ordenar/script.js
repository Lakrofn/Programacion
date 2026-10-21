document.getElementById("ordenar").addEventListener("click" , function(){
    let numeros = document.getElementById("numeros").value;
    numeros = numeros.split(",");
    numeros.sort();
    document.getElementById("ordenado").innerHTML = numeros;
});
