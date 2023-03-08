// muestra solo el boton seleccionado.
$(document).ready(() =>{
    $('#map').show();
    $('#graficos').hide();
    $('#contactos').hide();
   $('#mostrarmap').click(function(){
    $('#map').show();
    $('#graficos').hide();
    $('#contactos').hide();
      });
$('#mostrargraficos').click(function(){
    $('#map').hide();
    $('#graficos').show();
    $('#contactos').hide();
       });
$('#mostrarcontactos').click(function(){
    $('#map').hide();
    $('#graficos').hide();
    $('#contactos').show();
           });
});

// funcion api para meter datos en el mapa y adentro esta la funcion del mapa tambien

let latitud = 0;
let longitud = 0;
let nombre = '';
//declaro al mapa en esta zona
var map = L.map('map').setView([-36,-80], 6);
var marker = 0;
//funcion ajax para recorrer la api generada anteriormente y sacar los datos que necesito de las estacines
const url = 'http://127.0.0.1:8000/listaEstaciones/';
$.ajax({
url: url,
type: 'GET',
dataType: 'json',
success: (data) => {
    for (i in data.estaciones){
        //este for es para recorrer la api y sacar los datos necesarios
        //console.log(data.estaciones[i].nombre);
        
        latitud = data.estaciones[i].latitud;
        longitud = data.estaciones[i].longitud;
        nombre = data.estaciones[i].nombre;
        marker = L.marker([latitud, longitud]).addTo(map);
        marker.bindPopup("NOMBRE :" + nombre).openPopup();
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
        
    
        };
       
},

error: () => {
alert('Error vuelva a intentarlo mas tarde.');
}

});







