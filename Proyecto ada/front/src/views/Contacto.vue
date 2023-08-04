<script setup>
import FormularioContacto from '../components/FormularioContacto.vue'
</script>

<template>
  <main>
    <div>
      <p class="font-extrabold text-5xl text-cyan-500">¿Querés más informacion? Contactanos</p>
      <p class="text-3xl pb-5">LLená este formulario</p>
    </div>
    <div class="grid grid-cols-3 mx-auto gap-2">
      <FormularioContacto class="w-fit p-2"/>
      <div class="w-fill h-fill col-span-2 p-2">
        <img src="../../public/contactanos.jpg" alt="contactanos">
      </div>
    </div>
  </main>
</template>
