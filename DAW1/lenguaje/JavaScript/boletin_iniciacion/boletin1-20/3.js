let num1 = 5;
let acumulador = num1 - 1;


while (num1 > 0) {
    acumulador += acumulador * num1;
    num1 -= 1;
}

console.log(acumulador);