let numero = document.getElementById("numero");
let texto = document.getElementById("texto");
let acumulador = "";

document.getElementById("boton").addEventListener("click", function() {
    for (let i = 1; i <= numero.value; i++) {
        if (i % 2 === 0) {
            acumulador += i + " es par " + '<br>';
        } else {
            acumulador += i + " es impar " + '<br>';
        }
    }
    texto.innerHTML = acumulador;
});