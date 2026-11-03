// ============================================================
// 1. DATOS
// ============================================================
const bookStore = {
    books: [
        { title: '1984',    author: 'George Orwell',     price: 15, category: 'Fiction' },
        { title: 'Sapiens', author: 'Yuval Noah Harari', price: 20, category: 'Non-fiction' }
    ]
};

let order = ''; // '', 'asc' o 'desc'

// ============================================================
// 2. LÓGICA
// ============================================================
function addBook(title, author, price, category) {
    bookStore.books.push({ title, author, price, category });
}

function removeBook(book) {
    const index = bookStore.books.indexOf(book);
    if (index !== -1) bookStore.books.splice(index, 1);
}

function getBooksByCategory(category) {
    return bookStore.books.filter(b => b.category === category);
}

function getCategories() {
    return [...new Set(bookStore.books.map(b => b.category))].sort();
}

function sortBooks(books) {
    if (order === 'asc')  return books.sort((a, b) => a.price - b.price);
    if (order === 'desc') return books.sort((a, b) => b.price - a.price);
    return books;
}

function getVisibleBooks() {
    const books = filter.value
        ? getBooksByCategory(filter.value)
        : [...bookStore.books];
    return sortBooks(books);
}

function isValidBook({ title, author, price, category }) {
    return title && author && category && Number.isFinite(price) && price >= 0;
}

// ============================================================
// 3. RENDERIZADO
// ============================================================
const tbody  = document.getElementById('books');
const filter = document.getElementById('categoryFilter');

function createOption(value, text) {
    const option = document.createElement('option');
    option.value = value;
    option.textContent = text;
    return option;
}

function updateCategories() {
    const current = filter.value;

    filter.replaceChildren(
        createOption('', 'Todas'),
        ...getCategories().map(category => createOption(category, category))
    );

    filter.value = current;
}

function createCell(text) {
    const td = document.createElement('td');
    td.textContent = text;
    return td;
}

function createDeleteCell(book) {
    const td = document.createElement('td');
    const button = document.createElement('button');

    button.type = 'button';
    button.textContent = 'Eliminar';
    button.addEventListener('click', () => {
        removeBook(book);
        updateCategories();
        renderBooks();
    });

    td.appendChild(button);
    return td;
}

function createBookRow(book) {
    const tr = document.createElement('tr');

    tr.append(
        createCell(book.title),
        createCell(book.author),
        createCell(book.price.toFixed(2) + ' €'),
        createCell(book.category),
        createDeleteCell(book)
    );

    return tr;
}

function renderBooks() {
    tbody.replaceChildren(...getVisibleBooks().map(createBookRow));
}

// ============================================================
// 4. EVENTOS
// ============================================================
function setOrder(newOrder) {
    order = newOrder;
    renderBooks();
}

document.getElementById('addBook').addEventListener('submit', event => {
    event.preventDefault();

    const book = {
        title:    document.getElementById('title').value.trim(),
        author:   document.getElementById('author').value.trim(),
        price:    Number(document.getElementById('price').value),
        category: document.getElementById('category').value.trim()
    };

    if (!isValidBook(book)) return;

    addBook(book.title, book.author, book.price, book.category);
    updateCategories();
    renderBooks();
    event.target.reset();
});

filter.addEventListener('change', renderBooks);
document.getElementById('asc').addEventListener('click',  () => setOrder('asc'));
document.getElementById('desc').addEventListener('click', () => setOrder('desc'));

// ============================================================
// 5. INICIALIZACIÓN
// ============================================================
updateCategories();
renderBooks();