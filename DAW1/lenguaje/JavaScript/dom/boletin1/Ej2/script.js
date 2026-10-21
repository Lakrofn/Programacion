let figura = document.getElementById("figuras");
let radio = document.getElementById("radio");
let altura = document.getElementById("altura");
let base = document.getElementById("base");

figura.addEventListener("change", function() {
document.getElementById("input1").classList.add("oculto");
document.getElementById("input2").classList.add("oculto");
document.getElementById("input3").classList.add("oculto");

if (this.value === "1") {
    document.getElementById("input1").classList.remove("oculto");
    document.getElementById("calcular").addEventListener("click", function() {
        console.log("El área es " + (base.value * altura.value) / 2);
        alert("El área es " + (base.value * altura.value) / 2);
    });
} else if (this.value === "2") {
    document.getElementById("input2").classList.remove("oculto");
    document.getElementById("calcular").addEventListener("click", function() {
        console.log("El área es " + (base.value * altura.value));
        alert("El área es " + (base.value * altura.value));
    });
} else if (this.value === "3") {
    document.getElementById("input3").classList.remove("oculto");
    document.getElementById("calcular").addEventListener("click", function() {
        console.log("El área es " + (radio.value * (radio.value * 2) * Math.PI));
        alert("El área es " + (radio.value * (radio.value * 2) * Math.PI));
    });
}
});