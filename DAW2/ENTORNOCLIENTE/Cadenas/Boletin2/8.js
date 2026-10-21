function contadorDePalabras(cadena) {
    let palabras = 0;
    cadena = cadena.trim();
    for (let i = 0; i < cadena.length; i++) {
        if (i === 0) {
            palabras++;
        } else {
            if (cadena[i] === " ") {
                palabras++;
            }
        }

    }
    return palabras;
}

console.log(contadorDePalabras("esto es una prueba"));