const products = [
  { id: 1, name: "Camisa", price: 25 },
  { id: 2, name: "Pantalón", price: 40 },
  { id: 3, name: "Zapatos", price: 60 },
  { id: 4, name: "Bufanda", price: 15 },
  { id: 5, name: "Gorra", price: 10 },
];

function expensiveProducts(array){
    return array.filter(product => product.price > 30);
}

console.log(expensiveProducts(products));

function productsName(array){
    return array.map(p => p.name);
}

console.log(productsName(products));
