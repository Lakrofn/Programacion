const gradebook = {
    students: [
        { name: 'Ana', grades: [8, 7, 9], average: 0 },
        { name: 'Luis', grades: [6, 8, 6], average: 0 },
        { name: 'Maria', grades: [9, 10, 9], average: 0 }
    ]
};

function calculateAverage() {
    for (let i = 0; i < gradebook.students.length; i++) {
        const grades = gradebook.students[i].grades;
        gradebook.students[i].average = grades.length === 0
            ? 0
            : grades.reduce((total, grade) => total + grade, 0) / grades.length;
    }
}

function addStudent(name) {
    gradebook.students.push({ name: name, grades: [], average: 0 });
}

function addGrade(name, grade) {
    const student = gradebook.students.find(student => student.name === name);
    student.grades.push(grade);
    calculateAverage();
}


const sobresaliente = 8;

const form = document.getElementById('addStudent');
const name = document.getElementById('name');
const list = document.getElementById('students');

function create(student) {
    const li = document.createElement('li');
    li.dataset.name = student.name;

    const title = document.createElement('strong');
    title.textContent = student.name;

    const gradesSpan = document.createElement('span');
    gradesSpan.className = 'grades';

    const avgSpan = document.createElement('span');
    avgSpan.className = 'average';

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.textContent = 'Añadir nota';

    const gradeForm = addGrade(student.name);
    gradeForm.hidden = true;

    btn.addEventListener('click', () => {
        gradeForm.hidden = !gradeForm.hidden;
        if (!gradeForm.hidden) gradeForm.querySelector('input').focus();
    });

    li.append(title, gradesSpan, avgSpan, ' ', btn, gradeForm);
    update(li, student);
    return li;
}

function update(li, student) {
    li.querySelector('.grades').textContent =
        ` · Notas: ${student.grades.length ? student.grades.join(', ') : 'sin notas'}`;
    li.querySelector('.average').textContent =
        ` · Media: ${student.grades.length ? student.average.toFixed(2) : '—'}`;

    li.classList.toggle('sobresaliente', student.average > sobresaliente);
}

function renderStudents() {
    calculateAverage();
    list.innerHTML = '';
    gradebook.students.forEach(student => list.appendChild(create(student)));
}

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = inputName.value.trim();
    if (!name) return;

    if (gradebook.students.some(s => s.name.toLowerCase() === name.toLowerCase())) {
        alert(`El alumno "${name}" ya existe.`);
        return;
    }

    addStudent(name);
    const student = gradebook.students[gradebook.students.length - 1];
    list.appendChild(create(student));

    form.reset();
    inputName.focus();
});

function addGrade(name) {
    const f = document.createElement('form');
    f.className = 'grade-form';

    const input = document.createElement('input');
    input.type = 'number';
    input.min = '0';
    input.max = '10';
    input.step = '0.01';
    input.placeholder = 'Nota (0-10)';
    input.required = true;

    const submit = document.createElement('button');
    submit.textContent = 'Guardar';

    f.append(input, ' ', submit);

    f.addEventListener('submit', (e) => {
        e.preventDefault();

        const grade = parseFloat(input.value);
        if (Number.isNaN(grade) || grade < 0 || grade > 10) {
            alert('Introduce una nota entre 0 y 10.');
            return;
        }

        addGrade(name, grade); 

        const student = gradebook.students.find(s => s.name === name);
        const li = f.closest('li');
        update(li, student);

        f.reset();
        f.hidden = true;
    });

    return f;
}

renderStudents();