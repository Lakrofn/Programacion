let cadena = "Hola Mundo";

function contar(cadena) {
    let acumulador = "";
    for (let i = 0; i < cadena.length; i++) {
        if(i == 0) { 
            acumulador = cadena[i];
        }
    }
    return acumulador;
}

console.log(contar(cadena));

console.log(cadena.charAt(0));
console.log(cadena.substring(0,1));