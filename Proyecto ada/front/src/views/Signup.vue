<template>
  <div class="center-container">
    <div class="logo">
      <img src="../../public/logoSIMPARH.png" alt="Logo SIMPARH">
    </div>
    <section>
      <form @submit.prevent="submit">
        <h1>Registro</h1>
        <div class="input-container">
          <div id="inputbox-nombreUsuarioField" class="inputbox">
            <input v-model="nombreUsuario" type="text" id="nombreUsuarioField" title="Campo alfanumerico." />
            <label for="nombreUsuarioField">Nombre Usuario<span style="color:red"> *</span></label>
          </div>
          <div id="inputbox-nombreField" class="inputbox">
            <input v-model="nombre" type="text" id="nombreField" title="Campo alfabético" />
            <label for="nombreField">Nombre<span style="color:red"> *</span></label>
          </div>
        </div>
        <div class="input-container">
          <div id="inputbox-apellidoField" class="inputbox">
            <input v-model="apellido" type="text" id="apellidoField" title="Campo alfébetico" />
            <label for="apellidoField">Apellido<span style="color:red"> *</span></label>
          </div>
          <div id="inputbox-emailField" class="inputbox">
            <input v-model="email" type="email" id="emailField" title="Ingrese un mail válido" autocomplete="email" />
            <label for="emailField">Email<span style="color:red"> *</span></label>
          </div>
        </div>
        <div class="input-container">
          <div id="inputbox-passwordField" class="inputbox">
            <input v-model="password" type="password" autocomplete="current-password" id="passwordField"
              title="Campo de 8-15 caracteres." />
            <label for="passwordField">Contraseña<span style="color:red"> *</span></label>
            <span class="toggle-password" @click="togglePasswordVisibility('passwordField', 'eyePassword')">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="20" height="20" id="eyePassword"
                style="fill:grey">
                <path
                  d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z" />
              </svg>
            </span>
          </div>
          <div id="inputbox-repeatPasswordField" class="inputbox">
            <input v-model="repeatPassword" type="password" id="repeatPasswordField"
              title="Repita la contraseña por favor." autocomplete="new-password" />
            <label for="repeatPasswordField">Repetir Contraseña<span style="color:red"> *</span></label>
            <span class="toggle-password" @click="togglePasswordVisibility('repeatPasswordField', 'eyePasswordRepeat')">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="20" height="20" id="eyePasswordRepeat"
                style="fill:grey">
                <path
                  d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z" />
              </svg>
            </span>
          </div>
        </div>
        <div class="button-container">
          <button type="submit">Crear</button>
          <button type="button" @click="goToLogin">Volver</button>
        </div>
      </form>
    </section>

  </div>
</template>

<script>
import { useToast } from 'vue-toastification';
import axios from 'axios';



export default {
  data() {
    return {
      nombreUsuario: '',
      nombre: '',
      apellido: '',
      email: '',
      password: '',
      repeatPassword: '',
      csrfToken: null,
    };
  },
  async created() {
    try {
      const csrfResponse = await axios.post(this.BACKEND_URL + '/getcsrf');
      this.csrfToken = csrfResponse.data.csrfToken;
    } catch (error) {
      console.error('Error al obtener el token CSRF', error);
    }
  },
  props: {
    BACKEND_URL: {
      type: String,
      required: true
    },
  },
  setup() {
    const toast = useToast();

    const showToastError = (message) => {
      toast.error(message);
    };

    const showToastSuccess = (message) => {
      toast.success(message);
    };

    return {
      showToastError,
      showToastSuccess
    };
  },
  methods: {
    goToLogin() {
      this.$router.push('/login');
    },
    validate() {
      const validationRules = [
        { field: 'nombreUsuario', nom: 'Nombre de Usuario', regex: /^[a-zA-Z0-9]*$/, errorMessage: 'Por favor ingrese un nombre de usuario alfanumérico' },
        { field: 'nombre', nom: 'Nombre', regex: /^[a-zA-Z]*$/, errorMessage: 'Por favor ingrese un nombre alfabético' },
        { field: 'apellido', nom: 'Apellido', regex: /^[a-zA-Z]*$/, errorMessage: 'Por favor ingrese un apellido alfabético' },
        { field: 'email', nom: 'E-mail', regex: /^\S+@\S+\.\S+$/, errorMessage: 'Por favor ingrese un email válido' },
        { field: 'password', nom: 'Contraseña', regex: /^.{8,15}$/, errorMessage: 'La contraseña debe tener entre 8 y 15 caracteres' },
        { field: 'repeatPassword', nom: 'Repetir Contraseña', regex: /^.{8,15}$/, matchField: 'password', errorMessage: 'La contraseña debe tener entre 8 y 15 caracteres' }
      ];

      let isValid = true;

      for (const rule of validationRules) {
        const value = this[rule.field].trim();
        const inputbox = document.getElementById(`inputbox-${rule.field}Field`);

        if (!value) {
          this.showToastError(`Por favor ingrese ${rule.nom}`);
          inputbox.style.borderColor = 'red';
          isValid = false;
        } else if (rule.regex && !rule.regex.test(value)) {
          this.showToastError(rule.errorMessage);
          inputbox.style.borderColor = 'red';
          isValid = false;
        } else if (rule.matchField && value !== this[rule.matchField]) {
          this.showToastError('Las contraseñas no coinciden');
          inputbox.style.borderColor = 'red';
          isValid = false;
        } else {
          inputbox.style.borderColor = 'green';

        }
      }
      return isValid;
    },
    async submit(event) {
      event.preventDefault();
      console.log('BACKEND_URL:', this.BACKEND_URL);
      console.log('csrfToken:', this.csrfToken);

      if (this.validate()) {

        const data = {
          nombreUsuario: this.nombreUsuario,
          nombre: this.nombre,
          apellido: this.apellido,
          email: this.email,
          password: this.password
        };
        try {
          console.log('data', data);

          const crearUsuarioResponse = await axios.get(this.BACKEND_URL + '/crearUsuario', {
            params: data,
            headers: {
              'CSRF-Token': this.csrfToken
            }
          });
          console.log('crearUsuarioResponse', crearUsuarioResponse);


        } catch (error) {
          console.error('Error al registrar usuario', error);
          this.showToastError('Error al registrar usuario');
        }
      }

    },
    togglePasswordVisibility(idPassword, idEye) {
      const passwordField = document.getElementById(idPassword);
      const eye = document.getElementById(idEye);
      passwordField.type = passwordField.type === 'password' ? 'text' : 'password';
      eye.style.fill = eye.style.fill === 'grey' ? 'white' : 'grey';
    },
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'poppins', sans-serif;
}

h1 {
  font-size: 2rem;
  color: #fff;
  text-align: center;
}

.logo {
  position: absolute;
  top: 0;
  left: auto;
  width: 300px;
}


img {}

.center-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-image: url('../../public/rio-reconquista.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  overflow: hidden;

}

section {
  margin-top: 55px;
  position: relative;
  /* width: 50%; */
  background-color: transparent;
  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  backdrop-filter: blur(55px);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem 3rem;
}

.input-container {
  display: flex;
  flex-direction: row;
  margin: 30px;
  flex-grow: 1;
  /* Para que ocupen el mismo espacio */
}


.inputbox input:focus {
  outline: none;
}

.inputbox input:focus-visible {
  outline: none;
  box-shadow: 0 0 0 0px rgba(0, 0, 0, 0.1);
}

.inputbox {
  position: relative;
  border-bottom: 2px solid #fff;
  outline: none;
  margin: 0px 5px;
}

.inputbox label {
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-50%);
  color: #fff;
  font-size: 1rem;
  pointer-events: none;
  transition: all 0.5s ease-in-out;
}

input:focus~label,
input:valid~label {
  top: -5px;
}

.inputbox input {
  width: 100%;
  height: 60px;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1rem;
  padding: 0 35px 0 5px;
  color: #fff;
}

.forget {
  margin: 10px 0;
  font-size: 0.85rem;
  color: #fff;
  display: flex;
  justify-content: space-between;

}

.forget label {
  display: flex;
  align-items: center;
}

.forget label input {
  margin-right: 3px;
}

.forget a {
  margin-left: 10px;
  color: #fff;
  text-decoration: none;
  font-weight: 600;
}

.forget a:hover {
  text-decoration: underline;
}

button[type='submit'],
button[type='button'] {
  width: 50%;
  height: 40px;
  border-radius: 40px;
  background-color: rgb(255, 255, 255, 1);
  border: none;
  outline: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.4s ease;
  margin: 5px;
}


button:hover {
  background-color: rgb(255, 255, 255, 0.5);
}

.register {
  font-size: 0.9rem;
  color: #fff;
  text-align: center;
  margin: 10px 0 10px;
}

.register p a {
  text-decoration: none;
  color: #fff;
  font-weight: 600;
}

.register p a:hover {
  text-decoration: underline;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.has-error input {
  border-color: red;
}

.has-success input {
  border-color: green;
}

.toggle-password {
  cursor: pointer;
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
}
</style>


