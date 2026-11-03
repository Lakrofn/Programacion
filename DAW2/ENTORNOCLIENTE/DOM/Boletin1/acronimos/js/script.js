// TODO: leer frase, crear acrónimo, añadir un li a #results.
// TODO: marcar las frases de más de 3 palabras con classList.add("larga").
// TODO: limpiar lista y campo de texto.
const input = document.getElementById('phrase');
const lista = document.getElementById('results');

function acronimo(texto) {
    return texto.trim()
        .split(" ")
        .map(palabra => palabra[0].toUpperCase())
        .join('');
}

document.getElementById('submit').addEventListener('click' , () => {
    const li = document.createElement('li');
    li.textContent = input.value.trim() + " → " + acronimo(input.value.trim());

    if (input.value.trim().split(" ").length > 3) {
        li.classList.add('larga');
    }
    lista.appendChild(li);
    input.value = '';
});

document.getElementById('reset').addEventListener('click', () => {
    while (lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }
    input.value = '';
});