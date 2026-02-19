let num1; prompt("Introduce un numero: ");

function esPrimo(num1) {
    let respuesta = "Es un número primo";
    for(let i = 2; i < num1; i++) {
        if(i % num1 === 0) {
            respuesta = "No es un número primo";
        }
    }
    return respuesta;
}

console.log(esPrimo(num1));