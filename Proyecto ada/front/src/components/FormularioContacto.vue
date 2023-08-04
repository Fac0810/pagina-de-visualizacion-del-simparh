<template>
    <form class="border-4 border-cyan-300" @submit.prevent="onSubmit"> 
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Asunto:</p>
            <select v-model="seleccionado" class="ml-2 px-4 py-2 border rounded border-gray-300">
                <option v-for="opcion in opciones" :value="opcion.id">
                    {{ opcion.tipo }}
                </option>
            </select>
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Apellidos:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="apellidos" placeholder="Apellidos">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Nombres:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="nombres" placeholder="Nombres">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Email:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="email" placeholder="Email">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Teléfono:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="telefono" placeholder="Teléfono">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Descripción:</p>
            <textarea class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="desc" placeholder="Descripción"></textarea>
        </div>
        <div class="text-gray-40">
            <button type="submit" class="ml-2 px-4 py-2 border rounded bg-green-500 hover:border-black">Enviar</button>
        </div>
    </form>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue'

export default {

data(){
  return {
        seleccionado: ref(1),
        opciones: ref([{id:1, tipo:"Asunto"}])
    }
},

setup() {
const onSubmit = () => {
      enviarForm();
    };
const enviarForm= () => {
    
    const path = 'http://127.0.0.1:8000/api/v1.0/estaciones/'
    axios.get(path).then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
    });
    console.log("Formulario Enviado");
  };

return{ onSubmit, enviarForm }
},

mounted(){
  //agrego los asuntos en el select
  const path = 'http://127.0.0.1:8000/api/v1.0/asuntos/'
    axios.get(path).then((response) => {
      this.opciones = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    console.log("ok Asuntos")
}
}
</script>
