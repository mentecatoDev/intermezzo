# Gestionar las cuentas de usuario de un colegio de 1200 alumnos con Python y La API de Google

[![Goyo Regalado](https://miro.medium.com/fit/c/48/48/0*72uQ1EgyJRt_kDHc.)](https://medium.com/@goyoregalado?source=post_page-----87cb8a051f25----------------------)

[Goyo Regalado](https://medium.com/@goyoregalado?source=post_page-----87cb8a051f25----------------------)Follow

[Oct 13, 2019](https://medium.com/@goyoregalado/gestionar-las-cuentas-de-usuario-de-un-colegio-de-1200-alumnos-con-python-y-la-api-de-google-87cb8a051f25?source=post_page-----87cb8a051f25----------------------) · 13 min read









Actualmente trabajo como jefe de estudios de un centro escolar en Tenerife. Nuestro centro dispone del servicio G-Suite for education de google. Tenemos 1200 alumnos y unos 70 profesores. Nuestro equipo TIC dispone exactamente de una hora semanal para gestionar el acceso de estas 1270 personas.

Esta es la historia sobre cómo lo hacemos y he decidido escribirla sólo por si es de utilidad para alguien que pueda encontrarse en la misma situación. Todo el código está publicado en [mi repositorio de gitlab ](https://gitlab.com/goyoregalado/secuaz)y desde este momento es tan suyo como mío.

Desde el punto de vista del equipo TIC, lo que nos vendría bien es disponer de un esbirro, pero como la palabreja tiene connotaciones negativas, decidimos llamar a este proyecto “Secuaz”.

![img](https://miro.medium.com/max/30/1*ZOBmn2PAMPUtQkidXEPjtg.jpeg?q=20)

![img](https://miro.medium.com/max/1920/1*ZOBmn2PAMPUtQkidXEPjtg.jpeg)

Imagen de [Nino Carè](https://pixabay.com/es/users/ninocare-3266770/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1655783) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1655783)

# Descargo de responsabilidades

Ante todo me gustaría comenzar indicándoles que no puedo garantizar que este código vaya a resolver sus problemas, ni tampoco que no vaya a producir ningún tipo de pérdida de datos en su institución.

Puedo garantizarles que ha sido desarrollado intentando atender a todas las posibles causas de error y también que se ha escrito con la mejor de las voluntades, pero si se lía parda por utilizarlo… ¡El que avisa no es traidor!

Piensen que este es el resultado de un proyecto elaborado durante mi tiempo libre y por el placer de aprender y experimentar. Seguro que un equipo de profesionales con dedicación plena encontrará soluciones mejores que la mía, si es así, no duden en compartirla con todos nosotros y, a lo mejor, terminamos teniendo la herramienta que necesitamos todos ;)

He intentado testear todo lo posible este proyecto, pero no les puedo garantizar una cobertura del 100% del código, sigo trabajando sobre él y, en cuanto pueda, generaré mocks para toda la parte del acceso a la API de google, de momento, les garantizo que he hecho todo lo que he podido con el poquito tiempo de que dispongo (También les invito a ayudarme con eso)

# Un poco de contexto

Las decisiones de diseño que he tomado pueden parecer un tanto insólitas, pero creo que están justificadas. Vamos a ver cuál es el contexto en el que se desarrolla este proyecto.

Como centro escolar de la Comunidad Autónoma de Canarias, estamos obligados a utilizar una herramienta que se llama Pincel Ekade. Estoy seguro de que está repleta de endpoints, API’s y servicios web, pero yo no tengo acceso a ninguno así que tenemos que buscar una solución creativa para acceder a los datos.

Esta solución creativa tiene que cumplir con algunas premisas:

- Tiene que ser ágil. No puede conllevar gran procesamiento.
- Debe ser fácil de usar. La idea es que desde secretaría se pueda notificar la aparición de un nuevo alumno y que esto desencadene automáticamente la generación de su cuenta de usuario y la matrícula en los cursos definidos en Classroom para las asignaturas de las que está matriculado.
- Debe limitar la intervención humana al mínimo posible, recuerden, todo esto (y mucho más … ) se gestiona con sólo una hora semanal efectiva de trabajo.
- Debería garantizar que todos los usuarios cambian su contraseña en el primer inicio de sesión. No queremos disponer de las credenciales de acceso de ningún miembro de nuestra comunidad educativa.
- Si un estudiante de nuestra institución ya dispone de una cuenta corporativa, debería poder continuar utilizándola.
- Ya que estamos, habría que agrupar a los usuarios por clases, de manera que dispongamos de grupos de correo que permitan que nuestros docentes puedan llevar a cabo comunicaciones masivas entre sus alumnos de la manera más cómoda posible.
- Nuestra solución no debe permitir que salgan datos de nuestra infraestructura, limitando el uso de archivos temporales.
- Debe generarse una circular informativa por cada alumno en la que se muestre su correo electrónico, su contraseña inicial, que será temporal e información para las familias sobre las condiciones de uso de esta plataforma.

# ¿De dónde me saco yo estos datos?

Teniendo en cuenta los requisitos y las restricciones sólo se me ocurrió una posibilidad. ¿Y si utilizamos una hoja de cálculo de Google Docs almacenada en una unidad compartida de nuestro drive? Podríamos compartirla con el usuario específico de secretaría y una cuenta generada ex-profeso para la aplicación.

¿Tiene realmente sentido esto? Sin duda alguna sí. Más de uno debe estar revolviéndose en la silla. Dejen que me explique.

La aplicación que me ofrece la consejería de educación puede disponer de API’s, etc … pero a mi no me consta y no tengo acceso a su documentación, sin embargo, sí que exporta listados personalizados de alumnos en diversos formatos de hojas de cálculo. Por otro lado, no tengo ni tiempo ni ganas de estar pendiente de este proceso y mis compañeras de secretaría también están hasta arriba de trabajo, pero saben usar perfectamente una hoja de cálculo. ¿Por qué no aprovechar esta circunstancia?

El primer paso fue definir la salida desde Pincel Ekade. Tras dedicar un rato a pensar llegamos a la conclusión de que necesitábamos sólo un subconjunto de todos los datos disponibles.

![img](https://miro.medium.com/max/30/1*B1-axG9OW5-BvCuJQthZOg.png?q=20)

![img](https://miro.medium.com/max/2398/1*B1-axG9OW5-BvCuJQthZOg.png)

Los campos seleccionados para la exportación

Básicamente nos quedamos con el código que establece la administración educativa para cada alumno, su nombre, el nivel educativo en el que está matriculado, la clase concreta en la que se encuentra el estudiante, si es repetidor o no, si está matriculado del curso completo y la lista de asignaturas en las que está matriculado y las asignaturas que pudiera tener pendientes de cursos anteriores.

Esta aplicación de la administración permite definir informes personalizados, así que no hay que estar constantemente seleccionando columnas, el orden de salida ni nada por el estilo. Se define una vez y se exporta las que hagan falta.

No es poca información, pero sí es la mínima que necesitamos para cumplir con nuestro objetivo.

La idea es que cada vez que haya una modificación, mis compañeras simplemente exporten los datos y sin tener que volverse locas, copien la salida directamente en esta hoja de cálculo.

Nuestra aplicación debería ser capaz de detectar los cambios y aplicarlos.

El caso de los profesores es parecido, pero este listado es mucho menos dinámico que el de alumnos. Hemos optado por un archivo generado manualmente que representa una asignatura impartida por cada profesor en cada fila de la hoja de cálculo. Las cuentas de los profesores siempre estarán creadas antes del inicio de la importación así que identificaremos a cada profesor con su correo electrónico corporativo para evitar la ambigüedad.

![img](https://miro.medium.com/max/30/1*RJPHvIHdsjmOOu0uTceZUA.png?q=20)

![img](https://miro.medium.com/max/1708/1*RJPHvIHdsjmOOu0uTceZUA.png)

Este fichero cambia mucho menos que el de alumnos, así que lo elaboramos una vez durante el curso y probablemente se mantendrá.

El aspecto final del directorio dentro de nuestro drive, con todos los ficheros necesarios para mantener todas las cuentas de usuario de nuestro colegio es este:

![img](https://miro.medium.com/max/30/1*_4hnKtDNJRXPZ3G3LI_0Nw.png?q=20)

![img](https://miro.medium.com/max/1606/1*_4hnKtDNJRXPZ3G3LI_0Nw.png)

Con estas dos hojas de cálculo podemos gestionar todas las cuentas de usuario.

Otra cosa importante es que los nombres de los ficheros y de los directorios son totalmente irrelevantes, porque desde la API vamos a acceder a ellos a través de un identificador.

# ¿Cómo hago para que mi script acceda a los datos?

La autenticación de los usuarios así como el control de acceso a la API de google depende de que nuestro administrador de G-Suite nos conceda acceso a cada elemento de la API. Pero una vez hecho esto ya no nos tendremos que preocupar más.

![img](https://miro.medium.com/max/30/1*ya367lIcpA2hrzjfRYvb0A.png?q=20)

![img](https://miro.medium.com/max/2550/1*ya367lIcpA2hrzjfRYvb0A.png)

En la propia documentación de la API dispones de un botón que permite habilitar cada una de las API’s. Secuaz va a utilizar varias API’s de manera simultánea, les dejo los enlaces a la documentación de cada una de ellas donde podrán habilitarlas.

- API de hojas de cálculo: https://developers.google.com/sheets/api/quickstart/python
- API de google directory: https://developers.google.com/admin-sdk/directory/v1/quickstart/python?refresh=1
- API de google classroom: https://developers.google.com/classroom/quickstart/python
- API de google docs: https://developers.google.com/docs/api/quickstart/python

En la versión actual de Secuaz, no utilizamos la última API, hemos descubierto que un complemento para las hojas de cálculo de Google Docs cumple con casi todos los requisitos, no tenemos mucho tiempo para reinventar ruedas, así que optamos por generar las circulares con las credenciales utilizando [Autocrat](https://gsuite.google.com/marketplace/app/autocrat/539341275670?hl=es). Si no lo conoces aún, te garantizo que te va a dar más de una alegría.

Al habilitar cada API, vas a tener acceso a un cuadro de diálogo en el que podrás ver tus credenciales o descargarlas en formato JSON. Dado que nuestra intención es que la ejecución de este servicio sea totalmente desatendida, lo que hacemos es descargar el JSON para cada uno. Esto en si mismo, no es realmente necesario, podemos tener un único JSON para toda la aplicación, de hecho finalmente será así, pero de cara a probar los módulos de manera individual creo que es mucho más cómodo.

![img](https://miro.medium.com/max/30/1*KeXDMrmYYuRFsU4DDlM54w.png?q=20)

![img](https://miro.medium.com/max/1216/1*KeXDMrmYYuRFsU4DDlM54w.png)

Utilizando el botón Download client configuration podrás descargarte tus credenciales en formato JSON

# ¿Cómo se lleva a cabo el control de acceso?

Una de las cosas que más me sorprendió es el modelo de autenticación de usuarios.

Básicamente lo que hacemos para autenticar los accesos a la API es lo siguiente.

Una aplicación que ya ha sido autenticada debe disponer de un archivo serializado, en nuestro caso utilizamos el módulo pickle. Este archivo contiene el Token para la app.

Lo curioso ocurre cuando aún no disponemos de ese Token. Si ejecutamos nuestro código, utilizaremos parte del módulo google_auth_oauthlib_flow.

La clase InstalledAppFlow dispone de un método “from_clients_secrets_file” lo que hace es tomar como argumento nuestro archivo de credenciales, es decir, el JSON que nos descargamos en el apartado anterior y nos devuelve un objeto Flow.

El objeto Flow dispone de un método [run_local_server](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server), si ejecutamos esto en un sistema con entorno gráfico, se nos abrirá una ventana del navegador en la que tendremos que introducir nuestro correo y nuestra contraseña del dominio asociado a G-Suite for education.

Realmente podríamos utilizar un método alternativo, concretamente [run_console](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console) que muestra una URL al usuario en consola para que lo pegue manualmente en un navegador, se autentique con su cuenta de usuario y contraseña y obtenga un código que tendrá que escribir en la misma consola.

Con cualquiera de las dos alternativas lo que vamos a obtener son las credenciales OAuth2.0 que serializaremos y almacenaremos localmente para garantizar que, a partir de ese momento, no sea necesaria más intervención humana.

El código que les muestro ya incluye la funcionalidad para “refrescar” un token que haya caducado.

![img](https://miro.medium.com/max/30/1*Wp7gTVAjtNfM1iaw33JhbQ.png?q=20)

![img](https://miro.medium.com/max/1148/1*Wp7gTVAjtNfM1iaw33JhbQ.png)

Parte del código del archivo auth.py

Por motivos evidentes, ninguno de los archivos relativos a credenciales está en el repositorio de gitlab, la ruta donde la aplicación buscará estos archivos es configurable.

La función check_auth nos devuelve un objeto service que será el que nos permitirá acceder a los endpoints de las distintas API’s

![img](https://miro.medium.com/max/30/1*HLWgb5rRp9ias9_NjN3e0g.png?q=20)

![img](https://miro.medium.com/max/1624/1*HLWgb5rRp9ias9_NjN3e0g.png)

Fragmento de main.py donde obtenemos un objeto por cada API que utilizamos.

# Los scopes

El último argumento de nuestra función check_auth son los SCOPES para los que estamos solicitando autorización. Básicamente es una manera de segmentar el grado de autorización que tiene nuestra aplicación a la hora de interactuar con cada API. Puedes garantizar acceso de sólo lectura a algunas API’s y permitir que se lleven a cabo borrados y modificaciones en otras.

![img](https://miro.medium.com/max/30/1*UQoPYkTws1CEyxie7M1ZdQ.png?q=20)

![img](https://miro.medium.com/max/1018/1*UQoPYkTws1CEyxie7M1ZdQ.png)

Ámbitos de autorización de Secuaz

Traduciendo un poco estos Scopes podríamos decir que estamos dando permiso para leer, crear, modificar y borrar tanto hojas de cálculo como documentos de nuestro Drive, podemos también hacer todo tipo de operaciones CRUD sobre los usuarios de nuestro dominio y sobre los grupos y sobre los cursos de classroom.

No son pocos permisos, pero para la tarea que tenemos entre manos sí son los mínimos.

# Gestión de la configuración

Otro de los grandes escollos que hemos tenido que sortear en esta herramienta es la gestión de la configuración. Nos lo podríamos haber ahorrado, pero habría hecho que Secuaz no pudiera utilizarse en otros centros educativos y que, el próximo año, hubiera que modificar el código otra vez.

Para evitar esto hemos tenido que recurrir a un módulo que desconocía totalmente pero que, me sugirieron los amigos del grupo [Python Canarias](https://pythoncanarias.es/) (desde aquí muchas gracias por estar siempre ahí)

El módulo se llama [prettyconf](https://pypi.org/project/prettyconf/) y permite leer e interpretar distintos formatos de archivos de configuración.

Como les decía hace un momento, no conocía este módulo y seguro que se puede profundizar mucho más en su utilización, pero para el caso que me ocupaba, lo que hice fue recurrir a ficheros en formato .env

Toda la configuración de la aplicación, de momento, puede resumirse en estos valores:

![img](https://miro.medium.com/max/30/1*30bwjmA6MHgHfRMgg2U3Gg.png?q=20)

![img](https://miro.medium.com/max/1236/1*30bwjmA6MHgHfRMgg2U3Gg.png)

Un ejemplo de archivo de configuración para Secuaz

Creo que los nombres de las variables son bastante autoexplicativos, perdonen el spanglish pero hay una parte de la configuración, que puede ser útil para todos los que trabajen en Canarias, por eso la he dejado así.

Los seis primeros parámetros tienen que ver con los distintos archivos que utilizaremos en Drive, como son hojas de cálculo, incluimos el ID del archivo y el rango de datos en formato A1 sobre el que vamos a trabajar.

Sobre el ID de los archivos de Drive, me gustaría hacer una aclaración, se trata de un valor que es parte de la URL para compartir que nos ofrece la interfaz web de Drive, se las señalo en la siguiente imagen para que vean de dónde sale.

![img](https://miro.medium.com/max/30/1*ZzGNIX3Kg3yUb19rRsmvPw.png?q=20)

![img](https://miro.medium.com/max/1072/1*ZzGNIX3Kg3yUb19rRsmvPw.png)

El ID del fichero es la cadena alfanumérica que aparece tras el “id=” suele ser bastante larga

Básicamente tendrás que copiar el valor del parámetro id de esa URL, ojo que en la imagen aparece cortado, suele ser bastante más largo.

# Importación de profesores

Bueno, entrando en materia, lo que secuaz hace en cada ciclo de generación de cuentas es bastante básico y puede dividirse en dos procesos: El proceso de gestión de profesores y el proceso de gestión de alumnos

Durante el proceso de gestión de profesores no se lleva a cabo ninguna creación de cuentas del dominio, se presupone que todos han sido creados manualmente. Lo primero que hacemos es leer la hoja de cálculo de nuestro Drive y crear un macro-diccionario en memoria. Las claves de este diccionario serán los correos electrónicos de los docentes. Asociaremos a cada correo electrónico el nombre de cada profesor y las asignaturas que imparte, los nombres de sus asignaturas se han normalizado, de manera que este identificador contenga información sobre la etapa, curso y sección.

Una vez disponemos de ese súper diccionario, lo que hacemos es recorrerlo clave a clave, verificando que el usuario forma parte del grupo de profesores de classroom del dominio y si no es así insertándolo. En nuestro classroom, si no eres miembro de este grupo no puedes ser profesor de ningún curso.

Finalmente matriculamos a cada docente en su curso. Esto tiene algún truco, el primer profesor que aparezca relacionado con un curso será el propietario del mismo en classroom y el resto serán profesores adicionales. Esto que parece una chorrada es importantísimo, hasta que el profesor propietario no acepte su curso en la interfaz web de classroom, el resto no podrán verlo.

Por otro lado, nos abre la puerta a configuraciones creativas del equipo docente, por ejemplo, puedo generar un grupo en el que impartan clases varios profesores, ya sea en formato súper-aula o para desarrollar proyectos multidisciplinares.

# Importación de alumnos

La importación de alumnos es un poco más compleja.

Una vez que leemos el contenido de la hoja de cálculo de nuestro drive, lo primero que hacemos es calcular el hash para esta estructura en memoria.

Si en el disco de nuestra máquina existiera un archivo con un hash previo los compararíamos para ver si ha habido algún cambio en todo el bloque de definición de alumnos.

Si los hashes coinciden, no tendremos que realizar ninguna nueva operación. Si por el contrario, el hash almacenado y el que acabamos de calcular fueran distintos, esto nos indicaría que alguno de los registros de la hoja de cálculo han cambiado.

Si ha habido una sincronización previa, en memoria almacenamos la lista del alumnado a la que le hemos calculado un hash por registro, de esta manera podemos saber qué fila del archivo es la que se ha modificado para intervenir sólo en esta.

Para cada nuevo registro o registro modificado continuamos con los siguientes pasos.

En primer lugar intentamos determinar si ya existe una cuenta en nuestro dominio para este estudiante.

Si existe, generamos una nueva contraseña aleatoria, forzamos que deba cambiarla en el próximo inicio de sesión y continuamos con el proceso de matriculación en classroom.

Si no existiera cuenta previamente, se crearía y se forzaría el cambio de contraseña en el primer inicio de sesión.

En cualquiera de los dos procesos anteriores lo que hacemos es matricular a cada alumno en la lista de asignaturas con la que se relaciona.

A parte de eso, se le hará miembro de un grupo del dominio que tendrá el nombre de su grupo de clase. Esto nos facilitará en gran medida la comunicación con grupos completos.

# Generación de autorizaciones y distribución de credenciales

Al terminar cada ciclo de importación, se generan nuevas filas en una hoja de cálculo de drive. La pinta que tiene este archivo de salida es la siguiente.

![img](https://miro.medium.com/max/30/1*B9tz5jK21VXOM0hgiqhh7g.png?q=20)

![img](https://miro.medium.com/max/1452/1*B9tz5jK21VXOM0hgiqhh7g.png)

Archivo de salida en drive con las credenciales temporales de los usuarios

Utilizando el complemento Autocrat es muy sencillo hacer circulares personalizadas para cada alumno con el texto de autorización de las familias.

# Conclusiones

Este curso hemos utilizado por primera vez a nuestro “Secuaz”, en dos años hemos mejorado en casi dos meses el tiempo de configuración de todas nuestras plataformas de elearning y la asignación automática de alumnos y profesores a cursos. Sin embargo, creo que esto sólo ha sido un paso más hacia la herramienta ideal.

Las líneas de trabajo futuras creo que deben ser las siguientes:

- Terminar el código de sincronización para garantizar que sea totalmente desatendida. Aún hay algunas dificultades con los registros modificados.
- Deberíamos poder configurar la asignación de asignaturas optativas, esta parte aún es manual.
- La generación de todas las cuentas para este curso llevó más de ocho horas seguidas, habría que paralelizar los accesos a la API para mejorar estos tiempos.
- Necesitamos un sistema de logs normalizados.
- Una interfaz web agradable permitiría que otras personas sin conocimientos técnicos pudieran hacerse cargo de este proceso.

# Agradecimientos

Si hacemos esto es porque creemos que es útil a nuestros alumnos y a nuestros compañeros y estamos muy orgullosos de poder trabajar con todos ellos.

Es un privilegio trabajar cada día con personas que se toman tan en serio la educación así que: compañeros y compañeras, va por ustedes ;)

[Fuente](https://medium.com/@goyoregalado/gestionar-las-cuentas-de-usuario-de-un-colegio-de-1200-alumnos-con-python-y-la-api-de-google-87cb8a051f25)