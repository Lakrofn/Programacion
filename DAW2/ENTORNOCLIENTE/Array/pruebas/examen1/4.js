const transactions = [
  { type: "ingreso", amount: 1000 },
  { type: "egreso", amount: 500 },
  { type: "ingreso", amount: 200 },
  { type: "ingreso", amount: 300 },
  { type: "egreso", amount: 150 },
];

let amounts = transactions.filter(t => t.type === "egreso")
.map(a => -a.amount);

for(let i = 0; i < transactions.length; i++){
    if(transactions[i].type == "ingreso"){
        amounts.push(transactions[i].amount);
    }
}

console.log(amounts.reduce((total, a) => total += a,0));