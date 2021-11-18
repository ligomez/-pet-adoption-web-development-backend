# README #

## Backend del proyecto AdoptLife

Desarrollado por los integrantes del grupo # 2 - P19:
- Adolfo Cuartas - leonmesa29@gmail.com
- Jairo Cortes - jairodanielcortesguerrero@gmail.com / jadanielc@gmail.com
- Liliana Gómez - gomez.liliana333@gmail.com
- Camilo Zaque - zaquecamilo@gmail.com

Se desarrolla usando Python, Django, PostgreSQL, Node.js.

### Descripción del proyecto
- A diario cientos de mascotas son abandonadas a lo largo del país, cifra que ha incrementado durante la pandemia en Colombia. Ayudando a que esta problemática no se convierta en una emergencia sanitaria, surge esta plataforma que ayudará a reubicar mascotas en nuevos hogares disminuyendo tanto la situación de abandono en las calles de nuestro país como también el periodo de permanencia de las mascotas en un refugio por medio de un proceso de adopción sencillo y eficiente. 

- Nuestra plataforma permite consolidar la información de mascotas que buscan un hogar a lo largo de Colombia y propicia conexiones entre familias adoptantes y refugios/usuarios con mascotas en adopción. De esta forma facilitamos el proceso de búsqueda para ambas partes, ampliando el alcance de este a nivel nacional y agrupando todas las opciones posibles en un solo sitio web.

### Requerimientos para ejecución
Se debe tener instalado Python en su versión 3.7 o posterior, además verificar que está agregado al path de la maquina, para verificar ejecuta los siguientes comandos:
~~~
python --version
pip --version  
~~~
Tambien se requiere tener Git instalado, para verificar la instalación ejecutamos:
~~~
git --version  
~~~
Si todos retornan una versión ya se puede continuar al siguiente paso para la ejecución.

### Ejecución del proyecto
Se debe clonar el repositorio a la maquina donde se quiere ejecutar, para ello debemos asegurarnos de tener git instalado para ejecutar:
~~~
git clone https://bitbucket.org/ligomezm/adoptlife.git
~~~

Para ejecución local se debe correr el siguiente comando para crear el entorno de desarrollo local:

~~~
python -m venv env
~~~

Esto creará una nueva carpeta nueva en la raiz del proyecto, ahora para entrar en dicho entorno ejecuta:
~~~
./env/Scripts/activate
~~~
Para saber si funcionó debe aparecer (env) antes de la ruta donde nos situamos en la terminal.

Ahora se deben instalar las dependencias del proyecto, estas se encuentran en el archivo requirements.txt, ejecuta lo siguiente para instalar todas las dependencias automáticamente:
~~~
pip install -r requirements.txt
~~~

> Nota: Si se tiene otra base de datos PosgreSQL hay que modificar los parametros de acceso en el archivo settings.py en la carpeta del proyecto.

El último paso es ejecutar el servidor local con el proyecto, para ello se ejecuta en terminal:
~~~
python manage.py runserver  
~~~

Eso sería todo para poner en marcha el proyecto.
