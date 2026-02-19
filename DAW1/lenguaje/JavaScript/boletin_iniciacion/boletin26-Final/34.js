function toCase(cadena1, cadena2) {
    contador = 0;
    let resultado = "";

    while (contador < 2) {
        if (contador == 0) {
            resultado += cadena1.toLowerCase();
        }else{
            resultado += "-" + cadena2.toUpperCase();
        }
        contador++;
    }
    return resultado;
}

console.log(toCase("Alvaro", "Cruces"));