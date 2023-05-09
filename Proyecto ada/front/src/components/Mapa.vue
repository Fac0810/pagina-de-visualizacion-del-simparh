<template>
<div style="height: 600px; width: 100%" class="border-4 border-cyan-500">
  <l-map :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"/>
    <l-marker v-for="punto in estaciones" :lat-lng= "[punto.latitud, punto.longitud]">
      <l-popup>
        <div>
          <p>NOMBRE: {{ punto.nombre }} <br />FUENTE: {{ punto.fuente }}<br />CÓDIGO: {{ punto.estacion }}<br />MEDICIONES: <a :href="'http://127.0.0.1:8000/mediciones/' + punto.id " >listado mediciones</a> <br />GRÁFICOS: <a :href="'http://localhost:5173/graficos' /*+ punto.id */">Graficar mediciones</a> <p v-if="punto.mediciones.primera"> Primera medición: {{ punto.mediciones.primera }} <br/> Última medición: {{ punto.mediciones.ultima }}</p></p>
        </div>
      </l-popup>
    </l-marker>
  </l-map>
</div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup} from "@vue-leaflet/vue-leaflet";

import axios from 'axios';

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
    estaciones: [],
  };
},
methods: {
  getEstaciones() {
    
    const path = 'http://127.0.0.1:8000/api/v1.0/estaciones/'
    axios.get(path).then((response) => {
      this.estaciones = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    console.log("ok Estaciones")
  },
},
created(){
  this.getEstaciones();
}
};
</script>
