<template>
  <div class="center-container">
    <div class="logo">
      <img src="../../public/logoSIMPARH.png" alt="Logo SIMPARH">
    </div>
    <section>
      <form @submit.prevent="login">
        <h1>Registro</h1>
        <div class="input-container">
          <div class="inputbox">
            <input v-model="nombreUsuario" type="text" required id="nombreUsuarioField" />
            <label for="nombreUsuarioField">Nombre Usuario</label>
          </div>
          <div class="inputbox">
            <input v-model="nombre" type="text" required id="nombreField" />
            <label for="nombreField">Nombre</label>
          </div>
        </div>
        <div class="input-container">
          <div class="inputbox">
            <input v-model="apellido" type="text" required id="apellidoField" />
            <label for="apellidoField">Apellido</label>
          </div>
          <div class="inputbox">
            <input v-model="email" type="email" required id="emailField" />
            <label for="emailField">Email</label>
          </div>
        </div>
        <div class="input-container">
          <div class="inputbox">
            <input v-model="password" type="password" required autocomplete="current-password" id="passwordField" />
            <label for="passwordField">Contraseña</label>
          </div>
          <div class="inputbox">
            <input v-model="password" type="password" required autocomplete="current-password" id="passwordField" />
            <label for="passwordField">Repetir Contraseña</label>
          </div>
        </div>
        <div class="button-container">
          <button onclick="window.location.href='/'">Crear</button>
          <button onclick="window.location.href='/login'">Volver</button>
        </div>
      </form>
    </section>

  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {

    },
  },
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


img {

}

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

button {
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
</style>


