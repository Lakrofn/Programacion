// ============================================================
// 1. DATOS
// ============================================================
const gradebook = {
    students: [
        { name: 'Ana',   grades: [8, 7, 9],   average: 0 },
        { name: 'Luis',  grades: [6, 8, 6],   average: 0 },
        { name: 'Maria', grades: [9, 10, 9],  average: 0 }
    ]
};

const MIN_GRADE = 0;
const MAX_GRADE = 10;
const HIGH_AVERAGE = 8;

// ============================================================
// 2. LÓGICA
// ============================================================
function calculateAverage() {
    gradebook.students.forEach(student => {
        const { grades } = student;
        student.average = grades.length
            ? grades.reduce((sum, n) => sum + n, 0) / grades.length
            : 0;
    });
}

function addStudent(name) {
    const exists = gradebook.students.some(
        s => s.name.toLowerCase() === name.toLowerCase()
    );
    if (exists) return false;

    gradebook.students.push({ name, grades: [], average: 0 });
    return true;
}

function isValidGrade(grade) {
    return Number.isFinite(grade) && grade >= MIN_GRADE && grade <= MAX_GRADE;
}

function addGrade(name, grade) {
    const student = gradebook.students.find(s => s.name === name);
    if (!student || !isValidGrade(grade)) return false;

    student.grades.push(grade);
    calculateAverage();
    return true;
}

// ============================================================
// 3. RENDERIZADO
// ============================================================
const list = document.getElementById('students');

function buildInfoText(student) {
    const hasGrades = student.grades.length > 0;
    const grades = student.grades.join(', ') || 'sin notas';
    const average = hasGrades ? student.average.toFixed(2) : 'sin calcular';

    return `${student.name} | Notas: ${grades} | Media: ${average}`;
}

function buildGradeForm(student) {
    const form = document.createElement('form');
    form.hidden = true;

    const input = document.createElement('input');
    input.type = 'number';
    input.min = MIN_GRADE;
    input.max = MAX_GRADE;
    input.step = '0.1';
    input.required = true;

    const saveButton = document.createElement('button');
    saveButton.textContent = 'Guardar nota';

    form.append(input, saveButton);

    form.addEventListener('submit', event => {
        event.preventDefault();
        if (addGrade(student.name, Number(input.value))) {
            renderStudents();
        }
    });

    return form;
}

function buildStudentItem(student) {
    const li = document.createElement('li');

    if (student.grades.length && student.average > HIGH_AVERAGE) {
        li.classList.add('sobresaliente');
    }

    const info = document.createElement('span');
    info.textContent = buildInfoText(student);

    const form = buildGradeForm(student);

    const toggleButton = document.createElement('button');
    toggleButton.type = 'button';
    toggleButton.textContent = 'Añadir nota';
    toggleButton.addEventListener('click', () => {
        form.hidden = !form.hidden;
    });

    li.append(info, toggleButton, form);
    return li;
}

function renderStudents() {
    list.replaceChildren(
        ...gradebook.students.map(buildStudentItem)
    );
}

// ============================================================
// 4. EVENTOS
// ============================================================
document.getElementById('addStudent').addEventListener('submit', event => {
    event.preventDefault();

    const name = document.getElementById('studentName').value.trim();

    if (name && addStudent(name)) {
        renderStudents();
        event.target.reset();
    }
});

// ============================================================
// 5. INICIALIZACIÓN
// ============================================================
calculateAverage();
renderStudents();