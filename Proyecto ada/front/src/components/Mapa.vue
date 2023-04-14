<template>
<div style="height: 800px; width: 100%">
  <l-map :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"/>
    <l-marker :lat-lng="withPopup">
      <l-popup>
        <div @click="innerClick">
          I am a popup
        </div>
      </l-popup>
    </l-marker>
  </l-map>
</div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup} from "@vue-leaflet/vue-leaflet";

export default {
name: "MapaEmas",
components: {
  LMap,
  LTileLayer,
  LMarker,
  LPopup,
},
data() {
  return {
    zoom: 6,
    center: latLng(-38.157222 , -60.569722),
    url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attribution:
      '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>',
    withPopup: latLng(47.41322, -1.219482),
    currentCenter: latLng(47.41322, -1.219482),
  };
},
methods: {
  innerClick() {
    alert("Click!");
  }
},
created(){
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
  },

error: () => {
alert('Error vuelva a intentarlo mas tarde.');
}

});
}
};
</script>