<template >
  <form class="border-4 border-cyan-300 pb-10" v-on:submit.prevent="onSubmit"> 
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Asunto:</label>
          <p></p>
          <select v-model="form.asunto" class="ml-2 px-4 py-2 border rounded border-gray-300" required>
              <option v-for="opcion in opciones" :value="opcion.id">
                  {{ opcion.tipo }}
              </option>
          </select>
      </div>
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Localidad:</label>
          <p></p>
          <input type="text" class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.localidad" placeholder="Localidad" required>
      </div>
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Partido:</label>
          <p></p>
          <input type="text" class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.partido" placeholder="Partido" required>
      </div>
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Nombres:</label>
          <p></p>
          <input type="text" class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.nombres" placeholder="Apellidos Nombres" required>
      </div>
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Email:</label>
          <p></p>
          <input type="email" class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.email" placeholder="Ejemplo@ejemplo.eje" required pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$">
          <!--{{ esEmailValido }} -->
      </div>
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Teléfono: (sin espacios)</label>
          <p></p>
          <input type="tel" class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.telefono" placeholder="2211234567" required  pattern="[0-9]{10}">
      </div>
      <div class="text-gray-40 focus:border-teal-400  ">
          <label>Mensaje:</label>
          <p></p>
          <textarea class="ml-2 px-4 py-2 border rounded border-gray-300" v-model="form.mensaje" placeholder="¿Por qué desea comunicarse?" required></textarea>
      </div>
      <div class="text-gray-40">
          <button type="submit" class="ml-2 px-4 py-2 border rounded bg-green-500 hover:border-black">Enviar</button>
      </div>
  </form>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';


export default {

data(){
  return {
      form:{
        localidad:ref(''),
        partido:ref(''),
        nombres:ref(''),
        email:ref(''),
        telefono:ref(''),
        mensaje:ref(''),
        asunto: ref(""),
      },
      opciones: [{id:"", tipo:"Seleccione un asunto"}],
    }
},
/*computed: {
  esEmailValido() {
      return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.form.email)
    },
  },
*/
methods:{
  onSubmit(){
    const path = 'http://127.0.0.1:8000/api/v1.0/contactos/'
    axios.post(path,this.form).then((response) => {
      this.success = 'Data saved successfully';
      console.log("Data Guardada");
      this.response = JSON.stringify(response, null, 2);
      this.$router.push('exito');
      }).catch(error => {
        this.response = 'Error: ' + error.response.status;
        console.log(error.response.data);
    });
    console.log("Formulario");
  }
},

mounted(){
  //agrego los asuntos en el select
  const path = 'http://127.0.0.1:8000/api/v1.0/asuntos/'
    axios.get(path).then((response) => {
      this.opciones = this.opciones.concat(response.data)
    })
    .catch((error) => {
      console.log(error)
    })
    console.log("ok Asuntos")
}
}
</script>
