const bookStore = {
    books: [
        { title: '1984', author: 'George Orwell', price: 15, category: 'Fiction' },
        { title: 'Sapiens', author: 'Yuval Noah Harari', price: 20, category: 'Non-fiction' }
    ]
};
// TODO: addBook, getBooksByCategory, reduce, filter, sort.

// 1
function addBook(title, author, price, category) {
    bookStore.books.push({ title: title, author: author, price: price, category: category });
}



// 2

function getBooksByCategory(category) {
    return bookStore.books.filter(book => book.category === category);
}


// 3

console.log("Precio total: ");
console.log(bookStore.books.reduce((total, book) => total + book.price, 0));

// 4
console.log("Mas de 18: ");

console.log(bookStore.books.filter(book => book.price > 18));

// 5

console.log("Orden descendente: ");
bookStore.books.sort((a, b) => b.price - a.price);

console.log(bookStore.books);

console.log("Fiction: ");
addBook('Dune', 'Frank Herbert', 25, 'Fiction');
console.log(getBooksByCategory('Fiction'));