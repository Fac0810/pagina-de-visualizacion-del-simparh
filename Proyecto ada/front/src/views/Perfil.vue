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
                                    d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z" />
                            </svg>
                            {{ companyInfo.datos }}
                        </li>
                    </ul>
                </div>
                <div style="background-color: #F9FEFF;">
                    <div class="datosBasicos">
                        <h3>Editar perfil: </h3>
                        <form>
                            <p>
                                <label>Nombre de Usuario:</label>
                                <input v-model="formPerfil.nombreUsuario" type="text" name="nombreUsuario" disabled>
                            </p>
                            <p>
                                <label>Nombre:</label>
                                <input v-model="formPerfil.nombre" type="text" name="nombre" disabled>
                            </p>
                            <p>
                                <label>Apellido:</label>
                                <input v-model="formPerfil.apellido" type="text" name="apellido" disabled>
                            </p>
                            <p>
                                <label>Mail:</label>
                                <input v-model="formPerfil.mail" type="text" name="mail" disabled>
                            </p>
                            <p class="full">
                                <button type="submit">Enviar</button>
                            </p>
                        </form>
                    </div>

                    <div class="contraEdit">
                        <h3>Editar contraseña: </h3>
                        <form>
                            <p>
                                <label>Contraseña actual:</label>
                                <input v-model="formPassword.password" type="text" name="password">
                            </p>
                            <p>
                                <label>Nueva contraseña:</label>
                                <input v-model="formPassword.newPassword" type="text" name="newPassword">
                            </p>
                            <p class="full">
                                <button type="submit">Enviar</button>
                            </p>
                        </form>
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
                name: 'PERFIL DE USUARIO',
                datos: 'Datos básicos',
            },
            formPerfil: {
                nombreUsuario: '',
                nombre: '',
                apellido: '',
                mail: '',
            },
            formPassword: {
                password: '',
                newPassword: '',
            }
        }
    }
}
</script>


<style>
.full{
    display: flex;
    justify-content: end;
}
.datosBasicos {
    margin-bottom: 20px;
}

.datosBasicos input[type="text"] {
    background-color: #F9FEFF;
    border-bottom: 1px solid #c9e6ff;
    margin: 2px;
}

.contraEdit input[type="text"] {
    background-color: #F9FEFF;
    border-bottom: 1px solid #c9e6ff;
    margin: 2px;
}

h3 {
    margin-bottom: 10px;
    font-weight: bold;
}

input {
    padding: 4px;
    border-radius: 5px;
    border: 0px;
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
    /* background: #f9feff; */
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
    background-color: #92BDE7;
    /* padding: 1em; */
    /* border: 1px solid #c9e6ff; */
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

