// Copia aquí las funciones de librería del boletín 1.
// TODO: representar tabla, añadir, eliminar, filtrar y ordenar.
// TODO: actualizar opciones del selector si aparecen nuevas categorías.
const bookStore = {
    books: [
        { 
            title: '1984',    
            author: 'George Orwell',     
            price: 15, 
            category: 'Fiction' 
        },
        { title: 'Sapiens', author: 'Yuval Noah Harari', price: 20, category: 'Non-fiction' }
    ]
};

let order = ''; // '', 'asc' o 'desc'

let filter = document.getElementById('categoryFilter').value;




document.getElementById('categoryFilter').addEventListener('change', () => {
    filter = document.getElementById('categoryFilter').value;
    updateBooks();
});

document.getElementById('asc').addEventListener('click', () => {
    order = 'asc';
    updateBooks();
});

document.getElementById('desc').addEventListener('click', () => {
    order = 'desc';
    updateBooks();
});

function addBook(title, author, price, category) {
    bookStore.books.push({ title, author, price, category });
}

function removeBook(book) {
    bookStore.books = bookStore.books.filter(b => b !== book);
}

document.getElementById('addBook').addEventListener('submit', (event) => {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const price = parseFloat(document.getElementById('price').value);
    const category = document.getElementById('category').value;

    if (!filter.includes(category)) {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        document.getElementById('categoryFilter').appendChild(option);
    }
    addBook(title, author, price, category);
    updateBooks(); // Actualizar la tabla después de añadir un libro
});

function updateBooks() {
    let tbody = document.getElementById('books');
    tbody.innerHTML = ''; // Limpiar la tabla antes de actualizarla
    
    let filteredBooks = bookStore.books.filter(b => !filter || b.category === filter);

    // Aplicar ordenamiento
    if (order === 'asc') {
        filteredBooks.sort((a, b) => a.price - b.price);
    } else if (order === 'desc') {
        filteredBooks.sort((a, b) => b.price - a.price);
    }

    filteredBooks.forEach(book => {
        let row = document.createElement('tr');
        
        row.innerHTML = `
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.price}</td>
            <td>${book.category}</td>
            <td><button id="deleteBtn">Eliminar</button></td>
        `;
        let deleteBtn = row.querySelector('#deleteBtn');
        deleteBtn.addEventListener('click', () => {
            removeBook(book);
            updateBooks(); // Actualizar la tabla después de eliminar un libro
        });
        
        tbody.appendChild(row);
        

    }); 
}

updateBooks(); // Llamar a la función para mostrar los libros al cargar la página