function compromirRepeticiones(cadena){
    cadena = cadena.toLowerCase();
    let repeticiones = 0;
    let actual = "";
    let acumulador = "";
    for(let i = 0; i < cadena.length+1; i++){
        if(cadena[i] !== actual){
            acumulador += actual + repeticiones;
            repeticiones = 0;
            actual = cadena[i];
            repeticiones++;
        }else{
            repeticiones++;
        }
    }
    return acumulador.substring(1);
}

console.log(compromirRepeticiones("aaabbc"));
console.log(compromirRepeticiones("wwwwaaadexxxxxx"));