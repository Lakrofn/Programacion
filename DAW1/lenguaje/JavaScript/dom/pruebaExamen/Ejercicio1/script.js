let cadena = "kk bb cc dd ee ff gg hh ii jj aa ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz";

function ordenarFrases(cadena) {
    cadena = cadena.split(" ");
    cadena.sort();
    return cadena.join(" ");
}

console.log(ordenarFrases(cadena));