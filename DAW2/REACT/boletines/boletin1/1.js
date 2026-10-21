const estadoApp = {
usuario: "Admin",
carrito: [
{ id: 1, articulo: "Ratón", cantidad: 1 },
{ id: 2, articulo: "Teclado", cantidad: 1 }
],
total: 50
};

const nuevoEstadoApp = {...estadoApp,
    carrito: estadoApp.carrito.map(art =>
        art.articulo === "Teclado" ? {...art , cantidad: art.cantidad + 1} : art
    )
};

console.log(nuevoEstadoApp);