const gradebook = {
    students: [
        { name: 'Ana', grades: [8, 7, 9], average: 0 },
        { name: 'Luis', grades: [6, 8, 6], average: 0 },
        { name: 'Maria', grades: [9, 10, 9], average: 0 }
    ]
};
// TODO: calculateAverage, addStudent, addGrade.
// TODO: filtros y ordenación.

//1.

function calculateAverage() {
    for (let i = 0; i < gradebook.students.length; i++) {
        gradebook.students[i].average =
            gradebook.students[i].grades
                .reduce((total, grade) => total + grade, 0) / gradebook.students[i].grades.length;
    }
}

calculateAverage();


// 2

function addStudent(name) {
    gradebook.students.push({ name: name, grades: [], average: 0 });
}


// 3

function addGrade(studentName, grade) {
    const student = gradebook.students.find(student => student.name === studentName);
    student.grades.push(grade);
    calculateAverage();
}


// 4

console.log("Promedio mayor que 8: ");
console.log(gradebook.students.filter(student => student.average > 8));

console.log("Alguna nota mayor que 9: ");
console.log(gradebook.students.filter(student => student.grades.includes(9)).map(student => student.name));


gradebook.students.sort((a, b) => b.average - a.average);


console.log(gradebook.students);



addStudent('Pablo');
addGrade('Pablo', 9);
console.log("Despues de añadir: ");
console.log(gradebook.students);