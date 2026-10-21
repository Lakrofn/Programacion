function crearPalabra(letra, numero){
    letra = letra.toUpperCase();
    return letra.repeat(numero);
}

console.log(crearPalabra("a", 3));