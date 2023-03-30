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
var map = L.map('map').setView([-41.316356,-58.172720], 6);
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
        
        nombre = data.estaciones[i].nombre;
        marker = L.marker([data.estaciones[i].latitud, data.estaciones[i].longitud]).addTo(map);
        marker.bindPopup('<p>NOMBRE: '+data.estaciones[i].nombre+'<br />FUENTE: '+data.estaciones[i].fuente+'<br />CODIGO: '+data.estaciones[i].estacion+'<br />MEDICIONES: <a href=http://127.0.0.1:8000/mediciones/'+data.estaciones[i].id+'>listado mediciones</a> <br />GRAFICOS: <a href=http://127.0.0.1:8000/graficos/'+data.estaciones[i].id+'>Graficar mediciones</a></p>');
    };
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
    
       
},

error: () => {
alert('Error vuelva a intentarlo mas tarde.');
}

});







