let cadena1 = "Álvaro Cruces Martínez";
let cadena2 = "Javier Madrigal Hidalgo";
let cadena3 = "Lucía Fernandez Román";

let cadena4 = "1234567";
let cadena5 = "12345678";
let cadena6 = "12345678";

function devuelveMasLarga2(cadena1, cadena2, cadena3){
    let resultado = "";
    if(cadena1.length > cadena2.length && cadena1.length > cadena3.length){
        resultado = cadena1;
    }
    else if(cadena2.length > cadena3.length && cadena2.length > cadena1.length){
        resultado = cadena2;
    }
    else if(cadena3.length > cadena1.length && cadena3.length > cadena2.length){
        resultado = cadena3;
    }
    else{
        resultado = "Hay almenos 2 cadenas iguales";
    }

    return resultado;
}


console.log(comparar(cadena1, cadena2, cadena3));
console.log(comparar(cadena4, cadena5, cadena6));