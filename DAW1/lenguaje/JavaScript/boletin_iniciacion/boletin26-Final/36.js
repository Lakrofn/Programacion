function firstChar(cadena1) {
    contador = 0;
    let resultado = "";

    for (let i = 0; i < cadena1.length; i++) {
        if(cadena1[i] == " "){
            if (contador == 0) {
                resultado += cadena1[i+1];
                contador++;
            }
        }
    } 
    return resultado;
}

console.log(firstChar("Alvaro Cruces"));