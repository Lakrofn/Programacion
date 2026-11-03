let inventory = [
    { name: "Teclado", quantity: 15, price: 29.99 },
    { name: "Monitor", quantity: 6, price: 189.5 },
    { name: "Ratón", quantity: 25, price: 12.9 },
    { name: "Auriculares", quantity: 10, price: 55 }
];

function addItem(name, quantity, price) {
    inventory.push({ name, quantity, price });
    updateTable();
}

function removeItem(name) {
    inventory = inventory.filter(item => item.name !== name);
    updateTable();
}

document.getElementById("addProduct").addEventListener("submit", (event) => {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const quantity = parseInt(document.getElementById("quantity").value);
    const price = parseFloat(document.getElementById("price").value);
    addItem(name, quantity, price);
    document.getElementById("addProduct").reset();
});

function updateTable() {
    const tbody = document.getElementById("items");
    tbody.innerHTML = "";

    inventory.forEach(item => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>${item.price.toFixed(2)}</td>
            <td><button onclick="removeItem('${item.name}')">Eliminar</button></td>
        `;
        tbody.appendChild(tr);
    });
}

updateTable();