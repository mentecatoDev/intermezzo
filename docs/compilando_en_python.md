# Compilando en Python

### Componentes internos de Python

Lo más probable es que haya leído en alguna parte que el lenguaje Python es un lenguaje de programación interpretado o script. La verdad es que Python es tanto un lenguaje interpretado como compilado. Pero llamar a Python un lenguaje compilado sería engañoso. La gente asumiría que el compilador traduce el código de Python a  lenguaje de máquina. El código de Python se traduce en código intermedio, que debe ser ejecutado por una máquina virtual,  conocida como PVM (python Virtual Machine), la Máquina Virtual de Python. Este es un enfoque similar al adoptado por Java. Incluso hay una forma de traducir los programas de Python en código de bytes de Java para la máquina virtual de Java (JVM). Esto se puede lograr con *Jython*.

La pregunta es, ¿tengo que compilar mis scripts de Python para hacerlos más rápidos o cómo puedo compilarlos? La respuesta es fácil: normalmente, no necesitas hacer nada y no debes molestarte, porque "Python" ya está pensando por tí, es decir, toma  los pasos necesarios automáticamente.

¿Deseas compilar un programa de python manualmente por alguna razón? No hay problema. Se puede hacer con el módulo `py_compile`, ya sea usando el shell del intérprete

```python
import py_compile 
py_compile.compile('mi_primer_programa_simple.py')
```

#### SALIDA:

```text
'__pycache__/mi_primer_programa_simple.cpython-37.pyc'
```

o usando el siguiente comando en el indicador de shell

```bash
python -m py_compile mi_primer_programa_simple.py
```

De cualquier manera, puedes notar dos cosas: primero, habrá un nuevo subdirectorio " `__pycache__`", si aún no existe. Encontrará un archivo "mi_primer_programa_simple.cpython-37.pyc" en este subdirectorio. Esta es la versión compilada de nuestro archivo en código de bytes.

También puede compilar automáticamente todos los archivos de Python usando el módulo `compileall`. Puede hacerlo desde el indicador de shell ejecutando `compileall.py` y  proporcionando la ruta del directorio que contiene los archivos de Python para compilar:

```
monty@python:~/python$ python -m compileall .
Listing . ...
```

Pero como hemos dicho, no tienes que preocuparte ni debes preocuparte por compilar el código de Python. La compilación está oculta para el usuario por una buena razón. Algunos novatos se preguntan a veces de dónde podrían provenir estos siniestros archivos con el sufijo .pyc. Si Python tiene acceso de escritura para el directorio donde reside el  programa de Python, almacenará el código de bytes compilado en un archivo que termina con el sufijo `.pyc`. Si Python no tiene acceso de escritura, el programa funcionará de todos modos. El código de bytes se generará pero se descartará cuando finalice el programa. Cada vez que se llama a un programa de Python, Python verificará si existe una versión compilada con el sufijo .pyc. Este archivo debe ser más reciente que el archivo con el sufijo .py. Si existe dicho archivo, Python cargará el código de bytes, lo que acelerará el tiempo de inicio del script. Si no hay una versión de código de bytes, Python creará el código de bytes antes de que comience la ejecución del programa. La ejecución de un programa de Python significa la ejecución del código de bytes en Python.

![Código fuente a código de bytes](https://python-course.eu/images/python-tutorial/py_pyc_overview_500w.webp)

## Máquina virtual (PVM).

### Compilación de un script Python

Cada vez que se ejecuta un script de Python, se crea un código de bytes. Si se importa un script de Python como módulo, el código de bytes se almacenará en el archivo `.pyc` correspondiente. Por lo tanto, lo siguiente no creará un archivo de código de bytes:

```bash
monty@python:~/python$ python mi_primer_programa_simple.py
¡Mi primer script simple en Python!
monty@python:~/python$
```

La importación en la siguiente sesión de Python2  creará un archivo de código de bytes con el nombre  "my_first_simple_program.pyc":

```bash
monty@python:~/tmp$ ls 
mi_primer_programa_simple.py
monty@python:~/tmp$ python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import mi_primer_programa_simple
¡Mi primer script simple en Python!
>>> exit()
monty@python:~/tmp$ ls
mi_primer_programa_simple.py  mi_primer_programa_simple.pyc
monty@python:~/tmp$
```

## Scripts ejecutables bajo Linux

Hasta ahora, hemos comenzado nuestros scripts de Python con

```
python3 mi_fichero.py
```

en la línea de comandos de bash. Una  secuencia de comandos de Python también se puede iniciar como cualquier  otra secuencia de comandos en Linux, por ejemplo, las secuencias de  comandos de Bash. Se necesitan dos pasos para este  propósito: la línea *shebang* `#!/usr/bin/env python` debe agregarse como  la primera línea de su archivo de código Python. Alternativamente, esta línea puede ser `#!/usr/bin/python`, si esta es la ubicación de su intérprete de Python. En lugar de usar `env` como en la primera línea shebang, el intérprete se busca y se ubica en el momento en que se ejecuta el script. Esto hace que el script sea más portable. Sin embargo, también sufre el mismo problema: la ruta a `env` también puede ser diferente según la máquina.

El archivo debe hacerse ejecutable: el comando `chmod +x scriptname` debe ejecutarse en un shell de Linux, por ejemplo, bash. `chmod 755 scriptname` también se puede usar para hacer que su archivo sea ejecutable. En nuestro ejemplo:

```
    $ chmod +x mi_primer_programa_simple.py
```

Ilustramos esto en una sesión bash:

```bash
bernd@marvin:~$ more mi_primer_programa_simple.py 
#!/usr/bin/env python
print("¡Mi primer script simple en Python!")
bernd@marvin:~$ ls -ltr mi_primer_programa_simple.py 
-rw-r--r-- 1 mentecato mentecato 63 Nov  4 21:17 mi_primer_programa_simple.py
bernd@marvin:~$ chmod +x mi_primer_programa_simple.py 
bernd@marvin:~$ ls -ltr mi_primer_programa_simple.py 
-rwxr-xr-x 1 mentecato mentecato 63 Nov  4 21:17 my_first_simple_script.py
bernd@marvin:~$ ./mi_primer_programa_simple.py 
¡Mi primer script simple en Python!
```