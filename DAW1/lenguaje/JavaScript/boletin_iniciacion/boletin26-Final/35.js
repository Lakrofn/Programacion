function shortcut(cadena1, cadena2) {
    contador = 0;
    let resultado = "";

    while (contador < 2) {
        if (contador == 0) {
            resultado += cadena1[0].toUpperCase();
        }else{
            resultado += cadena2[0].toUpperCase();
        }
        contador++;
    }
    return resultado;
}

console.log(shortcut("Alvaro", "Cruces"));
console.log(shortcut("Amnesty", "International"));