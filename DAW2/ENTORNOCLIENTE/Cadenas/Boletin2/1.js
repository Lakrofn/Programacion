function cuentaVocales(cadena){
    cadena = cadena.toLowerCase();
    let cuenta = 0;
    for(let i = 0; i < cadena.length; i++){
        if(cadena[i] === 'a' || cadena[i] === 'e' || cadena[i] === 'i' || cadena[i] === 'o' || cadena[i] === 'u'){
            cuenta++;
        }
    }
    return cuenta;
}

console.log(cuentaVocales('Universidad'));
