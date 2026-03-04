let array = [1,2,3,4,5,6,7];

function rotar(array, n){
    let arrayRotada = [];

    for(let i = 0; i < array.length; i++){
        if(i + n >= array.length){
            arrayRotada[i + n - array.length] = array[i];
        } else {
            arrayRotada[i + n] = array[i];
        }
    }

    return arrayRotada;
}

console.log(rotar(array, 3));