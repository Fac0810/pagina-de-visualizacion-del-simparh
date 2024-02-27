<script setup>
import { RouterLink } from 'vue-router'
// class="block py-2 pl-3 pr-4 text-white bg-cyan-700 rounded md:bg-transparent md:text-cyan-700 md:p-0 md:dark:text-cyan-500" aria-current="page"
// class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-cyan-700 md:p-0 md:dark:hover:text-cyan-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700" aria-current="page"
</script>

<template>
    <body>
        <div class="ingrateBody">
            <nav class="navStyle border-b border-gray-200 dark:border-gray-600">
                <div class="flex justify-between mx-auto px-2">
                    <div class="logo flex items-center">
                        <RouterLink to="/" class="flex items-center">
                            <img src="../../public/logo_ada.svg" class="h-14 mr-3" alt="Logo ADA">
                            <span
                                class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white color">SIMPARH</span>
                        </RouterLink>
                    </div>

                    <div class="flex items-center justify-center hidden w-full md:flex md:w-auto " id="navbar-sticky">
                        <ul
                            class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                            <li>
                                <RouterLink to="/"
                                    class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-cyan-700 md:p-0 md:dark:hover:text-cyan-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
                                    aria-current="page">Inicio</RouterLink>
                            </li>
                            <li>
                                <RouterLink to="/mapa"
                                    class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-cyan-700 md:p-0 md:dark:hover:text-cyan-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">
                                    Mapas</RouterLink>
                            </li>
                            <li>
                                <RouterLink to="/graficos"
                                    class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-cyan-700 md:p-0 md:dark:hover:text-cyan-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">
                                    Graficos</RouterLink>
                            </li>
                            <li>
                                <RouterLink to="/contacto"
                                    class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-cyan-700 md:p-0 md:dark:hover:text-cyan-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">
                                    Contacto</RouterLink>
                            </li>
                        </ul>
                    </div>
                    <div class="perfil flex items-center justify-end ">
                        <!-- <RouterLink to="/">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="25" fill="#92bde7">
                                <path
                                    d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z" />
                            </svg>
                        </RouterLink>
                        <div>
                            Nombre Apellido
                        </div> -->
                        <div class="container">
                            <button class="btn"><span>Usuario</span>
                                <!-- <i class="material-icons">glow</i> -->
                                <ul class="dropdown">
                                    <li :class="{ active: isActive('/perfil') }"><a href="/perfil">Perfil</a></li>
                                    <li :class="{active: isActive('/panel')}"><a href="/panel">Panel de control</a></li>
                                    <li :class="{active: isActive('/mensajeria')}"><a href="/mensajeria">Mensajes</a></li>
                                    <li><a href="/login">Desconectarse</a></li>
                                </ul>
                            </button>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </body>
</template>
<script>
export default {
  methods: {
    isActive(url) {
      const currentPageUrl = window.location.pathname;
      return currentPageUrl === url;
    }
  }
}
</script>
<style>
.color{
    color: #0DA8C7;
}

.navStyle {
    background-color: #ffffff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 999;
}
/* .perfil {
    padding: 15px;
    cursor: pointer;
    transition: transform 0.3s ease-in-out;
    border-left: 2px solid #92bde7;
    padding-right: 5px;
    margin: 6px;

} */
/* .perfil .svg {
    border-radius: 50%;
    border: 2px solid #92bde7;
    margin: 2px;
} */

/* .perfil:hover {
    transform: scale(1.1);
} */

/* body {
  background: #F5F5F5;
  height: 100%;
  color: #FFFFFF; 
  font-family: "Roboto", sans-serif; 
  font-size: 14px; 
  font-weight: 400; 
  line-height: 1.5em; 
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
} */

.container {
  position: relative;
  /* top: 50%; */
  /* left: 50%; */
  /* transform: translate(-50%, -50%); */
}

.btn {
  outline: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center; /* space-between; */
  background: #0DA8C7; /* Use the appropriate accent color */
  min-width: 220px;
  border: 0;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, .1);
  box-sizing: border-box;
  padding: 16px 20px;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: 600; /* Use the appropriate semibold weight */
  letter-spacing: 1.2px;
  text-transform: uppercase;
  overflow: hidden;
  cursor: pointer;
}

.btn:focus .dropdown,
.btn:active .dropdown {
  transform: translate(0, 20px);
  opacity: 1;
  visibility: visible;
}

/* .btn .material-icons {
  border-radius: 100%;
  animation: ripple 0.6s linear infinite;
} */

.btn .dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  background: #FFFFFF;
  width: 100%;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, .1);
  text-align: left;
  opacity: 0;
  visibility: hidden;
  transition: 0.3s ease;
}

.btn .dropdown:before {
  content: '';
  position: absolute;
  top: -6px;
  left: 20px;
  width: 0;
  height: 0;
  box-shadow: 2px -2px 6px rgba(0, 0, 0, .05);
  border-top: 6px solid #FFFFFF;
  border-right: 6px solid #FFFFFF;
  border-bottom: 6px solid transparent;
  border-left: 6px solid transparent;
  transform: rotate(-45deg);
  mix-blend-mode: multiple;
}

.btn .dropdown li {
  z-index: 1;
  position: relative;
  background: #FFFFFF;
  padding: 0 20px;
  color: #666666;
}

.btn .dropdown li.active {
  color: #5380F7; /* Use the appropriate accent color */
}

.btn .dropdown li:first-child {
  border-radius: 4px 4px 0 0;
}

.btn .dropdown li:last-child {
  border-radius: 0 0 4px 4px;
}

.btn .dropdown li:last-child a {
  border-bottom: 0;
}

.btn .dropdown a {
  display: block;
  border-bottom: 1px solid rgba(0, 0, 0, .05);
  padding: 16px 0;
  color: inherit;
  font-size: 10px;
  text-decoration: none;
}

@keyframes ripple {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, .1), 0 0 0 20px rgba(255, 255, 255, .1), 0 0 0 40px rgba(255, 255, 255, .1), 0 0 0 60px rgba(255, 255, 255, .1);
  }
  100% {
    box-shadow: 0 0 0 20px rgba(255, 255, 255, .1), 0 0 0 40px rgba(255, 255, 255, .1), 0 0 0 60px rgba(255, 255, 255, .1), 0 0 0 80px rgba(255, 255, 255, 0);
  }
}
</style>