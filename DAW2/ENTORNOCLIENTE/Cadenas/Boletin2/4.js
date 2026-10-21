function rotarDerecha(cadena, n){
    return cadena.substring(cadena.length - n) + cadena.substring(0, cadena.length - n);

}

console.log(rotarDerecha('abcdef', 2));