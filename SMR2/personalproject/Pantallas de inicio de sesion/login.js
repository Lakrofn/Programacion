let registerBtn = document.getElementById("register");
let contenedor = document.getElementById("contenedor");
let loginBtn = document.getElementById("login");

registerBtn.addEventListener("click", () => {
    contenedor.classList.add("active");
});

loginBtn.addEventListener("click", () => {
    contenedor.classList.remove("active");
});