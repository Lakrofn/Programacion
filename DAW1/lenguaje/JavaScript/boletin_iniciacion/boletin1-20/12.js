const personas = [
{ nombre: "Alvaro", edad: 23, sexo: "Masculino" },
{ nombre: "Maria", edad: 24, sexo: "Femenino" },
{ nombre: "Juan", edad: 25, sexo: "Masculino" },
];

console.log(personas.sort((a, b) => a.edad - b.edad));