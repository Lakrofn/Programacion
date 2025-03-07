let pantalla = document.getElementById('pantalla');
let num1 = '';
let num2 = '';
let operator = '';
let resultado = '';

function numeros(numero){
    if(operator == ''){
        num1 += numero;
    }else{
        num2 += numero;
    }
pantalla.value = num1;
}

function limpiar(){
    num1 = '';
    num2 = '';
    operator = '';
    pantalla.value = '';
}

function sumar(){
 if(operator == '+'){
    resultado = num1 + num2;
 }
}

function restar(){
 if(operator == '-'){
    resultado = num1 - num2;
 }
}

function multiplicar(){
 if(operator == '*'){
    resultado = num1 * num2;
 }
}

function dividir(){
 if(operator == '/'){
    resultado = num1 / num2;
 }
}

function calcular(){
 if(operator == '^'){
    resultado = Math.pow(num1, num2);
 }
}

function igualar(){
 if(operator == '='){
    resultado = eval(num1 + operator + num2);
 }
}

function calculo(){
    num1 = pantalla.value;
    operator = document.querySelector('.operator').innerText;
    igualar();
    pantalla.value = resultado;
}
