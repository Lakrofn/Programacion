let ocultar = " ";
let mostrar = document.querySelectorAll("p")[0].textContent;

document.querySelectorAll("a")[0].addEventListener("click", function () {
    let actual = document.querySelectorAll("p")[0].textContent;
    if (actual == ocultar) {
        document.querySelectorAll("p")[0].textContent = mostrar;
        document.querySelectorAll("a")[0].textContent = "Ocultar contenidos";
    } else {
        document.querySelectorAll("p")[0].textContent = ocultar;
        document.querySelectorAll("a")[0].textContent = "Mostrar contenidos";
    }
});

document.querySelectorAll("a")[1].addEventListener("click", function () {
    let actual = document.querySelectorAll("p")[1].textContent;
    if (actual == ocultar) {
        document.querySelectorAll("p")[1].textContent = mostrar;
        document.querySelectorAll("a")[1].textContent = "Ocultar contenidos";
    } else {
        document.querySelectorAll("p")[1].textContent = ocultar;
        document.querySelectorAll("a")[1].textContent = "Mostrar contenidos";
    }
});

document.querySelectorAll("a")[2].addEventListener("click", function () {
    let actual = document.querySelectorAll("p")[2].textContent;
    if (actual == ocultar) {
        document.querySelectorAll("p")[2].textContent = mostrar;
        document.querySelectorAll("a")[2].textContent = "Ocultar contenidos";
    } else {
        document.querySelectorAll("p")[2].textContent = ocultar;
        document.querySelectorAll("a")[2].textContent = "Mostrar contenidos";
    }
});