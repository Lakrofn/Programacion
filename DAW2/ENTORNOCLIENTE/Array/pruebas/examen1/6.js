const fullNames = [
  "John Smith",
  "Alice Johnson",
  "Michael Brown",
  "Emily Davis",
  "David Johnson",
];

function getInitials(array){
    let initial1 = "";
    let initial2 = "";
    for(let i = 0; i < array.length; i++){
        for(let j = 0; j < array[i].length; j++){
            if(j == 0){
                initial1 = array[i][j]
            }else if(array[i][j-1] == " "){
                initial2= array[i][j];
            }
        }
        console.log(initial1 + "." + initial2);
    }
}

console.log(getInitials(fullNames));


function getLongestName(array){
    array = array.sort((a,b) => a.lenght > b.lenght);
    return array[0];
}

console.log(getLongestName(fullNames));


function findNamesStartingWith(array, word){
    for (let i = 0; i < array.length; i++){
        if(array[i].toLowerCase().startsWith(word.toLowerCase())){
            return array[i];
        }
    }
}

 console.log(findNamesStartingWith(fullNames, "a"));