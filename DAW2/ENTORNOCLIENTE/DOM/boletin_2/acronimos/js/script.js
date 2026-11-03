const input = document.getElementById('phrase');
const results = document.getElementById('results');

function acronym(text) {
    return text.trim()
        .split(/\s+/)
        .filter(Boolean)
        .map(w => w[0].toUpperCase())
        .join('');
}

function generateAcronym() {
    const phrase = input.value.trim();

    if (!phrase) return;

    const li = document.createElement('li');
    li.textContent = phrase + ' → ' + acronym(phrase);

    if (phrase.split(/\s+/).length > 3) {
        li.classList.add('larga');
    }

    results.appendChild(li);
    input.value = '';
    input.focus();
}

function clearResults() {
    results.replaceChildren();
    input.value = '';
    input.focus();
}

document.getElementById('submit')
    .addEventListener('click', generateAcronym);

document.getElementById('reset')
    .addEventListener('click', clearResults);