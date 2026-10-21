function generarNombre2(cadena1, cadena2, cadena3){
    return cadena1.length > 5 && cadena2.length > 5 && cadena3.length > 5 ? 
    cadena1.charAt(cadena1.length - 1) + cadena2.charAt(cadena2.length - 1)  + cadena3.charAt(cadena3.length - 1) :
    "error";
}

console.log(generarNombre2("alvaro", "cruces", "martinez"));