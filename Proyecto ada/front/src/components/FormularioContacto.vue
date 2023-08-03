<template>
    <form class="border-4 border-cyan-300"> 
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Asunto:</p>
            <input class="ml-2 px-4 py-2 border rounded" v-model="asunto" placeholder="Un asunto">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Apellidos:</p>
            <input class="ml-2 px-4 py-2 border rounded" v-model="apellidos" placeholder="Apellidos">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Nombres:</p>
            <input class="ml-2 px-4 py-2 border rounded" v-model="nombres" placeholder="Nombres">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Email:</p>
            <input class="ml-2 px-4 py-2 border rounded" v-model="email" placeholder="Email">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Teléfono:</p>
            <input class="ml-2 px-4 py-2 border rounded" v-model="telefono" placeholder="Teléfono">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Descripción:</p>
            <textarea class="ml-2 px-4 py-2 border rounded" v-model="desc" placeholder="Descripción"></textarea>
        </div>
    </form>
</template>

<script>

</script>
