<template>
  <div class="cuerpo">
    <div class="container">
      <h1 class="brand"><span></span></h1>
      <div class="wrapper animated bounceInLeft">
        <div class="company-info">
          <h3>{{ companyInfo.name }}</h3>
          <ul>
            <li>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="25" fill="#92bde7">
                <path
                  d="M352 320c88.4 0 160-71.6 160-160c0-15.3-2.2-30.1-6.2-44.2c-3.1-10.8-16.4-13.2-24.3-5.3l-76.8 76.8c-3 3-7.1 4.7-11.3 4.7H336c-8.8 0-16-7.2-16-16V118.6c0-4.2 1.7-8.3 4.7-11.3l76.8-76.8c7.9-7.9 5.4-21.2-5.3-24.3C382.1 2.2 367.3 0 352 0C263.6 0 192 71.6 192 160c0 19.1 3.4 37.5 9.5 54.5L19.9 396.1C7.2 408.8 0 426.1 0 444.1C0 481.6 30.4 512 67.9 512c18 0 35.3-7.2 48-19.9L297.5 310.5c17 6.2 35.4 9.5 54.5 9.5zM80 408a24 24 0 1 1 0 48 24 24 0 1 1 0-48z" />
              </svg>
              {{ companyInfo.datos }}
            </li>
          </ul>
        </div>
        <div style="background-color: #F9FEFF;">
          <div class="calendario">
            <div>
              <label for="select-year">Seleccione un año:</label>
              <select class="selectYear" id="select-year" v-model="selectedYear">
                <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
              </select>
            </div>
          </div>
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
        name: 'Panel de control de usuario',
        datos: 'Mantenimiento',
      },
      years: [],
      selectedYear: null,
    }
  },
  mounted() {
    const currentYear = new Date().getFullYear();
    for (let i = currentYear; i >= currentYear - 2; i--) {
      this.years.push(i);
    }
    this.selectedYear = currentYear;
  }
}
</script>

<style>
.selectYear {
  width: 20%;
  padding: 1em;
  border: 0px solid #c9e6ff;
}
.table {
  padding: 20px;
}

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
  height: calc(100vh - 88px);
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

select {
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

