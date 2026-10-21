function mostrarImpares(numeros) {
    for (let i = 0; i < numeros.length; i++) {
        if (numeros[i] % 2 != 0) {
            console.log(numeros[i]);
        }
    }
}

mostrarImpares([10, 25, 32, 47, 50, 61, 78, 83]);