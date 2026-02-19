function crearPalabra(letra, numero){
    let resultado = "";
    for(let i = 0; i < numero; i++){
        resultado += letra;
    }
    return resultado;
}

console.log(crearPalabra("a", 3));