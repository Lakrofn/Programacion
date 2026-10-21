function evaluarEdad(edad) {
    let resultado = "";
    if (edad < 18) {
        resultado = "Eres menor de edad";
    } else if (edad >= 18 && edad < 65) {
        resultado = "Eres adulto menor";
    } else if (edad >= 65) {
        resultado = "Eres adulto mayor";
    }
    return resultado;
}

console.log(evaluarEdad(17));
console.log(evaluarEdad(18));
console.log(evaluarEdad(65));
