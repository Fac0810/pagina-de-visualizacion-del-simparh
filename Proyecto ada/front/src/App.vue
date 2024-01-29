<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'

import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

onMounted(() => {
  initFlowbite();
})
</script>

<template>
  <div class="h-screen">
    <NavBar v-if="!$route.meta.excludeNavBarFooter" class="z-10"/>
    <!-- <RouterView class="mx-[5vw]"/> -->
    <RouterView />
    <Footer v-if="!$route.meta.excludeNavBarFooter" />
  </div>
</template>


<!-- agregar cuando haya Auth

<template>
  <navbar v-if="isAuthenticated"/>
  <router-view/>
</template>

export default {
name: 'App',
computed: { 
  isAuthenticated() {
    return this.$store.getters.isAuthenticated
  },
}, -->


