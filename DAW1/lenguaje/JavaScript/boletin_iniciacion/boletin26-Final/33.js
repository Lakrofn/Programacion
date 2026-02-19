function contadorDeLetras(cadena, letra){
    let resultado = 0;
    for(let i = 0; i < cadena.length; i++){
        if(cadena[i].toLowerCase() === letra.toLowerCase()){
            resultado++;
        }
    }

    return resultado;
}

console.log(contadorDeLetras("Alvaro", "a"));

function contadorDeLetras2(cadena1, cadena2, letra){
    let acumulador = 0;
    let suma = 0;
    let resultado = "";
    for(let i = 0; i < cadena1.length; i++){
        if(cadena1[i].toLowerCase() === letra.toLowerCase()){
            acumulador++;
        }
    }

    if(acumulador > suma){
        suma = acumulador;
        acumulador = 0;
        resultado = "La cadena: " + cadena1 + " tiene mas letras con la letra: " + letra;
    }else{
        acumulador = 0;
    }

    for(let i = 0; i < cadena2.length; i++){
        if(cadena2[i].toLowerCase() === letra.toLowerCase()){
            acumulador++;
        }
    }

    if(acumulador > suma){
        suma = acumulador;
        acumulador = 0;
        resultado = "La cadena: " + cadena2 + " tiene mas letras con la letra: " + letra;
    }else{
        acumulador = 0;
    }

    return resultado;
}

console.log(contadorDeLetras2("Alvaro", "Javier", "a"));