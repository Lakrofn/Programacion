const phrases = [
    { phrase: 'Hyper Text Markup Language' },
    { phrase: 'Cascading Style Sheets' },
    { phrase: 'Object Oriented Programming' }
];
// TODO: generar acrónimos con map y filtrar frases largas.


//1.

function generateAcronyms(phrases) {
    for (let i = 0; i < phrases.length; i++) {
        let acronyms = [];
        acronyms.push(phrases[i].phrase.split(' ').map(word => word[0].toUpperCase()).join(''));
        phrases[i].acronym = acronyms.join('');
    }
}

generateAcronyms(phrases)

console.log("Todos: ");
console.log(phrases);

// 2
console.log("Acrónimos por separado con map: ");
console.log(phrases.map(phrase => phrase.acronym));

// 3
console.log("Más de tres palabras: ");
console.log(phrases.filter(phrase => phrase.phrase.split(' ').length > 3))