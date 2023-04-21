<script setup>
import { RouterLink} from 'vue-router'

</script>

<template>
    <header>
        <div class="wrapper">
            <nav>
                <RouterLink to="/">Home</RouterLink>
                <RouterLink to="/mapa">Mapas</RouterLink>
                <RouterLink to="/contacto">Contactos</RouterLink>
                <RouterLink to="/graficos">Graficos</RouterLink>
            </nav>
        </div>
    </header>
</template>