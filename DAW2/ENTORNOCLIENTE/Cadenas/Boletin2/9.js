function codificarCesar(cadena, desplazamiento){
    let codificacion = "";
    for(let i = 0; i < cadena.length; i++){
        codificacion += String.fromCharCode(cadena.charCodeAt(i) + desplazamiento);
    }
    return codificacion;
}

console.log(codificarCesar("Abc z!", 2));