const personas = [
{ nombre: "Alvaro", apellido: "Cruces" },
{ nombre: "Ana", apellido: "Gómez" },
{ nombre: "Carlos", apellido: "Pérez" },
{ nombre: "Beatriz", apellido: "Gómez" }
];

personas.sort((a, b) => {
if (a.apellido < b.apellido) return -1;
if (a.apellido > b.apellido) return 1;

  // Si el apellido es igual, ordenar por nombre
if (a.nombre < b.nombre) return -1;
if (a.nombre > b.nombre) return 1;

return 0;
});

console.log(personas);
