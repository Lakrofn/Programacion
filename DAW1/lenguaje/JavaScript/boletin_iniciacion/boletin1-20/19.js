let cadena = "Hola Mundo";

function contar(cadena) {
    let acumulador = "";
    for (let i = 0; i < cadena.length; i++) {
        if(i == cadena.length - 1) {
            acumulador = cadena[i];
        }
    }
    return acumulador;
}

console.log(contar(cadena));

console.log(cadena.charAt(cadena.length - 1));
console.log(cadena.substring(cadena.length - 1,cadena.length));