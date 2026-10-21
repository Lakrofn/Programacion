function invertirCadena(cadena) {
    let resultado = "";
    for (let i = cadena.length - 1; i >= 0; i--) {
        resultado += cadena[i];
    }
    return resultado;
}

console.log(invertirCadena("alvaro"));
console.log(invertirCadena("Hola Mundo"));
console.log(invertirCadena("Hola Mundo, alvaro"));