const respuestaAPI = {
    status: 200,
    data: {
        usuario: {
            id: 105,
            nombre: "Sara",
            contacto: {
                email: "sara@ejemplo.com",
                
            }
        }
    }
};

const {data: {usuario: {nombre, contacto: {email, tlf = "No proporcionado"}}}} = respuestaAPI;

console.log(nombre, email, tlf);
