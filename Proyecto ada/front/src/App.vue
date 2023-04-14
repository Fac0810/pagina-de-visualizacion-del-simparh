<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'

</script>

<template>
  <NavBar /> <!-- incluye al RouterLink para links del menu-->

  <RouterView />

  <Footer />
</template>

<style scoped>

</style>
