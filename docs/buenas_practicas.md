1. **README.md**: Una documentación a nivel de proyecto ayuda a tener una estructura limpia, esto ayuda a todo el equipo en el futuro. Escribir esto en el archivo README.md, es un buen  punto para empezar, luego se puede expandir en la carpeta **docs/** de ser necesario. Incluya el propósito del proyecto, que hay en cada carpeta, de donde provienen los datos, que archivos son críticos y cómo se ejecutan los test.

2. Utiliza [**Docker**](https://www.docker.com/get-started):  utilizar Docker te permitirá simplificar el despliegue de la aplicación en otras máquinas o realizar el despliegue en algún entorno cloud.

3. **Test**: Agrega el archivo **test/** y agrega pruebas unitarias. Una de las librerías que se recomiendan utilizar es [**pytest**](https://docs.pytest.org/en/latest/), un moderno entorno para ejecutar las pruebas. Empezar con un par de test y luego continuar mejorándolos. Utiliza el coverage para  determinar que porcentaje de tu código está cubierto por pruebas.

4. Test de integración: Si tienes código heredado y careces de pruebas, una actividad de alto valor es agregar algunas «pruebas de integración» que verifiquen el flujo general del proyecto y verifiquen que con ciertos datos de entrada se obtienen resultados de salida específicos.

5. [**Docstrings**](https://www.datacamp.com/community/tutorials/docstrings-python): Agrega documentación en el código para las funciones, clases y módulos, esto es de gran ayuda. Agrega información de qué se espera de la función y un pequeño ejemplo de lo que se espera como salida. Puedes revisar el docstrings de numpy como inspiración.

6. **Refactoring**: Si el código se convierte en muy largo, como una función extensa que ocupe más de una pantalla, siéntete cómodo de hacer un refactoring del código y hacerlo más pequeño o reducirlo en funciones más pequeñas. Código más corto es más fácil para hacer pruebas y para darle mantenimiento.

7. [**Git**](https://git-scm.com/book/es/v1/Empezando-Acerca-del-control-de-versiones): Utiliza una herramienta para el control de versiones, esto te ayudará en momentos que sobreescribas algo crítico. Acostúmbrate a realizar  commits frecuentemente y realiza un push hacia el repositorio diariamente.

8. [PEP8](https://www.python.org/dev/peps/pep-0008/): Mantén el estandard de codificación PEP8. Aún mejor, adopta [Black](https://pypi.org/project/black/) como un enlace de control del código previo, para que simplemente reescribas el código estándar por tí mismo. Utiliza **[flake8](http://flake8.pycqa.org/en/latest/)** para limpiar tu código y evitar otros errores.

9. **PipEnv**: Crear entornos aislados del sistema operativo te facilitará la vida.  Algunos recomendados son Anaconda, otro puede ser pipenv con Docker, ambas son soluciones adecuadas.

10. **Legibilidad**:  Finalmente recuerda que la legibilidad es más importante que ser inteligente. Los fragmentos cortos de código complejo y dificíles de leer  serán difíciles de mantener para tí y tus colegas, por lo que el equipo tendrá miedo de tocar ese código. En su lugar, es preferible escibir una función más larga y más fácil de leer y que esté respaldada con documentación útil que muestre lo que devolverá y complementa esto con pruebas unitarias.

>>> "La depuración es el doble de difícil que escribir código en primera instanacia. Por lo tanto, si escribes código de la manera más inteligente posible, por definición, no serás lo suficientemente inteligente como para depurarlo."

>>> Brian Kernighan

https://www.clubdetecnologia.net/blog/2019/buenas-practicas-en-python/

# Creí que dominaba python hasta que descubrí estos trucos


## Evitar condiciones inútiles

A menudo, una larga condición  "if" y "elif"... y "else" es el signo de un código que necesita ser refactorizado, estas condiciones hacen que tu código sea largo y muy difícil de interpretar. A veces pueden ser fácilmente reemplazadas, por ejemplo, mira este código:

```python
def f():
    if condition:
    	return True
    else:
    	return False
```
¡Esto es una tontería! La función está devolviendo un valor lógico, así que ¿por qué usar bloques `if`? Lo correcto sería hacer esto:

```python
def f():
	return condition
```

En un desafío de [Hackerrank](https://www.hackerrank.com/dashboard), se te da el año y tienes que escribir una función para comprobar si el año es bisiesto o no. En el calendario gregoriano hay que tener en cuenta tres criterios para identificar los años bisiestos:

- Si el año puede ser dividido entre 4, ES un año bisiesto, a menos que:

- el año pueda ser dividido entre 100, en cuyo caso NO ES un año bisiesto, a menos que:

- el año también se pueda dividir entre 400 en cuyo caso ES un año bisiesto.

En este desafío, olvídate de los `if` y `else` y haz lo siguiente:

```
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
```

## Uso adecuado de los espacios en blanco

- Nunca mezcles tabuladores y espacios

- Una línea entre funciones

- Dos líneas entre clases

- Añade un espacio después de "," en los diccionarios, listas, tuplas, argumentos en una lista de argumentos y después de ":" en los diccionarios.

- Poner espacios alrededor de las asignaciones y comparaciones (excepto para los argumentos en una lista)

- No hay espacios para abrir/cerrar paréntesis o justo antes de una lista de argumentos.

```
def function(key, value=0):
    """Return a dictionary and a list..."""
    d = {key: value}
    l = [key, value]
    return d, l
```

## Docstings y comentarios

- Docstrings = Cómo usar el código

- Comentarios = Por qué (racionalizar) y cómo funciona el código

Las docstrings explican cómo usar el código:

- Explican el propósito de una función aunque te parezca obvio, porque no necesariamente le parecerá obvio a otra persona más adelante.

- Describen los parámetros esperados, los valores devueltos y las excepciones planteadas.

- Si el método está fuertemente acoplado a un solo llamador, menciona la función de llamada.

Los comentarios explican lo que son para los mantenedores del código. Ejemplos incluyendo notas para usted mismo, como:

> \# !!! BUG: …
>
> \# !!! FIX: This is a hack
>
> \# ??? Why is this here?

Es tu responsabilidad escribir buenas docstrings y comentarios, así que mantenlos siempre actualizados. Cuando hagas cambios, asegúrate de que los comentarios y las cadenas de documentos sean consistentes con el código.

Encontrarás un PEP detallado dedicado a las Doctsrings: [**“Docstring Conventions”**](https://www.python.org/dev/peps/pep-0257/)

## Variables y la asignación

En otros lenguajes de programación:

```python
c = a
a = b
b = c
```

En Python, es mejor usar la asignación en un código de una línea:

b, a = a, b

Puede que ya lo hayas visto pero, ¿sabes cómo funciona?

La coma es la sintaxis para construir una tupla.

Una tupla se crea a la derecha y otra es el objetivo de la izquierda. 

Otros ejemplos:

```python
>>> user =['Jan', 'Gomez', '+1-888-222-1546']
>>> name, title, phone = user
>>> name
'Jan'
>>> title
'Gomez'
>>> phone
'+1-888-222-1546'
```

Útil en bucles sobre datos estructurados (la variable `user` del código anterior se mantiene):

```python
>>> people = [user, ['German', 'GBT', 'unlisted']]
>>> for (name, title, phone) in people:
...      print (name, phone)
...
Jan +1-888-222-1546
German unlisted
```

También es posible hacer lo opuesto, sólo asegúrate de tener la misma estructura a la derecha y a la izquierda:

```python
>>> jan, (gname, gtitle, gphone) = people
>>> gname
'German'
>>> gtitle
'GBT'
>>> gphone
'unlisted'
>>> jan
['Jan', 'Gomez', '+1-888-222-1546']
```

# Concatenación de listas y unión (join)

Empecemos con una lista de cadenas:

```python
colors = ['red', 'blue', 'green', 'yellow']
```

Queremos concatenar estas cadenas para crear una larga. Particularmente cuando el número de cadenas es grande, evita hacer esto:


```python
result = ''
for s in colors:
    result += s
```

Es muy lento. Utiliza muchos recursos. La concatenación se hará, almacenará y luego pasará al siguiente paso intermedio.

En lugar de eso, haz esto:

```python
result = ''.join(colors)
```

El método `join()` hace toda la copia en una sola pasada. Cuando sólo procesas unas pocas cadenas, no hay diferencia. Pero acostúmbrate a construir tus cadenas de forma óptima, porque con cientos o miles de cadenas, realmente habrá diferencia.

Aquí hay algunas técnicas para usar el método de unión (). Si quieres un espacio como separador:

```python
result = ' '.join(colors)
```

o una coma y un espacio:

```python
result = ', '.join(colors)
```

Para hacer una frase gramaticalmente correcta, queremos comas entre cada valor excepto el último, donde preferimos una "o". La sintaxis para dividir una lista hace el resto. El [: -1] devuelve todo excepto el último valor, que podemos concatenar con nuestras comas.

```python
colors = ['rojo', 'azul', 'verde', 'amarillo']
print ('Elige', ', '.join(colors[:-1]), \
      'o', colors[-1])

SALIDA: Elige rojo, azul, verde o amarillo
```

## Testar condiciones verdaderas 

Es elegante y rápido aprovechar Python con respecto a los valores lógicos:

```python
# Do this :     # And not this :
if x:             if x == True:
   pass                  pass

# Do this :     # And not this :
if items:         if len(items) != 0:
    pass                pass

# and especially not that :
        if items != []:
               pass
```

Usa `enumerate` cuando sea posible

La función de `enumerate` toma una lista y devuelve pares (índice, item):

```
items = ['cero', 'uno', 'dos', 'tres']
>>> print list(enumerate(items))
[(0, 'cero'), (1, 'uno'), (2, 'dos'), (3, 'tres')]
```

Es necesario utilizar una lista para mostrar los resultados porque `enumerate` es una función perezosa, que genera un elemento (un par) a la vez, sólo cuando se solicita. Una bucle `for` requiere tal mecanismo. La impresión no toma un resultado a la vez, sino que debe estar en posesión de todo el mensaje que se va a mostrar. Por lo tanto, convertimos automáticamente el generador en una lista antes de utilizar la impresión.

Por lo tanto, usar el bucle de abajo es mucho mejor:

```python
for (index, item) in enumerate(items):
    print (index, item)

# compared to :              # And :
index = 0                     for i in range(len(items)):
for item in items:                    print (i, items[i])
    print (index, item)
    index += 1
```

La versión con `enumerate` es más corta y simple que las otras dos versiones. Un ejemplo que muestra que la función enumerar devuelve un iterador (un generador es una especie de iterador)

## Listas por comprensión

La forma tradicional con `for` e `if`:

```python
new_list = []
for item in a_list:
    if condition(item):
        new_list.append(fn(item))
```

Usando una lista por comprensión:

```python
new_list = [fn(item) for item in a_list if condition(item)]
```

Las listas por comprensión son claras y directas. Puedes tener varios bucles `for` y condicionales `if` dentro de la misma lista por comprensión, pero para más de dos o tres, o si las condiciones son complejas, te sugiero que uses el habitual bucle `for`.

Por ejemplo, la lista de cuadrados de 0 a 9:

```python
>>> [n ** 2 for n in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

La lista de números impares dentro de la lista anterior:

```python
>>> [n ** 2 for n in range(10) if n % 2]
[1, 9, 25, 49, 81]
```

Otro ejemplo:

```python
[(x, y) for x in (1, 2, 3, 4) if x % 2 == 0 for y in ['a', 'b'] if y == 'b']
[(2, 'b'), (4, 'b')]
```

## Expresiones generadoras

Sumemos los cuadrados de los números menores de 100:

```python
# With a loop :
total = 0
for num in range(1, 101):
    total += num * num
```

También podemos usar la función de suma que hace el trabajo más rápido para nosotros construyendo la secuencia correcta.

```python
# With a list comprehension :
total = sum([num * num for num in range(1, 101)])# With a generator expression :
total = sum(num * num for num in xrange(1, 101))
```

Las expresiones generadoras son como listas por comprensión, excepto que en su cálculo, son perezosas. Las listas por comprensión calculan todo el resultado en una sola pasada, para almacenarlo en una lista. Las expresiones generadoras calculan un valor cada vez, cuando es necesario. Esto es particularmente útil cuando la secuencia es muy larga y la lista generada es sólo un paso intermedio y no el resultado final.

Por ejemplo, si tenemos que sumar los cuadrados de varios miles de millones de enteros, llegaremos a una saturación de la memoria con una lista por comprensión, pero las expresiones generadoras no tendrán ningún problema. Sin embargo, ¡tardará un tiempo!

```python
total = sum(num * num for num in range(1, 1000000000))
```
La diferencia en la sintaxis es que las lista por comprensión tienen corchetes, mientras que las expresiones generadoras no. Las expresiones generadoras a veces requieren paréntesis, por lo que siempre se deben usar.

En resumen:

- Usar una **lista por comprensión** cuando el resultado esperado sea la lista.
- Usar una **expresión generadora** cuando la lista es sólo un resultado intermedio.

# Conclusión

Se han presentado algunos de los mejores consejos para aprender a programar en Python. Si realmente quieres convertirte en un programador o añadir una habilidad de codificación a tu preparación, aprender Python es un gran lugar para empezar. Busca una buena guía de enseñanza de Python en línea y empieza a averiguar cómo programar en Python. Te recomiendo que aprendas lo básico con un curso interactivo antes de pasar a conceptos más difíciles.

No deberías acelerar demasiado el proceso de aprendizaje, o podrías perder información importante. Toma notas y asegúrate de revisarlas regularmente y trata de practicar la escritura del código tan a menudo como sea posible.

Conéctate con colegas que estén aprendiendo como tú y no tengas miedo de hacer preguntas cuando las tengas. Ayudar a los demás cuando tienen problemas puede ser un gran repaso, y trabajar con el código de otra persona es una gran manera de aprender cosas nuevas.

Si haces todo esto, ¡nada puede detenerte! Entonces, ¿qué estás esperando? ¡Empieza a programar en Python ahora!

https://towardsdatascience.com/i-thought-i-was-mastering-python-until-i-discovered-these-tricks-e40d9c71f4e2

