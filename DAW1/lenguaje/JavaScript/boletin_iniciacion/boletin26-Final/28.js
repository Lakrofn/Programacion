function tieneLLetra(cadena, letra){
    let resultado = false;
    for(let i = 0; i < cadena.length; i++){
        if(cadena[i].toLowerCase() === letra.toLowerCase()){
            resultado = true;
        }
    }

    return resultado;
}

console.log(tieneLLetra("alvaro", "a"));
console.log(tieneLLetra("alvaro", "A"));