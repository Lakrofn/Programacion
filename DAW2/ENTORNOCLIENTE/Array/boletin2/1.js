let productos = 
[
  { id: 1, nombre: 'Teclado', precio: 25.5, stock: 10 },
  { id: 2, nombre: 'Ratón', precio: 15.0, stock: 0 },
  { id: 3, nombre: 'Monitor', precio: 150.0, stock: 5 },
  { id: 4, nombre: 'USB', precio: 8.0, stock: 25 }
];

const filtrado = productos.filter(producto => producto.stock > 0);

console.log(filtrado);

const mapeado = filtrado.map(producto => producto.nombre);

console.log(mapeado);

const reduce = filtrado.reduce((total, producto) => total + producto.precio, 0);

console.log(reduce);

function buscarProducto(nombre) {
    return productos.find(producto => producto.nombre.toLowerCase() === nombre.toLowerCase());
}

console.log(buscarProducto('Teclado'));