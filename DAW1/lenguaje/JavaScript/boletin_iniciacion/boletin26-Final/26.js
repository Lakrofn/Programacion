let cadena1 = "Álvaro";
let cadena2 = "Javier";
let cadena3 = "Lucía";

function generalNombre(cadena1, cadena2, cadena3){
    let resultado = "";

    if(cadena1.length >= 5 && cadena2.length >= 5 && cadena3.length >= 5){
        resultado = cadena1.substring(cadena1.length -3,cadena1.length) + cadena2.substring(cadena2.length -3,cadena2.length) + cadena3.substring(cadena3.length -3,cadena3.length);
    }
    else{
        resultado = "ERROR";
    }
    return resultado;
}


console.log(generalNombre(cadena1, cadena2, cadena3));