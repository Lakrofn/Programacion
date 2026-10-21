function tieneLetra(cadena, letra){
    letra = letra.toLowerCase();
    cadena = cadena.toLowerCase();
    return cadena.indexOf(letra) > -1;
}

console.log(tieneLetra("alvaro", "A"));