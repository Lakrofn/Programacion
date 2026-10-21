function primerasMayusculas(cadena){
    let acumulador = "";
    for(let i = 0; i < cadena.length; i++){
        if( i === 0 ){
            acumulador += cadena[i].toUpperCase();
        }else if(cadena[i -1] === " "){
            acumulador += cadena[i].toUpperCase();
        }else{
            acumulador += cadena[i];
        }
    }
    return acumulador;
}

console.log(primerasMayusculas("hola mundo desde js"));