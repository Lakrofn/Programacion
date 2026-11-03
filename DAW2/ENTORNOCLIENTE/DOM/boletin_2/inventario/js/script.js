const inventory = {
  items: [
    { name: "Laptop", quantity: 5, price: 1200 },
    { name: "Mouse", quantity: 25, price: 20 },
    { name: "Keyboard", quantity: 15, price: 50 },
  ],
  totalItems: 0,
};
function updateTotalItems() {
  inventory.totalItems = inventory.items.reduce(
    (sum, p) => sum + p.quantity,
    0,
  );
}
function addItem(name, quantity, price) {
  const found = inventory.items.find(
    (p) => p.name.toLowerCase() === name.toLowerCase(),
  );
  if (found) {
    found.quantity += quantity;
    found.price = price;
  } else inventory.items.push({ name, quantity, price });
  updateTotalItems();
}
function removeItem(name) {
  inventory.items = inventory.items.filter(
    (p) => p.name.toLowerCase() !== name.toLowerCase(),
  );
  updateTotalItems();
}

const tbody = document.getElementById("items");
function addRow(product) {
  const tr = document.createElement("tr");
  if (product.price > 50) tr.classList.add("caro");
  [product.name, product.quantity, product.price.toFixed(2) + " €"].forEach(
    (value) => {
      const td = document.createElement("td");
      td.textContent = value;
      tr.appendChild(td);
    },
  );
  const actions = document.createElement("td");
  const button = document.createElement("button");
  button.type = "button";
  button.textContent = "Eliminar";
  button.addEventListener("click", () => {
    removeItem(product.name);
    renderTable();
  });
  actions.appendChild(button);
  tr.appendChild(actions);
  tbody.appendChild(tr);
}
function renderTable() {
  tbody.replaceChildren();
  inventory.items.forEach(addRow);
}
document.getElementById("addProduct").addEventListener("submit", (event) => {
  event.preventDefault();
  const name = document.getElementById("name").value.trim();
  const quantity = Number(document.getElementById("quantity").value);
  const price = Number(document.getElementById("price").value);
  if (
    !name ||
    !Number.isInteger(quantity) ||
    quantity <= 0 ||
    !Number.isFinite(price) ||
    price <= 0
  )
    return;
  addItem(name, quantity, price);
  renderTable();
  event.target.reset();
});
updateTotalItems();
renderTable();
