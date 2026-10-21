function generarNombre(cadena1, cadena2, cadena3){
    return cadena1.length > 5 && cadena2.length > 5 && cadena3.length > 5 ? 
    cadena1.substring(0,3) + cadena2.substring(0,3)  + cadena3.substring(0,3) : "error";
}

console.log(generarNombre("alvaro", "cruces", "martinez"));