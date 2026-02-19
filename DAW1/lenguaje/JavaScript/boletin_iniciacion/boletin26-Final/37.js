function indexOfIgnoreCase(cadena1, cadena2) {
    contador = 0;
    let resultado = "";

    for (let i = 0; i < cadena1.length; i++) {
        for (let j = 0; j < cadena2.length; j++) {
            if(cadena1[i].toLowerCase() == cadena2[j].toLowerCase()){
                if (contador == 0) {
                    resultado += cadena1[i];
                    contador++;
                }
            }
        }
    } 
    return resultado;
}

console.log(indexOfIgnoreCase("Alvaro Cruces", "cruces"));