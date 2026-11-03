const gradebook = {
    students: [
        { name: 'Ana', grades: [8, 7, 9], average: 0 },
        { name: 'Luis', grades: [6, 8, 6], average: 0 },
        { name: 'Maria', grades: [9, 10, 9], average: 0 }
    ]
};

function calculateAverage() {
    gradebook.students.forEach(student => {
        let totalGrades = student.grades.length;
        student.average = student.grades.reduce((a, b) => a + b, 0) / totalGrades;
    });
}

calculateAverage();

function insertStudent(name) {
    gradebook.students.push({ name, grades: [], average: 0 });
    updateList();
}

document.getElementById("addStudent").addEventListener("click", () => {
    const nameInput = document.getElementById("studentName");
    if (nameInput.value.trim() !== '') {
        insertStudent(nameInput.value);

    }
    nameInput.value = '';
});

function updateList() {
    const list = document.getElementById('students');
    list.innerHTML = '';
    gradebook.students.forEach(student => {
        const li = document.createElement('li');
        const button = document.createElement('button');
        button.textContent = 'Añadir nota';
        button.addEventListener('click', () => {
            const grade = document.createElement('input');
            grade.type = 'number';
            const submit = document.createElement('button');
            submit.textContent = 'Añadir';
            submit.addEventListener('click', () => {
                const gradeValue = parseFloat(grade.value);
                if (!isNaN(gradeValue) && gradeValue >= 0 && gradeValue <= 10) {
                    student.grades.push(gradeValue);
                    calculateAverage();
                    updateList();
                }
            });
            li.appendChild(document.createElement('br'));
            li.appendChild(grade);
            li.appendChild(document.createElement('br'));
            li.appendChild(submit);
        });
        (student.average >= 8) ? li.style.color = 'green' : (student.average >= 5) ? li.style.color = 'orange' : li.style.color = 'red';
        li.textContent = student.name + ' | Notas: ' + student.grades.join(', ') + ' | Media: ' + (student.average) + " ";

        li.appendChild(button);
        list.appendChild(li);
    });
}

updateList();