<template>
<div style="height: 800px; width: 100%">
  <l-map :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"/>
    <l-marker :lat-lng="withPopup">
      <l-popup>
        <div>
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
  }
},
created(){
  this.getEstaciones()
}
};
</script>