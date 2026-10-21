function factorial(numero) {
    let resultado = numero;
    if (numero == 0) {
         console.log(1);
    } else {
        for (let i = 1; i < numero; i++) {
            resultado *= i;
        }
        console.log(resultado);
    }
}

factorial(5);
factorial(8);   
factorial(23);