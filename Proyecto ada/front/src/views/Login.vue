<template>
  <div class="center-container">
  <body>
    <div class="container">
      <div class="brand">
        <img src="../../public/logoSIMPARH.png" alt="Logo SIMPARH">
      </div>
    </div>
    <section>
      <form @submit.prevent="login">
        <h1>Ingreso</h1>
        <div class="inputbox">
          <input v-model="email" type="email" required id="emailField" />
          <label for="emailField">Email</label>
        </div>
        <div class="inputbox">
          <input v-model="password" type="password" required autocomplete="current-password" id="passwordField" />
          <label for="passwordField">Contraseña</label>
        </div>
        <div class="forget">
          <label for=""><input type="checkbox">Recordarme</label>
          <a href="#">Olvide la contraseña</a>
        </div>
        <button>Iniciar Sesión</button>
        <div class="register">
          <p>¿No tenes cuenta? <a href="#">Click acá</a></p>
        </div>
        <button onclick="window.location.href='/'">Ingresar como invitado</button>
      </form>
    </section>
  </body>
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

.container {
  width: 10%;
  height: 10%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.brand {
  position: absolute;
  top: 0;
  left: 0;
  padding: 50px;
  display: flex;
  align-items: center;
}
.container .brand img {
  width: 25%;
  height: 25 %;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'poppins', sans-serif;
}

body {
    margin: 0; /* Elimina el margen predeterminado del body */
    overflow: hidden; /* Evita el desplazamiento vertical */
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
  }

section {
  margin-top: 55px;
  position: relative;
  max-width: 400px;
  background-color: transparent;
  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  backdrop-filter: blur(55px);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem 3rem;
}

h1 {
  font-size: 2rem;
  color: #fff;
  text-align: center;
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
  margin: 30px 0;
  max-width: 310px;
  border-bottom: 2px solid #fff;
  outline: none; 

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
  width: 100%;
  height: 40px;
  border-radius: 40px;
  background-color: rgb(255, 255, 255, 1);
  border: none;
  outline: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.4s ease;
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
</style>


