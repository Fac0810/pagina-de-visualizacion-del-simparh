import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/index.css'
import 'leaflet/dist/leaflet.css';

  router.beforeEach((to, from, next) => {
    document.title = to.meta.title || 'SIMPARH';
    next();
  });

const app = createApp(App)

app.use(router)

app.mount('#app')
