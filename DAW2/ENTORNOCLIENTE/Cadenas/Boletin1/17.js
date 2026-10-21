function contadorDeLetras2(cadena1, cadena2, letra){
    letra = letra.toLowerCase();
    cadena1 = cadena1.toLowerCase();
    cadena2 = cadena2.toLowerCase();
    contador1 = 0;
    contador2 = 0;
    for(let i = 0; i < cadena1.length; i++){
        if(cadena1[i] == letra){
            contador1++;
        }
    }
    for(let i = 0; i < cadena2.length; i++){
        if(cadena2[i] == letra){
            contador2++;
        }
    }
    return contador1 > contador2 ? cadena1 : cadena2;
}

console.log(contadorDeLetras2("alvaro", "cruaces", "a"));
