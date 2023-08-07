<template>
    <form class="border-4 border-cyan-300" v-on:submit.prevent="onSubmit"> 
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Asunto:</p>
            <select v-model="form.asunto" class="ml-2 px-4 py-2 border rounded border-gray-300">
                <option v-for="opcion in opciones" :value="opcion.id">
                    {{ opcion.tipo }}
                </option>
            </select>
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Localidad:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.localidad" placeholder="localidad">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Partido:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.partido" placeholder="Partido">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Nombres:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.nombres" placeholder="Nombres">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Email:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.email" placeholder="Email">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Teléfono:</p>
            <input class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.telefono" placeholder="Teléfono">
        </div>
        <div class="text-gray-40 focus:border-teal-400  ">
            <p>Mensaje:</p>
            <textarea class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.mensaje" placeholder="¿Por qué desea comunicarse?"></textarea>
        </div>
        <div class="text-gray-40">
            <button type="submit" class="ml-2 px-4 py-2 border rounded bg-green-500 hover:border-black">Enviar</button>
        </div>
    </form>
</template>

<script>
import axios from 'axios';

export default {

data(){
  return {
      form:{
        localidad:'',
        partido:'',
        nombres:'',
        email:'',
        telefono:'',
        mensaje:'',
        asunto: 1,
      },
      opciones: [{id:1, tipo:"Asunto"}]
    }
},
methods:{
  onSubmit(){
    const path = 'http://127.0.0.1:8000/api/v1.0/contactos/'
    axios.post(path,this.form).then((response) => {
      this.success = 'Data saved successfully';
      console.log("Data Guardada")
      this.response = JSON.stringify(response, null, 2)
      }).catch(error => {
        this.response = 'Error: ' + error.response.status
    });
    console.log("Formulario");
  }
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
