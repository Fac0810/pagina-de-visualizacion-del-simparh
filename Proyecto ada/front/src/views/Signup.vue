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
            <input v-model="email" type="email" id="emailField" title="Ingrese un mail válido" />
            <label for="emailField">Email<span style="color:red"> *</span></label>
          </div>
        </div>
        <div class="input-container">
          <div id="inputbox-current-password" class="inputbox">
            <input v-model="password" type="password" autocomplete="current-password" id="passwordField"
              title="Campo de 8-15 caracteres." />
            <label for="passwordField">Contraseña<span style="color:red"> *</span></label>
          </div>
          <div id="inputbox-repeatPasswordField" class="inputbox">
            <input v-model="repeatPassword" type="password" id="repeatPasswordField"
              title="Repita la contraseña por favor." />
            <label for="repeatPasswordField">Repetir Contraseña<span style="color:red"> *</span></label>
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
      repeatPassword: ''
    };
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
      if (!this.validateUsername()) return;
      if (!this.validateName()) return;
      if (!this.validateLastName()) return;
      if (!this.validateEmail()) return;
      if (!this.validatePassword()) return;
      if (!this.validatePasswordMatch()) return;
    },

    validateUsername() {
      if (!this.nombreUsuario.trim()) {
        this.showToastError('Por favor ingrese un nombre de usuario');
        document.getElementById('inputbox-nombreUsuarioField').style.borderColor = 'red';
        return false;
      }
      if (!/^[a-zA-Z0-9]*$/.test(this.nombreUsuario)) {
        this.showToastError('El nombre de usuario debe ser alfanumérico');
        document.getElementById('inputbox-nombreUsuarioField').style.borderColor = 'red';
        return false;
      }
      document.getElementById('inputbox-nombreUsuarioField').style.borderColor = 'green';
      return true;
    },
    validateName() {
      if (!this.nombre.trim()) {
        this.showToastError('Por favor ingrese un nombre');
        document.getElementById('inputbox-nombreField').style.borderColor = 'red';
        return false;
      }
      if (!/^[a-zA-Z]*$/.test(this.nombre)) {
        this.showToastError('El nombre debe ser alfabético');
        document.getElementById('inputbox-nombreField').style.borderColor = 'red';
        return false;
      }
      document.getElementById('inputbox-nombreField').style.borderColor = 'green';
      return true;
    },
    validateLastName() {
      if (!this.apellido.trim()) {
        this.showToastError('Por favor ingrese un apellido');
        document.getElementById('inputbox-apellidoField').style.borderColor = 'red';
        return false;
      }
      if (!/^[a-zA-Z]*$/.test(this.apellido)) {
        this.showToastError('El apellido debe ser alfabético');
        document.getElementById('inputbox-apellidoField').style.borderColor = 'red';
        return false;
      }
      document.getElementById('inputbox-apellidoField').style.borderColor = 'green';
      return true;
    },
    validateEmail() {
      if (!this.email.trim()) {
        this.showToastError('Por favor ingrese un email');
        document.getElementById('inputbox-emailField').style.borderColor = 'red';
        return false;
      }
      if (!/^\S+@\S+\.\S+$/.test(this.email)) {
        this.showToastError('Por favor ingrese un email válido');
        document.getElementById('inputbox-emailField').style.borderColor = 'red';
        return false;
      }
      document.getElementById('inputbox-emailField').style.borderColor = 'green';
      return true;
    },
    validatePassword() {
      if (!this.password.trim()) {
        this.showToastError('Por favor ingrese una contraseña');
        document.getElementById('inputbox-current-password').style.borderColor = 'red';
        return false;
      }
      if (this.password.length < 8 || this.password.length > 15) {
        this.showToastError('La contraseña debe tener entre 8 y 15 caracteres');
        document.getElementById('inputbox-current-password').style.borderColor = 'red';
        return false;
      }
      document.getElementById('inputbox-current-password').style.borderColor = 'green';
      return true;
    },
    validatePasswordMatch() {
      if (this.password !== this.repeatPassword) {
        this.showToastError('Las contraseñas no coinciden');
        document.getElementById('inputbox-repeatPasswordField').style.borderColor = 'red';
        return false;
      }
      document.getElementById('inputbox-repeatPasswordField').style.borderColor = 'green';
      return true;
    },
    submit(event) {
      event.preventDefault();
      console.log(window.DEVELOPMENT_URL = "{{ DEVELOPMENT_URL }}");

      if (this.validate()) {
        const data = {
          nombreUsuario: this.nombreUsuario,
          nombre: this.nombre,
          apellido: this.apellido,
          email: this.email,
          password: this.password
        };
        const isDevelopment = process.env.NODE_ENV === 'development';
        const baseUrl = isDevelopment ? 'http://127.0.0.1:8000/' : 'https://tu-url-de-produccion.com/';
        console.log('data', data);
        console.log('baseUrl', baseUrl);
      }

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


</style>


