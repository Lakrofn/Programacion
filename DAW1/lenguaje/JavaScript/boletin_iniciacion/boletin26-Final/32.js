function contadorDeLetras(cadena, letra){
    let resultado = 0;
    for(let i = 0; i < cadena.length; i++){
        if(cadena[i] === letra){
            resultado++;
        }
    }

    return resultado;
}

console.log(contadorDeLetras("alvaro", "a"));
