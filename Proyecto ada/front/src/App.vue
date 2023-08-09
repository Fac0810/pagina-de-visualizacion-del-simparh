<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'

import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

onMounted(() =>{
  initFlowbite();
})

</script>

<template>
  <div class="h-screen">
    <NavBar class="z-10"/> <!-- incluye al RouterLink para links del menu-->

    <RouterView class="mx-[5vw] bg-white"/>

    <Footer/>
  </div>

</template>
