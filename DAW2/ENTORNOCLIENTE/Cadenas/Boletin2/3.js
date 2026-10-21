function esPalindromo(cadena){
    cadena = cadena.toLowerCase();
    let acumulador = '';
    cadena = cadena.replace(" ", "");
    for(let i = cadena.legnth - 1; i >= 0; i--){
        acumulador += cadena[i];
    }
    return acumulador === cadena;
}

console.log(esPalindromo('Dabale arroz a la zorra el abad'));