const peliculas = [
{ titulo: "Dune", año: 2021, valoracion: 8.0, vista: true },
{ titulo: "El Padrino", año: 1972, valoracion: 9.2, vista: false },
{ titulo: "Matrix", año: 1999, valoracion: 8.7, vista: true },
{ titulo: "Tenet", año: 2020, valoracion: 7.3, vista: false }
];

const peliculasJSX = peliculas.filter(pel => pel.vista).map(pel => <li>{pel.titulo}</li>);

console.log(peliculasJSX);