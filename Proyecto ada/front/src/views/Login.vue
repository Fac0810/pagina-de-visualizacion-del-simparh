<template>
  <div class="center-container">
  <body>
    <div class="logo">
    <img src="../../public/logoSIMPARH.png" alt="Logo SIMPARH">
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
          <span class="toggle-password" @click="togglePasswordVisibility('passwordField','eye')">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="20" height="20" id="eye" style="fill:grey" >
                <path d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"/></svg>
            </span>
        </div>
        <div class="forget">
          <label for=""><input type="checkbox">Recordarme</label>
          <a href="/">Olvide la contraseña</a>
        </div>
        <button onclick="window.location.href='/'" >Iniciar Sesión</button>
        <div class="register">
          <p>¿No tenes cuenta? <a href="/signup">Click acá</a></p>
        </div>
        <button onclick="window.location.href='/'" >Ingresar como invitado</button>
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
    ingresoInvitado() {
      this.$router.push('/');
    },
    togglePasswordVisibility(idPassword,idEye) {
      const passwordField = document.getElementById(idPassword);
      const eye = document.getElementById(idEye);
      passwordField.type = passwordField.type === 'password' ? 'text' : 'password';
      eye.style.fill = eye.style.fill === 'grey' ? 'white' : 'grey';
    }
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

.logo {
  position: absolute;
  top: 0;
  left: auto;
  width: 300px;
}
body {
    margin: 0; 
    overflow: hidden; 
  }

  img {
    margin-left: 28px;

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

.toggle-password {
  cursor: pointer;
  position: absolute;
  right: 0px;
  top: 50%;
  transform: translateY(-50%);
  padding: 20px;
}


</style>


