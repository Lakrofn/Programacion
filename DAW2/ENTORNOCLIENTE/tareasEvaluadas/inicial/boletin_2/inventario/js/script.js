const inventory = [
    { name: "Teclado", quantity: 15, price: 29.99 },
    { name: "Monitor", quantity: 6, price: 189.5 },
    { name: "Ratón", quantity: 25, price: 12.9 },
    { name: "Auriculares", quantity: 10, price: 55 }
];

const form = document.getElementById("addProduct");
const tbody = document.getElementById("items");

function renderTable() {
    tbody.innerHTML = "";

    inventory.forEach((item, index) => {
        const tr = document.createElement("tr");

        const tdName = document.createElement("td");
        tdName.textContent = item.name;

        const tdQuantity = document.createElement("td");
        tdQuantity.textContent = item.quantity;

        const tdPrice = document.createElement("td");
        tdPrice.textContent = item.price.toFixed(2) + " €";

        const tdActions = document.createElement("td");
        const btnDelete = document.createElement("button");
        btnDelete.type = "button";
        btnDelete.textContent = "Eliminar";
        btnDelete.addEventListener("click", () => removeItem(index));
        tdActions.appendChild(btnDelete);

        tr.append(tdName, tdQuantity, tdPrice, tdActions);

        if (item.price > 50) {
            tr.classList.add("expensive");
        }

        tbody.appendChild(tr);
    });
}

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const quantity = parseInt(document.getElementById("quantity").value, 10);
    const price = parseFloat(document.getElementById("price").value);

    if (!name || isNaN(quantity) || isNaN(price)) return;

    inventory.push({ name, quantity, price }); 
    renderTable();                              
    form.reset();
    document.getElementById("name").focus();
});

function removeItem(index) {
    inventory.splice(index, 1);
    renderTable();
}

renderTable();