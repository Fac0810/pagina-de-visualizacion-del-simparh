<script setup>
import FormularioContacto from '../components/FormularioContacto.vue'

const foto={
    'src': '../../public/contactanos.jpg',
    'alt': 'Foto 1',
  }
</script>

<template>
  <main>
    <div class="my-3">
      <p class="font-extrabold text-5xl text-cyan-500">¿Querés más informacion? Contactanos</p>
      <p class="text-3xl">LLená este formulario</p>
    </div>
    <div class="grid grid-cols-3 mx-auto gap-2">
      <FormularioContacto class="w-fit p-2"/>
      <img src="../../public/contactanos.jpg" alt="contactanos" class="w-3/4 h-3/4 col-span-2 p-2">
    </div>
  </main>
</template>
