const persons = [
  { name: "Juan", age: 25 },
  { name: "Ana", age: 30 },
  { name: "Luis", age: 25 },
  { name: "María", age: 35 },
  { name: "Luis", age: 25 },
];

function removeDuplicates(array){
    let noDuplicates = new Set(array);
    return noDuplicates;
}

console.log(removeDuplicates(persons));