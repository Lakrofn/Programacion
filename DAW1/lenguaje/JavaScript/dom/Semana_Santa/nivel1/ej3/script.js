let contador = document.getElementById("contador");

contador.addEventListener("click", function(){
    contador.innerHTML = parseInt(contador.innerHTML) + 1;
})