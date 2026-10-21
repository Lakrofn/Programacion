const inventory = {
    items: [
        { name: 'Laptop', quantity: 5, price: 1200 },
        { name: 'Mouse', quantity: 25, price: 20 },
        { name: 'Keyboard', quantity: 15, price: 50 }
    ],
    totalItems: 0
};
// TODO: updateTotalItems, addItem, removeItem.
// TODO: filtros y suma de cantidades.

//1.

console.log("Unicades iniciales: " + (inventory.totalItems = inventory.items.reduce((total, item) => total + item.quantity, 0)));

//2.

function addItem(name, quantity, price) {
    let exists = false;
    for (let i = 0; i < inventory.items.length && !exists; i++) {
        if (inventory.items[i].name.toLowerCase() === name.toLowerCase()) {
            inventory.items[i].quantity += quantity;
            exists = true;
        }
    }

    if (!exists) {
        inventory.items.push({ name: name, quantity: quantity, price: price });
    }
}


// 3.
function removeItem(name) {
    for (let i = 0; i < inventory.items.length; i++) {
        if (inventory.items[i].name.toLowerCase() === name.toLowerCase()) {
            inventory.items.splice(i, 1);
        }
    }
}


// 4.

console.log("Articulos caros: ");
console.log(inventory.items
    .filter(item => item.price > 50));

addItem('headset', 22, 20);

console.log("Unidades con o " + (inventory.items
    .filter(item => item.name.toLowerCase().includes('o'))
    .reduce((total, item) => total + item.quantity, 0)));


// Comprobación

addItem('mouse', 22, 20);

console.log("Tras añadir mouse: ");
console.log((inventory.items));

removeItem('Keyboard');

console.log("Tras eliminar keyboard: ");
console.log((inventory.items));