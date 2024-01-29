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
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      meta: { excludeNavBarFooter: true },
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/mapa',
      name: 'mapa',
      component: MapaEmas
    },
    {
      path: '/graficos',
      name: 'graficos',
      component: GraficosEmas
    },
    {
      path: '/contacto',
      name: 'contacto',
      component: Contacto
    }
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () => import('../views/AboutView.vue')
  ]
})

export default router
