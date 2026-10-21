function sustituirVocalesPorAsteriscos(cadena){
    cadena = cadena.toLowerCase();
    let sustituido = '';
    for(let i = 0; i < cadena.length; i++){
        if(cadena[i] === 'a' || cadena[i] === 'e' || cadena[i] === 'i' || cadena[i] === 'o' || cadena[i] === 'u'){
            sustituido += '*';
        }else{
            sustituido += cadena[i];
        }
    }
    return sustituido;
}

console.log(sustituirVocalesPorAsteriscos('Carrera'));