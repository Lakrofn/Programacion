function addGuiones(cadena){
    let resultado = "";
    for(let i = 0; i < cadena.length; i++){
        if(i === cadena.length - 1){
            resultado += cadena[i];
        }
        else{
            resultado += cadena[i] + "-";
        }
    }
    return resultado;
}

console.log(addGuiones("alvaro"));