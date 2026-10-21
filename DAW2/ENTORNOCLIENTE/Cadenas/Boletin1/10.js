function generarNombre3(cadena1, cadena2, cadena3){
    return cadena1.length > 5 && cadena2.length > 5 && cadena3.length > 5 ? 
    cadena1.substring(cadena1.length - 3) + cadena2.substring(cadena2.length - 3)  + cadena3.substring(cadena3.length - 3) :
    "error";
}

console.log(generarNombre3("alvaro", "cruces", "martinez"));