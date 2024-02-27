# pagina-de-visualizacion-del-simparh
Proyecto del ADA para realizar una pagina web con la capacidad de mostrar en un mapa dinámico las distintas
estaciones de recopilación de datos metereológicos y fluviales. 

Objetivos:
	·Crear mapa dinamico que permita visualizar las distintas estaciones de monitoreo y sus datos.
	El mismo deberá tambien poder mostrar regiones hidrograficas y otros aspectos fluviales y meteorologicos
	de ser necesario. También es necesario poder aplicar distintos filtros para permitir que la información sea
	legible.
	
	·Tener una seccion para poder acceder a los contactos de ciertas personas/departamentos/instituciones por
	 medio de un menú de selección

Participantes:

	·Facundo Cadaa
	·Sebastian Baldini
	·Franco Serra
	·Luciano Otero Nolte
	·Facundo Medina
	·Iara Caruso
	·Mariano Gandin


Necesario installar:
	Python{
	(En el venv via pip debería quedar así):
		Package                  Version
		------------------------ --------
		asgiref                  3.6.0
		defusedxml               0.7.1
		diff-match-patch         20200713
		Django                   4.1.7
		django-cors-headers      3.14.0
		django-import-export     3.1.0
		django-phonenumber-field 7.0.2
		django-phonenumbers      1.0.1
		djangorestframework      3.14.0
		et-xmlfile               1.1.0
		MarkupPy                 1.14
		odfpy                    1.4.1
		openpyxl                 3.1.2
		phonenumbers             8.13.7
		pip                      23.0.1
		pytz                     2023.3
		PyYAML                   6.0
		setuptools               65.5.0
		sqlparse                 0.4.3
		tablib                   3.4.0
		xlrd                     2.0.1
		xlwt                     1.3.0

	Para instalar dependencias:

		pip install Django
		pip install django-phonenumbers
		pip install django-phonenumber-field
		pip install django-import-export
		pip install djangorestframework
		pip install django-cors-headers

		Resumen:
		
		pip install Django django-phonenumbers django-phonenumber-field django-import-export djangorestframework django-cors-headers

	Para correr el local server:

		python -m venv venv (como administrador)

		python manage.py runserver
		python manage.py make migration
		python manage.py migrate

	Para correr vite-vue run:  
	
		cd front
		npm install   
		npm run dev 


	}
	JS{
	hay qur tener instalada la version 18.15.0 de node.js y el npm 9.5.0
	(en debian:
	apt update
	apt upgrade
	apt install curl
	curl -sL https://deb.nodesource.com/setup_16.x | bash -
	apt install nodejs
	//se comprueba haciendo node-v y npm -v//
	
	adamas debemos ejecutar
		npm install vite

		npm i vue-chartjs chart.js
		(^para los graficos)
		
		npm i @vue-leaflet/vue-leaflet leaflet
		npm install axios
		(^para los mapas)
		
		npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
		npm install flowbite
		npm i flowbite-vue
		(^para el ccs en general)
	}
	{CCS
	https://www.c-sharpcorner.com/article/how-to-add-tailwind-css-in-vue-js/
	para tailwind
	
	https://flowbite.com/docs/getting-started/vue/
	para flowbite
	}
	
