const datosUsuario = {
id: 99,
nombre: "Elena",
preferencias: {
idioma: "es",
tema: "oscuro"
},
suscripcion: "Premium"
};


const {nombre, preferencias: {tema}} = datosUsuario;

console.log(nombre, tema);
