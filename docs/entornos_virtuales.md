# 1. Introducción

Un entorno virtual de Python es un **ambiente** creado con el objetivo de **aislar recursos**, como librerías y el entorno de ejecución, del sistema principal o de otros entornos virtuales. Lo anterior significa que en el mismo sistema, máquina o computadora, es posible **tener instaladas múltiples versiones** de una misma librería sin crear ningún tipo de conflicto.

Cuando se está desarrollando software con Python, es **común utilizar diferentes versiones de un mismo paquete**. Por ejemplo, imagina que estás desarrollando un videojuego con la versión 1.2 de `pygame` y mientras eso pasa, se comienza el desarrollo de otro videojuego que necesita las nuevas características presentes en la versión 1.3.

En este escenario, no es posible para los desarrolladores eliminar la version 1.2 e instalar la 1.3 en sus computadoras. Así que el problema a solucionar radica en cómo instalar las dos versiones de la misma librería con el fin de poder desarrollar ambos proyectos de forma simultánea.

La solución consiste en crear **entornos virtuales**. De esta manera, es posible instalar la versión 1.2 de `pygame` en un entorno virtual y la versión 1.3 en otro diferente o en el sistema principal sin problema alguno.

Para poder utilizar este simple pero poderoso concepto es necesario **instalar** una utilidad que permita gestionar la creación y utilización de dichos entornos virtuales.

> Hay muchas áreas de desarrollo de software sobre las que se debaten acaloradamente, pero el uso de entornos virtuales para el desarrollo de Python no es uno de ellos.

Históricamente, los desarrolladores de Python han usado `virtualenv` o `pyenv` para configurar entornos virtuales. Durante años, la comunidad se unió al `requirements.txt`, el archivo para administrar dependencias, pero hay algunas fallas sutiles que hacen que el manejo de las dependencias sea más confuso de lo necesario. Para solucionar estos problemas, la Python Packaging Authority, grupo responsable de muchas cosas, incluyendo `pip` y `PyPI`, propuso un sustituto al `requirements.txt` llamado `Pipfile`. Vamos a ver los dos formatos de archivo para ver por qué `Pipfile` se adapta mejor a la comunidad del futuro y cómo puede comenzar a usar uno. 

## 1.1. `requirements.txt`

Un archivo `requirements.txt` tiene una estructura muy primitiva. Veamos una muestra:

```
Jinja2==2.8
Markdown==2.4
MarkupSafe==0.23
PyYAML==3.11
Pygments==2.1.3
Werkzeug==0.11.4
argh==0.26.1
argparse==1.2.1
blinker==1.4
docutils==0.12
mock==1.0.1
pathtools==0.1.2
textile==2.2.2
watchdog==0.8.3
```

El requisito principal es que cada línea del archivo especifique una dependencia.

El ejemplo agrega un especificador de versión para cada paquete, aunque no es necesario. El archivo podría haber dicho `Jinja2` en lugar de `Jinja2==2.8`. En ese pequeño detalle, podemos empezar a ver debilidades en la estructura. ¿Qué es más correcto, especificar versiones o no? Pues... depende.

Especificar la versión de un paquete se llama anclar. Los archivos que anclan versiones para cada dependencia hacen posible la reproducción del entorno. Esta cualidad es muy valiosa para operar en un escenario de producción.

¿Cual es la desventaja? Es muy difícil determinar qué paquetes son dependencias directas. Por ejemplo, `handroll` utiliza directamente `Jinja2`, pero `MarkupSafe` solo se incluye porque es una dependencia de una dependencia. `Jinja2` depende de `MarkupSafe`. Por lo tanto, `MarkupSafe` es una dependencia transitiva de `handroll`.

La razón para incluir la dependencia transitiva vuelve a reproducir el entorno. Si solo enumeramos `Jinja2`, es posible `MarkupSafeque` se instale como versión actualizada que podría romper a `handroll`. Eso conduce a una mala experiencia de usuario.

Hemos llegado al problema central del formato anterior: `requirements.txt` está intentando tener dos vistas de dependencias.

- Un `requirements.txt` clavado actúa como un manifiesto para reproducir el entorno operativo.
- Un `requirements.txt` no clavado actúa como la lista lógica de dependencias de las que depende un paquete.

También hay un problema secundario relacionado con la audiencia. Si soy usuario de `handroll`, solo me preocupan las dependencias que hacen que la herramienta funcione. Si soy un desarrollador de `handroll`, también me gustaría tener las herramientas necesarias para el desarrollo (por ejemplo, un linter, herramientas de traducción, herramientas de carga para PyPI).

En esta etapa, las convenciones comienzan a desmoronarse en la comunidad. Algunos proyectos usan un archivo `requirements-dev.txt` de dependencias solo para desarrolladores. Otros optan por un directorio `requirements` que contiene muchos archivos de dependencias diferentes. Ambas son soluciones imperfectas.

Ahora estamos en condiciones de considerar lo que `Pipfile` trae al problema.

## `Pipfile`

`Pipfile` maneja los problemas con los que `requirements.txt` no puede. Es importante señalar que a `Pipfile` no es una creación novedosa sino que es una implementación para Python de un sistema que aparece en Ruby, Rust, PHP y JavaScript. Bundler, Cargo, Composer y Yarn son herramientas de cada uno de esos lenguajes que siguen un patrón similar. ¿Qué rasgos tienen estos sistemas en común?

- Divide las dependencias lógicas y hace un manifiesto de dependencia en archivos separados.
- Separa las secciones para las dependencias de usuarios y desarrolladores.

### `Pipfile` y `Pipfile.lock`

El archivo `Pipfile` gestiona las dependencias lógicas de un proyecto. Cuando escribo "lógico", me refiero a las dependencias de las que un proyecto depende directamente en su código. Una forma de pensar en las dependencias lógicas es como el conjunto de dependencias que excluyen las dependencias transitivas.

A la inversa, a `Pipfile.lock` es el conjunto de dependencias que incluyen las dependencias transitivas. Este archivo actúa como el manifiesto de dependencia que se utiliza al crear un entorno para producción.

> `Pipfile` es para la gente. `Pipfile.lock` es para computadoras.

Tener una clara distinción entre archivos ofrece un par de beneficios.

- Se puede leer y razonar sobre el `Pipfile`. No es necesario adivinar si una dependencia es una dependencia directa de un proyecto.
- Se pueden almacenar metadatos adicionales en `Pipfile.lock`. Los metadatos pueden incluir cosas como checksums sha256 que ayudan a verificar la integridad del contenido de un paquete.

### Usuarios y desarrolladores

El otro rasgo de `Pipfile` es la división entre las dependencias del usuario y del desarrollador. Veamos el `Pipfile` de `pytest-tap`, un proyecto convertido al formato `Pipfile`.

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[dev-packages]
babel = "*"
flake8 = "*"
mock = "*"
requests = "*"
tox = "*"
twine = "*"

[packages]
pytest = "*"
"tap.py" = "*"
```

Debido a que `Pipfile` usa TOML, puede incluir secciones mientras que `requirements.txt` no puede. Las secciones proporcionan una delimitación clara entre los paquetes de usuario y los paquetes de desarrollador.

`pytest-tap` es un plugig de `pytest` que produce la salida *Test Anything Protocol (TAP)*. Es un ajuste natural depender de `pytest` y `tap.py`, una biblioteca TAP.

Las otras dependencias hacen cosas específicas del desarrollador. `tox` y `mock` ayudan con la ejecución de la prueba, `twine` es para cargar el paquete en PyPI, y así sucesivamente.

Dividir las cosas permite a los usuarios habituales omitir la instalación de paquetes adicionales. Ese es el poder de un `Pipfile`.

### `pipenv`

En 2017 el destacado desarrollador de Python Kenneth Reitz, famoso por su librería `request`, lanzó `pipenv`, que ayuda a sus usuarios a añadir y retirar paquetes de sus `Pipfile` (y `Pipfile.lock`) y que ahora es la herramienta de empaquetado Python recomendada oficialmente por **PyPa** (*Python Packaging Authority*).

<iframe width="945" height="480" src="https://www.youtube.com/embed/GBQAKldqgZs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

`pipenv` es similar a `npm` y `yarn` del ecosistema Node:

- Crea un `Pipfile` con las dependencias de software
- Crea un `Pipfile.lock` para asegurar construcciones *deterministas*.

Éstos son archivos que buscan reemplazar el antiguo `requirements.txt` de `virtualenv` y `pyenv` con la sintaxis [TOML](https://github.com/toml-lang/toml) (*Tom's Obvious, Minimal Language*) para declarar todo tipo de dependencias. Un solo archivo `Pipfile` para reemplazar la variedad de `requirements.txt`. Ejemplo `dev-requirements`, `test-requirements`, etc.

El *determinismo* se refiere a que cada vez que se descargue el software en un nuevo entorno virtual, tendrá exactamente la **misma configuración**. *Sebastian McKenzie*, el creador de `yarn` que introdujo por primera vez este concepto al empaquetado de JavaScript, tiene una [publicación en su blog](https://yarnpkg.com/blog/2017/05/31/determinism/) concisa que explica qué es el *determinismo* y por qué es importante.

Los problemas que `pipenv` busca resolver son multifacéticos:

- No se necesitará usar más `pip` y `virtualenv` separados. Trabajan juntos.
- Manejar un archivo [`requirements.txt`](https://www.kennethreitz.org/essays/a-better-pip-workflow) puede ser problemático, por eso Pipenv usa en su lugar `Pipfile` y `Pipfile.lock`, que son superiores para usos básicos
- Los Hashes se usan en todas partes, siempre. Seguridad. Automáticamente expone vulnerabilidades de seguridad.
- Se recomienda encarecidamente el uso de las últimas versiones de dependencias para minimizar los riesgos de seguridad derivados de componentes obsoletos.
- Da una vista del árbol de dependecias (por ejemplo `$ pipenv graph`).
- Agiliza el flujo de desarrollo cargando archivos `.env`.

La conclusión es que **se debe crear un nuevo entorno virtual para cada nuevo proyecto en python**.

> **Nota sobre Pipenv y Anaconda**: No se recomienda utilizar  Pipenv con Anaconda, ya que Anaconda hace más o menos lo mismo que  “Pipenv” salvo por alguna excepcionalidad (se puede usar Pipenv con Anaconda,  pero es tener un “gestor de entornos virtuales” dentro de un “gestor de  entornos virtuales” cada uno gestionando entornos virtuales por su lado y a su modo). Se recomienda Pipenv si se trabaja sobre “Python común”.  Pipenv se instala con PIP en la carpeta “Lib” del “Python global” (si no se  tiene instalado Virtualenv lo instalará automáticamente como dependencia, pues lo necesita). Cuando se instala Pipenv se tendrá unas cuantas variables de entorno de Python en el sistema operativo (que se podrán usar en la consola) y que son: python, pip, virtualenv, pipenv. Se usará la nueva `pipenv` para gestionar los entornos virtuales (así que hay que olvidar utilizar `virtualenv` y sus comandos; aunque `pipenv` utiliza comandos semejantes). Pipenv creará los entornos virtuales (usa por debajo Virtualenv) en una carpeta que gestiona llamada `virtualenvs` y si se le pasan paquetes en la creación se podrán instalar (usa por debajo PIP).

# 2. ¿Cómo funciona Pipenv?

Por lo general, cuando se crea un proyecto de Python y se utiliza un entorno virtual para los paquetes, se tiene la tarea de crear el entorno virtual (usando el comando `py -m venv`), instalar dependencias en él y rastrear las  dependencias manualmente.

Pipenv proporciona una forma de hacer todo esto de forma semiautomática. El entorno virtual para el proyecto se crea y administra cuando se instalan paquetes a través de la interfaz de línea de comandos de `pipenv`. Las dependencias se rastrean y bloquean, y se pueden administrar las dependencias de desarrollo y tiempo de ejecución por separado. También se puede migrar desde archivos `requirements.txt` de la vieja escuela, por lo que no se necesita desarmar el proyecto e iniciarlo desde cero para usar bien `pipenv`.

Tenga en cuenta que, a diferencia de otras herramientas de administración de proyectos de Python (como [Poetry](https://www.infoworld.com/article/3527850/how-to-manage-python-projects-with-poetry.html)), `pipenv` no administra el "andamiaje" del proyecto. Es decir, `pipenv` no crea la estructura interna del directorio del proyecto con pruebas simuladas, comprobantes de documentación, etc., sino que se centra principalmente en la gestión de paquetes y entornos. Esto hace de `pipenv` una buena opción si solo se desea una herramienta para enfocarse en entornos  virtuales y paquetes, y no una solución todo en uno.

# 3. Instalar `pipenv`

Si bien [`pip`](https://pip.pypa.io/en/stable/installing/) puede instalar paquetes de Python, se recomienda `pipenv` ya que es una herramienta de nivel superior que simplifica la administración de dependencias para casos de uso comunes.

## 3.1. Instalación en Arch y derivadas (ArcoLinux, Manjaro, Anarchy, etc.)

Afortunadamente, dentro de los repositorios oficiales de Arch, se encuentra el paquete [python-pipenv](https://www.archlinux.org/packages/community/any/python-pipenv/) con lo que la instalación se convierte en algo tan sencillo como introducir el comando:

```bash
    $ pacman -S python-pipenv
```

## 3.2. Instalación en Debian y derivadas

Se usará `pip3` para instalar `pipenv` por tanto, debe estar instalado previamente. Para ello se usará:

```bash
    $ sudo apt install python3-pip
```

Gracias a `pip3` podemos instalar ahora `pipenv`.

```bash
    $ pip3 install --user pipenv
```

Esto hace una instalación de usuario para evitar romper cualquier paquete de todo el sistema. Si pipenv no está disponible en el shell **después de la instalación**, se deberá agregar el directorio binario de la base de usuarios al PATH.

Se puede encontrar el directorio binario de la base de usuarios ejecutando `python -m site --user-base` y agregando `bin` al final. Por ejemplo, esto normalmente imprimirá `~/.local` (con `~` expandido a la ruta absoluta al directorio de inicio) por lo que se deberá agregar `~/.local/bin` al PATH. Se puede establecer el PATH para que esté permanentemente modificando `~/.profile`.

Debería bastar con recargar `~/.profile` usando:

    source ~/.profile

## 3.3. Para usuarios de zsh

El comportamiento de `zsh` es algo distinto ya que se basa en usar un fichero de configurarión diferente a los habituales de Bash, por tanto, la instalación del nuevo `$PATH` dependerá ahora de configurar convenientemente el fichero `.zshrc` añadiéndole lo siguiente como primeras líneas de código:

```bash
    # If you come from bash you might have to change your $PATH.
    export PATH=$HOME/bin:/usr/local/bin:$PATH

    # set PATH so it includes user's private bin if it exists
    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi
```

# 4. Instalando paquetes del proyecto

Instalar paquetes para un proyecto no es apreciablemente diferente con `pipenv` que con `pip`; de hecho, la sintaxis es muy parecida. Abrir una consola en el directorio del proyecto y escribir `pipenv install <package_name>` para instalar un paquete para el proyecto. Para especificar que el paquete es una versión en desarrollo, usar la bandera `-d`. Se puede usar la sintaxis de `pip` para denotar una versión específica de un paquete (por ejemplo, `black==13.0b1`).

Cuando se instala un paquete con `pipenv`, suceden dos cosas. Primero, Pipenv verificará si ya se ha creado un entorno virtual para este directorio de proyecto. En caso afirmativo, Pipenv instalará el paquete en el entorno virtual existente. Si no, Pipenv creará un entorno virtual que usa la misma edición de Python utilizada para ejecutar Pipenv. Tenga en cuenta que el entorno virtual no se crea en el directorio del proyecto en sí; se crea en un directorio administrado por Pipenv en su perfil de usuario (más tarde se indicará como cambiar el directorio por defecto por uno del directorio del proyecto).

En segundo lugar, Pipenv instalará los paquetes solicitados en el entorno virtual. Cuando finalice la instalación, Pipenv informará sobre todo lo que hizo, incluida una ruta al entorno virtual si tuviera que crear uno.

Por lo general, no se necesita conocer la ruta al entorno virtual que crea Pipenv. Para activar el entorno, simplemente navegue hasta el directorio de su proyecto y úselo con pipenv shell para iniciar una nueva sesión de shell o úselo con `pipenv run <commando>` para ejecutar un comando directamente. Por ejemplo, use  `pipenv run mypy` para ejecutar la versión de la herramienta de línea de comandos de mypy (suponiendo que la herramienta mypy se instaló en el entorno virtual), o `pipenv run python -m <module>` para ejecutar un módulo Python disponible en el entorno virtual.

Pongámonos manos a la obra y ejecutemos el siguiente grupo de comandos:

```bash
    $ cd myproject
    $ pipenv install requests
```

Pipenv instalará la excelente biblioteca [`requests`](http://docs.python-requests.org/en/master/) y creará un archivo `pipfile` en el directorio del proyecto. `pipfile` se usa para **rastrear qué dependencias necesita el proyecto** en caso de que se necesite volver a instalarlas, como cuando se comparte el proyecto con otros.

## 4.1. `pienv` y archivos de bloqueo

Mira dentro del directorio después de haber instalado los paquetes con Pipenv, y verás dos archivos Pipfile y Pipfile.lock. Ambos son generados automáticamente por Pipenv, y no deben editarse directamente, ya que describen el estado de los paquetes en el proyecto.

`Pipfile` es el más simple de los dos. Simplemente enumera los paquetes necesarios para el proyecto, desde dónde están instalados (el valor predeterminado es PyPI) y qué versión de Python se necesita para ejecutar todo.

`Pipfile.lock` es más complejo. Enumera cada paquete junto con los detalles de la versión y los hash SHA-256 generados a partir del paquete. Los hashes se utilizan para garantizar que los paquetes instalados coincidan exactamente con lo especificado, no solo el número de versión, sino también el contenido obtenido.

Cuando trabaje en un proyecto que use Pipenv para la administración de paquetes, querrá agregar los archivos Pipfile y Pipfile.lock al repositorio de control de versiones para el proyecto. Cualquier cambio realizado en los paquetes para su proyecto alterará a su vez esos archivos, por lo que esos cambios deben ser rastreados y versionados.

## 4.1. Usar los paquetes instalados

Ahora que las solicitudes están instaladas, se puede crear un archivo `main.py` simple para usarlo:

```python
import requests

response = requests.get('https://httpbin.org/ip')
print('Su IP en Internet es {0}'.format(response.json()['origin'].split(',')[0]))
```

```bash
$ pipenv run python main.py
```

..y  obtener una salida similar a esta:

```
    Su IP es 8.8.8.8
```

El uso de `$ pipenv run` asegura que los paquetes instalados estén disponibles para el script. También es posible generar un nuevo *shell* que garantice que todos los comandos tengan acceso a los paquetes instalados con `$ pipenv shell`.

### Otro ejemplo: `pipenv` y Django

Crear un nuevo directorio y entrar en él.

```bash
    $ cd
    $ mkdir django
    $ cd django
```

Ahora se usa `pipenv` para instalar `django`

```
    $ pipenv install django
```
o si queremos la versión 3.2 específicamente utilizaremos

```
    $ pipenv install django==3.2
```
- Si se mira en el directorio, ahora hay dos nuevos archivos: `Pipfile` y `Pipfile.lock`. Se tiene la información que se necesita para el nuevo entorno virtual pero aún no ha sido activado. Se hace con:

```
  $ pipenv shell
```

  Debería verse ahora el nombre del entorno envuelto entre paréntesis precediendo al *prompt*.
  Si ahora se puede ejecutar `django-admin startproject` a continuación es que Django se ha instalado correctamente.

Lanzar entonces lo siguiente:

```
    (django) $ django-admin startproject test_project .
```

El `.` al final del comando no creará un directorio adicional para `test_project` pero sí todos los subdirectorios que se necesitan para la aplicación, en resumidas cuentas, se hará una instalación en el directorio en curso.

Se puede comprobar que todo funciona arrancando el servidor web local con:

```
    (django) $ python manage.py runserver
```

Si se visita `http://127.0.0.1:8000/` se debería ver la página inicial de Django.
El servidor se parará con `C-c` y se saldrá del entorno virtual con el comando `exit`.

## 4.2. Desinstalar un entorno virtual

```
    pipenv --rm
```

## 4.3. Usar un proyecto Pipenv

Si descargas un repositorio de origen para un proyecto que usa Pipenv para la administración de paquetes, todo lo que necesitas hacer es desempaquetar el contenido del repositorio en un directorio y ejecutarlo con `pipenv install` (no se necesitan nombres de paquetes). Pipenv leerá los archivos Pipfile y Pipfile.lock para el proyecto, creará el entorno virtual e instalará todas las dependencias según sea necesario.

Finalmente, si deseas usar Pipenv para administrar un proyecto que actualmente usa un fichero requirements.txt, simplemente navega al directorio del proyecto y ejecúta `pipenv install`. Pipenv detectará el  `requirements.txt` (o puede usar el indicador -r para señalarlo) y migrarás todos los requisitos a un `Pipfile`.

## 4.4. Advertencia: mapeo de Virtualenv

*Pipenv* asigna automáticamente proyectos a sus ***virtualenvs*** específicos.
El *virtualenv* se almacena globalmente con el nombre del directorio raíz del proyecto más el hash de la ruta completa a la raíz del proyecto (por ejemplo, `my_project-a3de50`).
Si cambia la ruta de su proyecto, interrumpe dicha asignación predeterminada y pipenv ya no podrá encontrar y usar el *virtualenv* del proyecto.
Es posible que desees establecer la exportación

```bash
export PIPENV_VENV_IN_PROJECT= 1
```

en `.bashrc/` ó `.zshrc/` (o cualquier archivo de configuración de shell) para crear el *virtualenv* dentro del directorio del proyecto, evitando problemas con los cambios de ruta posteriores.

`PIPENV_VENV_IN_PROJECT` es una variable de entorno, simplemente configúrala (**el valor no importa**, pero **no debe estar vacío**). Asegúrate de exportarla para que los procesos secundarios del shell puedan verla:

```bash
export PIPENV_VENV_IN_PROJECT= "enabled"
```

Esto hace que virtualenv se cree en el directorio `.venv ` junto al archivo `Pipfile` . Utiliza

```bash
unset PIPENV_VENV_IN_PROJECT
```

para eliminar la opción nuevamente.

>Es posible que quieras ver si el proyecto [`direnv`](http://direnv.net) puede ser útil aquí. Establece variables de entorno, automáticamente, cuando ingresas al directorio del proyecto, siempre que haya creado un archivo `.envrc` en el directorio del proyecto y habilitado el directorio con `direnv`. Luego se pueden agregar dichos comandos de exportación a ese archivo.



## 4.5. Borrar un entorno virtual

Si por algún motivo movemos el directorio del proyecto, las referencias al entorno virtual ya no serán válidas y habrá que generar uno nuevo.

Primero borraremos el entorno virtual inválido usando el comando:

```bash
pipenv --rm
```

También puede realizarse a mano borrándolo del directorio `~/.local/share/virtualenv/<entorno virtual>`.

Puede ocurrir que, si la variable de entorno `PIPENV_VENV_IN_PROJECT` es tá a `1`,  el entorno virtual estará en un directorio oculto de nombre `.venv` dentro del directorio del propio proyecto y procederemos a borrarlo igualmente.

Una vez que nos hemos deshecho del entorno antiguo crearemos uno nuevo a partir de los ficheros `Pipfile` y `Pipfile.lock` con :

```bash
pipenv install
```

## 4.6. Enlaces

[Pipenv: Flujo de trabajo en Python para humanos.](https://pipenv-es.readthedocs.io/es/latest/)

# 5. Otros entornos de virtualización de python

## 5.1. [`virtualenv`](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)

### 5.1.1. Cómo instalar `virtualenv`

Se puede instalar la utilidad `virtualenv` utilizando el gestor de paquetes de las diferentes distribuciones Linux:

Los siguientes comandos instalarán la utilidad `virtualenv` para las versiones 2 y 3 de Python.

```
$ sudo apt-get install python-virtualenv virtualenv
```

También es posible instalar `virtualenv` utilizando el instalador de paquetes de Python pip:

```
$ sudo pip install virtualenv
```

### 5.1.2. Cómo crear un entorno virtual de Python con `virtualenv`

1. `virtualenv` con Python 3

Para crear un entorno virtual con Python 3, simplemente ejecutamos el comando `virtualenv` de la siguiente manera:

```
$ virtualenv <entorno> --python=python3
```

Python 3 debe estar instalado de antemano para poder crear el entorno virtual.

2. `virtualenv` con Python 2

Para crear un entorno virtual con Python 2, simplemente ejecutamos el comando `virtualenv` de la siguiente manera:

```
        $ virtualenv <entorno>
```

Lamentablemente, no es posible crear un entorno virtual que contenga las dos versiones de Python al mismo tiempo.

### 5.1.3. Estructura de un entorno virtual de Python

La ejecución de comandos anteriormente explicados crean el directorio `<entorno>/` con la siguiente estructura:

```
    env/
      bin/
      include/
      lib/
        site-packages/
```

En el directorio `bin/` se encuentran los ejecutables necesarios para interactuar con el entorno virtual. En el directorio `include/` se encuentran algunos archivos de cabecera de C (cuya extensión es \*.h) necesarios para compilar algunas librerías de Python.

Finalmente, en el directorio `lib/` se encuentra una copia de la instalación de Python así como un directorio llamado `site-packages/` en donde se almacenan los paquetes Python instalados en el entorno virtual.

### 5.1.4. Cómo activar un entorno virtual de Python con virtualenv

Para activar un entorno virtual de Python, se ejecuta el script `activate` de `virtualenv` instalado en el directorio `bin/`:

```bash
$ cd env
$ source bin/activate ó $ . bin/activate
(env)$
```

El prompt de la terminal indica que el entorno virtual `mi_proyecto` está activado. Ya es posible utilizar los paquetes Python instalados en el entorno virtual así como instalar paquetes adicionales.

### 5.1.5. Cómo desactivar un entorno virtual de Python con `virtualenv`

Para desactivar un entorno virtual, porque se necesita trabajar en otro diferente, se ejecuta el comando `deactivate` de `virtualenv`. No es necesario ir al directorio del entorno virtual para realizar esta operación:

```
    (env)$ deactivate
```

El prompt de la terminal indica que el entorno virtual ha sido desactivado con éxito.

### 5.1.6. Cómo instalar paquetes en un entorno virtual de Python

Después de activarlo, lo único que resta es instalar los paquetes que sean necesarios usando el instalador de paquetes `pip`.
Al momento de crear un entorno virtual, la utilidad `virtualenv` instala de manera automática el ejecutable `pip`.
Por ejemplo, para instalar `Django` se ejecuta el siguiente comando:

```
    (env)$ pip install Django
```

Nótese que el prompt de la terminal indica que el entorno virtual `env` está activado de antemano.

### 5.1.7. ¿En qué directorio ubico el código fuente de mi proyecto?

La ubicación del código fuente del proyecto en el que se está trabajando no es importante. Puede ser colocado inclusive dentro del directorio del entorno virtual. Una vez que el entorno virtual está activado, todas las librerías de Python que se instalen solo podrán ser usadas al activar ese entorno virtual específico.

### 5.1.8. Instrucciones de instalación de `virtualenv` de EDX

Para comprobar si tenemos VirtualEnv instalado: virtualenv
Para instalar VirtualEnv: sudo apt install virtualenv
Para crear un directorio donde almacenar los entornos virtuales: mkdir ~/.virtualenvs
Para crear el entorno virtual: virtualenv ~/.virtualenvs/web
Impedir la instalación de módulos fuera de un entorno virtual: export PIP<sub>REQUIRE</sub><sub>VIRTUALENV</sub>=true
Permitir eliminar el valor de dicha variable de entorno: unset PIP<sub>REQUIRE</sub><sub>VIRTUALENV</sub>
Instalar módulo pprint: pip3 install pprint
Para abrir fichero bashrc y especificar en él que debe haber un entorno activo para la instalación de módulos: emacs .bashrc &
Activar entorno virtual: source .virtualens/web/bin/activate
Desactivar el entorno virtual: deactivate
Para conocer qué Python se está ejecutando: which python3
Instalar módulo Flask (necesario tener el entorno virtual web activado): pip3 install flask

## 5.2. VirtualEnvWrapper

VirtualEnvWrapper es una utilidad de Python con la que podemos trabajar con entornos virtuales (creando, activando y desactivando) de forma equivalente a lo que has visto en el vídeo. Si quieres utilizarla (no es necesario), tendrás que instalarla a través de pip:

```bash
$ sudo pip3 install virtualenvwrapper
```

Antes de empezar a trabajar con la utilidad, es necesario configurarla, lo cual significa fijar dos variables de entorno e invocar un script.

Podemos fijar las variables desde la terminal, pero es más cómodo hacerlo en el bashrc para que cada vez que arranques una sesión de bash, estas variables se fijen. Para ello, abrimos el fichero con un editor de texto como emacs:

```bash
$ emacs .bashrc &
```

La primera variable de entorno que necesito es el WORKON<sub>HOME</sub>, que es equivalente al directorio ~/.virtualenvs. Básicamente lo que le está diciendo al wrapper es dónde está el directorio con los entornos virtuales. Escribimos al final del fichero:

```config
export WORKON<sub>HOME</sub>=~/.virtualenvs”
```

Con VIRTUALENVWRAPPER<sub>PYTHON</sub> le estamos diciendo qué versión de Python queremos que utilice el wrapper:

```config
export VIRTUALENVWRAPPER<sub>PYTHON</sub>=/usr/bin/python3
```

Y por último hay que invocar a este script, que fija las variables de entorno para que el wrapper funcione:

```
./usr/local/bin/virtualenvwrapper.sh. 
```

También podemos fijar en este archivo la variable VIRTUALENV para que no nos permita instalar ni desinstalar nada si no es un entorno virtual activo:

```
export PIP<sub>REQUIRE</sub><sub>VIRTUALENV</sub>=true
```

Importante: guarda los cambios hechos en el fichero bash.

A partir de ahora, con el comando workon puedo saber los entornos virtuales que tengo en mi máquina, en el directorio que hemos especificado, y me permite además activar en un entorno virtual concreto:

```bash
$ workon web
```

Para desactivarlo, utilizamos el comando:

```bash
$ deactivate
```

Para crear un nuevo entorno virtual:

```bash
$ mkvirtualenv web2
```

Para borrar un entorno virtual, utilizo:

```bash
$ rmvirtualenv web2
```

# 6 Entornos virtuales en Visual Studio Codium/Code

Un entorno consta de un intérprete y cualquier número de paquetes instalados. La extensión de Python para VS Codium/Code proporciona funciones de integración útiles para trabajar con diferentes entornos.

## 6.1. Seleccionar y activar un entorno

De forma predeterminada, la extensión de Python busca y usa el primer intérprete de Python que encuentra en la ruta del sistema. Si no encuentra un intérprete, emite una advertencia (en cualquier caso, se puede deshabilitar estas advertencias configurando `python.disableInstallationCheck` en `true` en la configuración de usuario).

Para seleccionar un entorno específico, usar `Python: Select Interpreter` en la Paleta de comandos(`Ctrl+Shift+P`).

Se puede cambiar de entorno en cualquier momento; los entornos de conmutación ayudan a probar diferentes partes de un proyecto con diferentes intérpretes o versiones de biblioteca según sea necesario.

El comando `Python: Select Interpreter` muestra una lista de los **entornos globales** disponibles, los entornos **conda** y los **entornos virtuales**.  La siguiente imagen, por ejemplo, muestra varias instalaciones de Anaconda y CPython junto con un entorno conda y un entorno virtual (env) que se encuentra dentro de la carpeta del espacio de trabajo.

<p align="center">
<img src="https://code.visualstudio.com/assets/docs/python/environments/interpreters-list.png">
</p>

Al seleccionar un intérprete de la lista, se agrega una entrada para `python.pythonPath` con la ruta al intérprete dentro de la Configuración del área de trabajo. Debido a que la ruta forma parte de la configuración del espacio de trabajo, el mismo entorno ya debería estar seleccionado cada vez que se abra ese espacio de trabajo.

La extensión de Python utiliza el entorno seleccionado para ejecutar el código de Python (usando el comando `Python: Run Python file`, proporcionando servicios del lenguaje (autocompletar, verificación de sintaxis, linting, formateo, etc.) cuando se tiene un archivo `.py` abierto en el editor, y abre un terminal con el comando `Terminal: Create a New Integrated Terminal`. En este último caso, VS Codium/Code activó automáticamente el entorno seleccionado.

> Para evitar la activación automática de un entorno seleccionado, agregar `"python.terminal.activateEnvironment": false` al archivo `settings.json` (se puede colocar en cualquier lugar como hermano de la configuración existente). 

> De manera predeterminada, VS Codium/Code usa el intérprete identificado por la configuración de `python:pythonPath` al depurar el código. Puede anular este comportamiento especificando una ruta diferente en la propiedad `pythonPath` de una configuración de depuración.

La barra de estado siempre muestra el intérprete actual. 

<p align="center">
<img src="https://code.visualstudio.com/assets/docs/python/environments/selected-interpreter-status-bar.png">
</p>
La barra de estado también refleja cuando no se selecciona ningún intérprete.

<p align="center">
<img src="https://code.visualstudio.com/assets/docs/python/environments/no-interpreter-selected-statusbar.png">
</p>

En cualquier caso, hacer clic en esta área de la barra de estado es un atajo conveniente para el comando `Python: Select Interpreter`.

1. Entornos y ventanas de terminal
   
   Después de usar `Python: Select Interpreter`, ese intérprete se aplica al hacer clic con el botón derecho en un archivo y seleccionar `Python: Run Python File` en la Terminal. El entorno también se activa automáticamente cuando usa el comando `Terminal: Create New Integrated Terminal`, a menos que se cambie la configuración de `python.terminal.activateEnvironment` a `false`.
   
   Sin embargo, el lanzamiento de VS Codium/Code desde un shell en el que se activa un determinado entorno de Python no activa automáticamente ese entorno en el terminal integrado predeterminado. Usar el comando `Terminal: Create new Integrated Terminal` después de que se esté ejecutando el código VS.
   
   **Cualquier cambio que realice en un entorno activado dentro del terminal es persistente**. Por ejemplo, al utilizar `conda install <package>` desde el terminal con un entorno `conda` activado, se instala el paquete en ese entorno de forma permanente. De manera similar, el uso de `pip install` en un terminal con un entorno virtual activado agrega el paquete a ese entorno.
   
   El cambio de intérpretes con el comando  `Python: Select Interpreter` no afecta a los paneles de terminales que ya están abiertos. De este modo, **se puede activar entornos separados** en un terminal dividido: seleccione el primer intérprete, cree un terminal para él, seleccione un intérprete diferente y luego use el botón dividir (<Ctrl>+\\) en la barra de título del terminal.

2. Elegir un entorno de depuración
   
   De forma predeterminada, la configuración `python.pythonPath` especifica el intérprete de Python que se usará para la depuración. Sin embargo, si se tiene una propiedad `pythonPath` en la configuración de depuración de `launch.json`, se usa ese intérprete en su lugar. Para ser más específicos, VS Codium/Code aplica el siguiente orden de precedencia al determinar qué intérprete usar para la depuración:
   
   1. Propiedad `pythonPath` de la configuración de depuración seleccionada en `launch.json`
   2. Configuración de `python.pythonPath` en el espacio de trabajo de `settings.json`
   3. Configuración de `python.pythonPath` en setting del usuario `settings.json`
   
   Para obtener más detalles sobre la configuración de depuración, consultar [Depuración de configuraciones](https://code.visualstudio.com/docs/python/debugging).

3. ¿Dónde busca la extensión de Python los entornos virtuales?
   
   La extensión busca automáticamente intérpretes en las siguientes ubicaciones:
   
   - Rutas de instalación estándar como `/usr/local/bin`, `/usr/sbin`, `/sbin`, `c:\python27`, `c:\python36` , etc.
   - Entornos virtuales ubicados directamente debajo de la carpeta del área de trabajo (proyecto).
   - Los entornos virtuales ubicados en la carpeta identificada por la configuración `python.venvPath`, que puede contener múltiples entornos virtuales. La extensión busca entornos virtuales en las subcarpetas de primer nivel de `venvPath`.
   - Intérpretes instalados por pyenv.
   - Un entorno `pipenv` para la carpeta de trabajo. Si se encuentra uno, no se busca ni se enumera ningún otro intérprete, ya que pipenv espera gestionar todos los aspectos del entorno.
   - Los entornos Conda que contienen un intérprete de Python. VS Codium/Code no muestra los entornos de Conda que no contienen un intérprete.
   - Intérpretes instalados en una carpeta `.direnv` por `direnv` bajo la carpeta (proyecto) de trabajo.
   
   También se puede [especificar manualmente un intérprete](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter) si VS Codium/Code no lo localiza automáticamente.
   
   La extensión también carga un [archivo de definiciones de variables de entorno](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file) identificado por el fichero de configuración `python.envFile`. El valor predeterminado de esta configuración es `${workspaceFolder}/.env`.

4. Entornos globales, virtuales y conda.
   
   De forma predeterminada, cualquier intérprete de Python que se haya instalado se ejecuta en su propio entorno global, que no es específico de ningún proyecto. Por ejemplo, si solo se ejecuta python o python3 en un nuevo símbolo del sistema, se está ejecutando en el entorno global de ese intérprete. En consecuencia, cualquier paquete que se instale o desinstale afectará el entorno global y todos los programas que se ejecuten dentro de ese contexto.
   
   Aunque trabajar en el entorno global es una forma fácil de comenzar, con el tiempo, ese entorno se llenará de muchos paquetes diferentes que habrán instalado para diferentes proyectos. Tal desorden hace que sea difícil probar una aplicación a fondo contra un conjunto específico de paquetes con versiones conocidas, que es exactamente el tipo de entorno que se configuraría en un servidor de compilación o servidor web.
   
   Por esta razón, los desarrolladores a menudo crean un entorno virtual para un proyecto. Un entorno virtual es una subcarpeta en un proyecto que contiene una copia de un intérprete específico. Cuando se activa el entorno virtual, los paquetes que se instalen lo harán solo en la subcarpeta de ese entorno. Cuando luego se ejecuta un programa Python dentro de ese entorno, sabe que se está ejecutando solo contra esos paquetes específicos.
   
   Un entorno de Conda es un entorno de Python que se administra mediante el gestor de paquetes  `conda` (consultar [Comenzar con conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)). Conda funciona bien para crear entornos con dependencias interrelacionadas, así como paquetes binarios. A diferencia de los entornos virtuales, que están incluidos en un proyecto, los entornos de Conda están disponibles globalmente en cualquier computadora. Esta disponibilidad hace que sea fácil configurar varios entornos de conda distintos y luego elegir el adecuado para cualquier proyecto dado.
   
   Como se señaló anteriormente, la extensión de Python detecta automáticamente los entornos de conda existentes siempre que el entorno contenga un intérprete de Python. Por ejemplo, el siguiente comando crea un entorno conda con el intérprete de Python 3.4 y varias bibliotecas, que el Código VS luego muestra en la lista de intérpretes disponibles:
   
   `conda create -n env-01 python=3.4 scipy=0.15.0 astroid babel`
   
   Por el contrario, si no se especifica un intérprete, como con `conda create --name env-00`, el entorno no aparecerá en la lista.
   
   Para obtener más información sobre la línea de comandos de conda, consulte [Entornos de Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

5. Especificar manualmente un intérprete
   
   Si VS Codium/Code no localiza automáticamente el intérprete que desea usar, puede configurar la ruta de acceso manualmente en su archivo del área de trabajo `settings.json`. Con cualquiera de las entradas que siguen, se puede agregar la línea como un añadido más a otras configuraciones existentes.)
   
   Primero, seleccione el comando de menú `File > Preferences > Settings` (<Ctrl>+,) para abrir la Configuración, seleccionar `Workspace`.
   
   A continuación, realizar cualquiera de los siguientes pasos:
   
   - Crear o modificar una entrada para `python.pythonPath` con la ruta completa al ejecutable de Python (si se edita `settings.json` directamente, agregar la siguiente línea como configuración):
     
     - Por ejemplo:
       
       - Windows:
         
         `"python.pythonPath" : "c:/python36/python.exe"`
         
         - macOS / Linux:
           
           `"python.pythonPath" : "/home/python36/python"`
   
   - También se puede usar `python.pythonPath` para apuntar a un entorno virtual, por ejemplo:
     
     Windows:
     
     - &ldquo;python.pythonPath&rdquo; : &ldquo;c:/dev/ala/venv/Scripts/python.exe&rdquo;
     
     macOS / Linux:
     
     - &ldquo;python.pythonPath&rdquo; : &ldquo;/home/abc/dev/ala/venv/bin/python&rdquo;
   
   - Se puede usar una variable de entorno en la configuración de ruta usando la sintaxis `${env:VARIABLE}`. Por ejemplo, si se ha creado una variable llamada `PYTHON_INSTALL_LOC` con una ruta a un intérprete, se puede usar el siguiente valor de configuración:
     
     - &ldquo;python.pythonPath&rdquo; : &ldquo;${env:PYTHON<sub>INSTALL</sub><sub>LOC</sub>}&rdquo;
     
     Al usar una variable de entorno, se puede transferir fácilmente un proyecto entre sistemas operativos donde las rutas son diferentes, solo hay que asegurarse de establecer primero la variable de entorno en el sistema operativo.

### Archivo de definiciones de variables de entorno

Un archivo de definiciones de variables de entorno es un archivo de texto simple que contiene pares clave-valor en forma de `variable_de_entorno=valor`, con # utilizado para comentarios. Los valores de multilínea no son compatibles, pero los valores pueden referirse a cualquier otra variable de entorno que ya esté definida en el sistema o anterior en el archivo.

De forma predeterminada, la extensión de Python busca y carga un archivo llamado `.env` en la carpeta del área de trabajo actual, luego aplica esas definiciones. El archivo se identifica mediante la entrada predeterminada `"python.envFile": "${workspaceFolder}/.env"` en la configuración del usuario. Se puede cambiar la configuración de `python.envFile` en cualquier momento para usar un archivo de definiciones diferente.

Una configuración de depuración también contiene una propiedad `envFile` que también se establece de manera predeterminada en el archivo `.env` en el área de trabajo actual. Esta propiedad permite establecer fácilmente variables para fines de depuración que reemplazan las variables especificadas en el archivo `.env` predeterminado.

Por ejemplo, al desarrollar una aplicación web, es posible que se desee cambiar fácilmente entre los servidores de desarrollo y de producción. En lugar de codificar las diferentes URL y otras configuraciones en la aplicación directamente, se pueden usar archivos de definiciones separados para cada una. Por ejemplo:

Archivo `dev.env`

```
    # dev.env - development configuration

    # API endpoint
    MYPROJECT_APIENDPOINT=https://my.domain.com/api/dev/

    # Variables for the database
    MYPROJECT_DBURL=https://my.domain.com/db/dev
    MYPROJECT_DBUSER=devadmin
    MYPROJECT_DBPASSWORD=!dfka**213= 
```

Archivo `prod.env`

```
    # prod.env - production configuration
    # API endpoint 
    MYPROJECT_APIENDPOINT=https://my.domain.com/api/ 

    # Variables for the database
    MYPROJECT_DBURL=https://my.domain.com/db/
    MYPROJECT_DBUSER=coreuser
    MYPROJECT_DBPASSWORD=kKKfa98*11@ 
```

A continuación, se puede establecer la configuración `python.envFile` a `${workspaceFolder}/prod.env`, luego establecer la propiedad `envFile` en la configuración de depuración en `${workspaceFolder}/dev.env`.

1. Sustitución de variables
   
   Al definir una variable de entorno en un archivo de definiciones, se puede utilizar el valor de cualquier variable de entorno existente con la siguiente sintaxis general:
   
   ```
       <VARIABLE>=... ${EXISTING_VARIABLE} ... 
   ```
   
   donde `...` significa cualquier otro texto usado en el valor. Las llaves son necesarias.

Dentro de esta sintaxis, se aplican las siguientes reglas:

- Las variables se procesan en el orden en que aparecen en el archivo `.env`, por lo que se puede usar cualquier variable que se haya definido anteriormente en el archivo.
- Las comillas simples o dobles no afectan el valor sustituido y se incluyen en el valor definido. Por ejemplo, si el valor de `VAR1` es `abcedfg`, entonces `VAR2='${OTHERVAR}'` asigna el valor `'abcedfg'` a `VAR2`.
- El carácter `$` se puede escapar con una barra invertida, como en `\$`.
- Se puede usar la sustitución recursiva, como `PYTHONPATH=${PROJ_DIR}:${PYTHONPATH}` (donde `PROJ_DIR` es cualquier otra variable de entorno).
- Se puede usar solo la sustitución simple; anidar como `${_${OTHERVAR}_EX}` no es compatible.
- Las entradas con sintaxis no admitida se dejan como están.

### Uso de la variable PYTHONPATH

La variable de entorno `PYTHONPATH` especifica ubicaciones adicionales donde el intérprete de Python debe buscar módulos. El valor de `PYTHONPATH` puede contener múltiples valores de ruta separados por `os.pathsep` (puntos y coma en Windows, dos puntos en Linux/macOS). Las rutas no válidas se ignoran.

Nota: se debe configurar la variable `PYTHONPATH` a través del sistema operativo, ya que VS Codium/Code no proporciona un medio para establecer las variables de entorno directamente.

En el Código VS, `PYTHONPATH` afecta la depuración, el linting, el IntelliSense, las pruebas de unidades y cualquier otra operación que dependa de los módulos de resolución de Python. Por ejemplo, suponga que se tiene el código fuente en una carpeta `src` y las pruebas en una carpeta de tests. Sin embargo, al ejecutar pruebas, normalmente no pueden acceder a los módulos en `src` menos que se codifiquen las rutas relativas. Para resolver este problema, se agrega la ruta a `src` a `PYTHONPATH`.

Se recomienda que establezca la variable `PYTHONPATH` en un archivo de definiciones de variable de entorno, descrito anteriormente.

Nota: `PYTHONPATH` no, repetimos **no**, especifica una ruta al intérprete de Python y, por lo tanto, nunca se usa con la configuración `python.pythonPath`. Claramente, la variable de entorno está mal llamada, pero&#x2026; *c&rsquo;est la vie*. Así que asegurarse de leer la documentación de `PYTHONPATH` varias veces y téngase en cuenta que `PYTHONPATH` **no es un camino a un intérprete**.

## 6.2. Bootstrap

- Instalar con:
  
  ```bash
  $ pipenv install bootstrap4
  ```

## 7. Referencias

[Pipenv & Virtual Environments; The Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/)

[Python Tutorial: Pipenv - Easily Manage Packages and Virtual Environments](https://www.youtube.com/watch?v=zDYL22QNiWk)

[Using Pipenv to manage Python virtual environments and packages](
https://www.youtube.com/watch?v=0CKuaf11H5Q)

[How to manage Python projects with Pipenv](https://www.infoworld.com/article/3561758/how-to-manage-python-projects-with-pipenv.html)
