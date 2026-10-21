let listaCompra = ["Peras", "Manzanas", "Kiwis", "Plátanos", "Mandarinas"];

// Eliminar Manzanas
listaCompra.splice(1,1);

console.log(listaCompra);

// Añadir Naranjas y Sandias despues de Plátanos
listaCompra.splice(3,0,"Naranjas","Sandias");

console.log(listaCompra);

// Reemplazar kiwis con Cerezas y nisperos

listaCompra.splice(1,1,"Cerezas","Nisperos");

console.log(listaCompra);

