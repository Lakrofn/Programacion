function indexOfIgnoreCase(cadena1, cadena2){
    cadena1 = cadena1.toLowerCase();
    cadena2 = cadena2.toLowerCase();
    return cadena1.indexOf(cadena2);
}

console.log(indexOfIgnoreCase("bit", "it"));