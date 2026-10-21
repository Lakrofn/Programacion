let notas = [5.2, 3.9, 6, 9.75, 7.5, 3, 6.5, 9.75];


const aprobados = notas.filter(nota => nota >= 5);

console.log(aprobados);

const media = notas.reduce((total, nota) => total + nota, 0) / notas.length;

console.log(media);

const notaMasAlta = Math.max(...notas);

console.log(notaMasAlta);

const set = new Set(notas);

console.log(set);

const map = notas.map(nota => "Nota: " + nota);

console.log(map);

const some = notas.some(nota => nota < 5);

console.log(some);

const every = notas.every(nota => nota >= 3);

console.log(every);