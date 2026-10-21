const alumnos = [
    { nombre: "Vmax", edad: 18 },
    { nombre: "cabesa", edad: 23 },
    { nombre: "chabe", edad: 21 },
    { nombre: "chinuga", edad: 19 },
    { nombre: "lakro", edad: 24 },
];

alumnos.sort((a, b) => a.edad - b.edad);

console.log(alumnos);