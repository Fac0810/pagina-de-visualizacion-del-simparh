<template>
  <div class="cuerpo">
    <div class="container">
      <h1 class="brand"><span></span> </h1>
      <div class="wrapper animated bounceInLeft">
        <div class="company-info">
          <h3>{{ companyInfo.name }}</h3>
          <ul>
            <li>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="25" fill="#92bde7">
                <path
                  d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z" />
              </svg>
              {{ companyInfo.address }}
            </li>
            <li>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="20" fill="#92bde7">
                <path
                  d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64C0 311.4 200.6 512 448 512c18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 18.4-30 11.6-46.3l-40-96z" />
              </svg>
              {{ companyInfo.phone }}
            </li>
            <li>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="20" fill="#92bde7">
                <path
                  d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48H48zM0 176V384c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V176L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z" />
              </svg>
              {{ companyInfo.email }}
            </li>
          </ul>
        </div>
        <div class="contact">
          <h3>Contactenos: </h3>
          <form @submit.prevent="submitForm" class="contact-form">
            <p class="primerP">
              <label>Asunto</label>
              <select v-model="formData.asunto" name="asunto">
                <option value="" disabled>Seleccionar</option> 
                <option value="opcion1">Pedido de información</option>
                <option value="opcion2">Reclamo</option>
                <option value="opcion3">Opción 3</option>
              </select>
            </p>
            <p>
              <label>Nombre</label>
              <input v-model="formData.nombre" type="text" name="nombre">
            </p>
            <p>
              <label>Apellido</label>
              <input v-model="formData.apellido" type="text" name="apellido">
            </p>
            <p>
              <label>Email</label>
              <input v-model="formData.email" type="email" name="email">
            </p>
            <p>
              <label>Telefono</label>
              <input v-model="formData.telefono" type="text" name="telefono">
            </p>
            <p class="full">
              <label>Mensaje</label>
              <textarea v-model="formData.mensaje" name="mensaje" rows="5"></textarea>
            </p>
            <p class="full">
              <button type="submit">Enviar</button>
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      companyInfo: {
        name: 'SIMPARH',
        address: 'Calle 5 N°366 C1900 ',
        phone: ' (0800) 444-0579',
        email: 'test@ada.test'
      },
      formData: {
        asunto: '',
        nombre: '',
        apellido: '',
        email: '',
        telefono: '',
        mensaje: ''
      }
    };
  },
  methods: {
    submitForm() {
      // Handle form submission logic here
      console.log('Form submitted:', this.formData);
    }
  }
};
</script>

<style>
.animated {
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@keyframes bounceInLeft {

  from,
  60%,
  75%,
  90%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: translate3d(-3000px, 0, 0);
    transform: translate3d(-3000px, 0, 0);
  }

  60% {
    opacity: 1;
    -webkit-transform: translate3d(25px, 0, 0);
    transform: translate3d(25px, 0, 0);
  }

  75% {
    -webkit-transform: translate3d(-10px, 0, 0);
    transform: translate3d(-10px, 0, 0);
  }

  90% {
    -webkit-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }

  to {
    -webkit-transform: none;
    transform: none;
  }
}

.bounceInLeft {
  -webkit-animation-name: bounceInLeft;
  animation-name: bounceInLeft;
}

* {
  box-sizing: border-box;
}

.cuerpo {
  background: #92bde7;
  color: #485e74;
  line-height: 1.6;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  padding: 1em;
}

.container {
  max-width: 1170px;
  margin-left: auto;
  margin-right: auto;
  /* padding: 1em; */
}

ul {
  list-style: none;
  padding: 0;
}

.brand {
  text-align: center;
}

.brand span {
  color: #fff;
}

.wrapper {
  box-shadow: 0 0 20px 0 rgba(72, 94, 116, 0.7);
}

.wrapper>* {
  padding: 1em;
}

.company-info li {
  margin-bottom: 10px;
  font-size: 1.1em;
}

.company-info svg {
  vertical-align: middle;
  display: inline-block;
  margin-right: 10px;
}



.company-info {
  background: #c9e6ff;
}

.company-info h3 {
  display: block;
  font-size: 1.17em;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
}

.company-info ul {
  margin: 0;
  padding: 0;
  list-style: none;

}

.contact {
  background: #f9feff;
}

.contact h3 {
  display: block;
  font-size: 1.17em;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
}

/* FORM STYLES */
.contact-form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 20px;
}

.contact-form .primerP {
  grid-column: span 2;
}

select{
  width: 100%;
}

.contact-form label {
  display: block;
}

.contact-form p {
  margin: 0;
}

.contact-form .full {
  grid-column: 1 / 3;
}

.contact-form button,
.contact-form input,
.contact-form textarea {
  width: 100%;
  /* padding: 1em; */
  border: 1px solid #c9e6ff;
}

.contact-form textarea {
  resize: none;
  height: 80px;
}

.contact-form button {
  background: #c9e6ff;
  border: 0;
  text-transform: uppercase;
}

.contact-form button:hover,
.contact-form button:focus {
  background: #92bde7;
  color: #fff;
  outline: 0;
  transition: background-color 1s ease-out;
}

/* LARGE SCREENS */
@media (min-width: 700px) {
  .wrapper {
    display: grid;
    grid-template-columns: 1fr 2fr;
  }

  .wrapper>* {
    padding: 2em;
  }

  .company-info h3,
  .company-info ul,
  .brand {
    text-align: left;
  }
}
</style>
