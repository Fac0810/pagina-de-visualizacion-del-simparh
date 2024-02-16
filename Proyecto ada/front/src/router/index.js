import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MapaEmas from '../views/MapaEmas.vue'
import Contacto from '../views/Contacto.vue'
import GraficosEmas from '../views/GraficosEmas.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      meta: { title: 'SIMPARH' },
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      meta: { excludeNavBarFooter: true, title: 'SIMPARH' },
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/signup',
      name: 'signup',
      meta: { excludeNavBarFooter: true, title: 'SIMPARH' },
      component: () => import('../views/Signup.vue'),
      props: { BACKEND_URL: import.meta.env.VITE_BACKEND_URL }
    },
    {
      path: '/mapa',
      name: 'mapa',
      meta: { title: 'Mapa' },
      component: MapaEmas
    },
    {
      path: '/graficos',
      name: 'graficos',
      meta: { title: 'Graficos' },
      component: GraficosEmas
    },
    {
      path: '/contacto',
      name: 'contacto',
      meta: { title: 'Contacto' },
      component: Contacto
    }
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () => import('../views/AboutView.vue')
  ]
})

export default router
