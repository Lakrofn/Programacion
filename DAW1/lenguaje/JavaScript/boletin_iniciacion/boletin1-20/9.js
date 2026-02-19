let array1 = [12,42,1,53,16,82,23];

let mayor = 0;
for(let i = 0; i < array1.length; i++) {
    if(array1[i] > mayor) {
        mayor = array1[i];
    }
}

console.log(mayor);