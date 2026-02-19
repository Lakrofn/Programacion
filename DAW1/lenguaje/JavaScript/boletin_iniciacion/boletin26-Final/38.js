function firstWord(cadena1) {
    contador = 0;
    let resultado = "";

    for (let i = 0; i < cadena1.length; i++) {
        if(cadena1[i] == " "){
            contador++;
        }else{
            if (contador == 0) {
                resultado += cadena1[i];
            }
        }
    
    } 
    return resultado;
}

console.log(firstWord("Alvaro Cruces"));