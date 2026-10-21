const students = [
  { id: 1, name: "Carlos", age: 22 },
  { id: 2, name: "Ana", age: 20 },
  { id: 3, name: "Luis", age: 25 },
  { id: 4, name: "Elena", age: 18 },
  { id: 5, name: "María", age: 21 },
];

function findStudents(array, id){
    return array.filter(s => s.id === id)
    .map(p => p.name);
}

console.log(findStudents(students, 1));


function increaseAge(array){
    for(let i = 0; i < array.length; i++){
        array[i].age += 1;
    }
    return array;
}

console.log(increaseAge(students));
