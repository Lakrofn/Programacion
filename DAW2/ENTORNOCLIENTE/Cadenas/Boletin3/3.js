function contarVocales(cadena){
    cadena = cadena.toLowerCase();
    const vocales = "aeiouáéíóú";
    let contador = 0;

    for(let i = 0; i < cadena.lenght; i++){
        if(vocales.includes(cadena[i])){
            contador++;
        }
    }

    return contador;
}

console.log(contarVocales("javaSCript is great"));
