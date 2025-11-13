let num1 = '';
num1 = Number(num1);
let num2 = '';
num2 = Number(num2);
let operador = '';

    function numeros(valor) {
        if (operador === '') {
            num1 += valor; // Escribe el primer número
        } else {
            num2 += valor; // Escribe el segundo número
        }
            actualizarpantalla(); // Actualiza la pantalla
    }

    function operadores(valor) {
        if (num1 !== '') {
            operador = valor; // Guarda el operador
        }
            actualizarpantalla(); // Actualiza la pantalla
    }

    function limpiar() {
        num1 = '';
        num2 = '';
        operador = '';
        actualizarpantalla(); // Limpia la pantalla
    }

    function calculo() {
        let resultado = '';

        if (operador === '+') {
            resultado = num1 + num2;
        } else if (operador === '-') {
            resultado = num1 - num2;
        } else if (operador === '*') {
            resultado = num1 * num2;
        } else if (operador === '^') {
            resultado = Math.pow(num1, num2);
        } else if (operador === '/') {
            if (num2 !== '0') {
                resultado = num1 / num2;
            } else {
                resultado = 'Error'; // Maneja en caso de división por cero
            }
        }

        num1 = resultado; // Guarda el resultado como el nuevo num1
        num2 = ''; // Limpia el num2
        operador = ''; // Limpia el operador
        actualizarpantalla(); // Muestra el resultado
    }

function actualizarpantalla() {
        let display = document.getElementById('pantalla');
        pantalla.value = num1 + operador + num2; // Muestra lo que se ha escrito
    }