function contadorDeLetras(cadena, letra){
    contador = 0;
    for(let i = 0; i < cadena.length; i++){
        if(cadena[i] == letra){
            contador++;
        }
    }
    return contador;
}

console.log(contadorDeLetras("alvaro", "a"));