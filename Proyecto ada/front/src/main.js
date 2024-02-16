import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Toast from "vue-toastification";

import './assets/index.css'
import 'leaflet/dist/leaflet.css';
import "vue-toastification/dist/index.css";

  router.beforeEach((to, from, next) => {
    document.title = to.meta.title || 'SIMPARH';
    next();
  });

const app = createApp(App)

app.use(router)

app.use(Toast, {
  transition: "Vue-Toastification__slideBlurred",
  maxToasts: 20,
  newestOnTop: false,
  position: "bottom-right",
  timeout: 5000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.75,
  showCloseButtonOnHover: false,
  hideProgressBar: true,
  closeButton: "button",
  icon: true,
  rtl: false,  
});

app.mount('#app')


