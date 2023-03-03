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




// funcion de mapa
var map = L.map('map').setView([-34.61315, -58.37723], 10);
var marker = L.marker([-34.61315, -58.37723]).addTo(map);
marker.bindPopup("<b>Hello world!</b><br>I aammmmnnmmmm popup.").openPopup();
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);



// funcion api de bitcoin para probar
const url = 'http://127.0.0.1:8000/ListaEstaciones/';
$.ajax({
url: url,
type: 'GET',
dataType: 'json',
success: (data) => {
console.log(data.estaciones);
$('#graficos').text(data.nombre ,'+');
},
error: () => {
alert('Error vuelva a intentarlo mas tarde.');
}
});




