let cadena1 = "Álvaro Cruces Martínez";
let cadena2 = "Javier Madrigal Hidalgo";

function devuelveMasLarga(cadena1, cadena2){
    let resultado = "";
    if(cadena1.length > cadena2.length){
        resultado = cadena1;
    }
    else if(cadena1.length < cadena2.length){
        resultado = cadena2;
    }else{
        resultado = cadena1;
    }

    return resultado;
}

console.log(comparar(cadena1, cadena2));