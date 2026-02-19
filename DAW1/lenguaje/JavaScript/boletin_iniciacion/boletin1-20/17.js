function contar(cadena) {
    let contador = 0;
    for (let i = 0; i < cadena.length; i++) {
        if(cadena[i] !== " ") { 
            contador++;
        }
    }
    return contador;
}

console.log(contar("Hola Mundo"));