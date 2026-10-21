function generarNombre(cadena1, cadena2, cadena3){
    let resultado = "";
    if(cadena1.length > cadena2.length && cadena1.length > cadena3.length){
        resultado = cadena1;
    }
    else if(cadena2.length > cadena1.length && cadena2.length > cadena3.length){
        resultado = cadena2;
    }
    else if(cadena3.length > cadena1.length && cadena3.length > cadena2.length){
        resultado = cadena3;
    }
    else{
        resultado = "Hay almenos dos cadenas iguales";
    }
    return resultado;
}

console.log(generarNombre("hola", "hola2", "hola3"));