# Doctest

Si por un lado las **docstrings** permiten describir documentación, los **doctest** permiten combinar las pruebas con la propia documentación.

Este concepto ayuda a mantener las pruebas actualizadas, y además sirve como ejemplo de uso del código, ayudando a explicar su propósito.

Para utilizar **doctests** hay que escribir una línea dentro de la documentación como la siguiente:

```
>>>
```

Python entenderá que debe ejecutar el contenido dentro del comentario como si fuera código normal, y lo hará **hasta que encuentre  una línea en blanco** (o llegue al final de la documentación).

Lo mejor es ver  a **doctest** en acción.

## Definiendo pruebas

Por regla general cada prueba va ligada a una funcionalidad, pueden  ser funciones, clases o sus métodos. Por ejemplo, dada una función **suma**...

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos"""
    return a+b
```

Para realizar una prueba dentro de la función, vamos a ejecutar un código que la invoque:

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    >>> suma(5,10)
    """
    return a+b
```

Bien, ya tenemos la prueba, pero ahora nos falta indicar a **doctest** cuál es el resultado correcto, y eso lo indicaremos en la siguiente línea:

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    >>> suma(5,10)
    15
    """
    return a+b
```

Ahora se ha de ejecutar la prueba para ver si funciona o no, pero antes hay que adaptar el código.

## Pruebas en un módulo

Para ejecutar pruebas se usará la terminal, así que se guarda la función en un script **test.py** como si fuera un *módulo con funciones*.

Ahora, justo al final, se indicará que se ejecuten las pruebas doctest de las funciones del módulo escribiendo el siguiente código:

```python
import doctest
doctest.testmod()  # Notar que mod significa módulo
```

Esto sería suficiente, pero con el objetivo de evitar que este código se ejecute al ser importado desde otro lugar, se suele hacer de la siguiente otra forma:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Con esto se lanzarán las pruebas **únicamente al ejecutar directamente el módulo**, y ya podremos ejecutar el módulo desde la terminal:

```bash
$ python test.py
```

Como resultado no se muestra nada, lo cual no significa que no se haya ejecutado la prueba, sino que ésta ha funcionado correctamente y no hay fallos.

Se puede mostrar todo el registro de ejecución pasando un argumento `-v` a python justo al final:

```bash
$ python test.py -v
```

Y entonces se verá el siguiente resultado:

```
Trying:
    suma(5,10)
Expecting:
    15
ok
1 items had no tests:
    __main__
1 items passed all tests:
1 tests in __main__.suma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

...en el que se prueba el código `suma(5,10)`, se espera `15` y el resultado es ok; un resumen y finalmente `Test passed`.

## Creando varias pruebas

Evidentemente se puede definir múltiples pruebas e incluso alguna que se sepa que no es correcta:

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    >>> suma(5,10)
    15

    >>> suma(0,0)
    1

    >>> suma(-5,7)
    2
    """
    return a+b
```

Ahora, si se ejecuta el script de forma normal...

```bash
python test.py
```

A diferencia de antes sí que muestra algo; indicando que uno de los tests ha fallado:

```bash
**********************************************************************
File "test.py", line 7, in __main__.suma
Failed example:
    suma(0,0)
Expected:
    1
Got:
    0
**********************************************************************
1 items had failures:
1 of   3 in __main__.suma
***Test Failed*** 1 failures.
```

La cuestión ahora es revisar si el test es incorrecto, o adaptar  la función para que devuelva el resultado esperado en el test.  Evidentemente en este caso el test era incorrecto a propósito  así que simplemente habrá que borrarlo.

## Pruebas que nos guían

Una de las ventajas de usar tests es que pueden utilizarse para detectar posibles fallas. En el siguiente ejemplo se usa como guía los tests para implementar correctamente una función.

```python
def palindromo(palabra):
    """
    Comprueba si una palabra es un palíndromo. Los palíndromos son 
    palabras o frases que se leen igual en ambos sentidos.
    Si es un palíndromo devuelve True y si no False

    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("holah")
    False
    """
    if palabra == palabra[::-1]: 
        return True
    else:
        return False
```

Bien, ¿pero qué ocurre si se hace el siguiente test?

```python
>>> palindromo("Ana")
True
```

Evidentemente, fallará:

```
**********************************************************************
File "test.py", line 11, in __main__.palindromo
Failed example:
    palindromo("Ana")
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
1 of   3 in __main__.palindromo
***Test Failed*** 1 failures.
```

Claro, es que `Ana` empieza por mayúscula, pero hay que recordar que un palíndromo lo es si se pronuncia igual, por tanto las mayúsculas no deberían afectar. Por tanto, en este caso habría que readaptar el código para prevenir el error:

```python
def palindromo(palabra):
    """
    Comprueba si una palabra es un palíndrimo. Los palíndromos son 
    palabras o frases que se leen igual en ambos sentidos.
    Si es un palíndromo devuelve True y si no False

    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("holah")
    False

    >>> palindromo("Ana")
    True
    """
    if palabra.lower() == palabra[::-1].lower(): 
        return True
    else:
        return False
```

Y en el test de la frase... ¿"Atar a la rata"? Esto también es un palíndromo:

```
>>> palindromo("Atar a la rata")
True
**********************************************************************
Failed example:
    palindromo("Atar a la rata")
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
1 of   4 in __main__.palindromo
***Test Failed*** 1 failures.
```

¡Falla de nuevo! Ahora el problema son los espacios, ya que estos no se leen pero, si existen en la cadena, la frase no concuerda.

```python
def palindromo(palabra):
    """
    Comprueba si una palabra es un palíndromo. Los palíndromos son 
    palabras o frases que se leen igual en ambos sentidos.
    Si es un palíndromo devuelve True y si no False

    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("holah")
    False

    >>> palindromo("Atar a la rata")
    True
    """
    palabra = palabra.lower().replace(" ", "")
    if palabra == palabra[::-1]: 
        return True
    else:
        return False
```

Todavía habría algunos casos como los acentos que darían fallos,  pero ya se ve por donde va la lógica. Se trata de que, gracias a los test, se cree la función correctamente.

De hecho en el mundo de la programación hay una práctica conocida como TDD, **Test Driven Development** o **Desarrollo guiado por pruebas** que trata de escribir las pruebas primero y luego refactorizar para ir puliendo la funcionalidad.

## Tests avanzados

Hasta ahora se han hecho unos tests muy simples, pero los **doctests** son muy flexibles. Algunas de sus funcionalidades interesantes son la posibilidad de **ejecutar bloques de código** o la **captura de excepciones**.

Para crear un test que incluya un bloque de código, se debe utilizar las sentencias anidadas para simular tabulaciones:

```python
...
def doblar(lista):
    """Dobla el valor de los elementos de una lista
    >>> l = [1, 2, 3, 4, 5] 
    >>> doblar(l)
    [2, 4, 6, 8, 10]
    """
    return [n*2 for n in lista]
```

En este caso se ha creado la lista del test manualmente, pero se podría haber generado con un bucle utilizando sentencias anidadas:

```python
def doblar(lista):
    """Dobla el valor de los elementos de una lista
    >>> l = [1, 2, 3, 4, 5] 
    >>> doblar(l)
    [2, 4, 6, 8, 10]

    >>> l = [] 
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [n*2 for n in lista]
```

Si se ejecuta el script monitorizando todo:

```bash
$ python test.py -v
```

...se puede observar la ejecución del test avanzado:

```text
Trying:
    l = [1, 2, 3, 4, 5]
Expecting nothing
ok
Trying:
    doblar(l)
Expecting:
    [2, 4, 6, 8, 10]
ok
Trying:
    l = []
Expecting nothing
ok
Trying:
    for i in range(10):
        l.append(i)
Expecting nothing
ok
Trying:
    doblar(l)
Expecting:
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
ok
1 items had no tests:
    __main__
1 items passed all tests:
5 tests in __main__.doblar
5 tests in 2 items.
5 passed and 0 failed.
Test passed.
```

Por último vamos a volver a nuestra función suma para tratar excepciones dentro de los tests.

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    Pueden ser números:

    >>> suma(5,10)
    15

    >>> suma(-5,7)
    2

    Cadenas de texto:

    >>> suma('aa','bb')
    'aabb'

    O listas:

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]
    """
    return a + b
```

Se sabe que no se pueden sumar valores de tipos distintos, ¿cómo puede tenerse esto en cuenta en un test?

Pues por ahora se supondrá un resultado y se comprobará que este falla:

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    Pueden ser números:

    >>> suma(5,10)
    15

    >>> suma(-5,7)
    2

    Cadenas de texto:

    >>> suma('aa','bb')
    'aabb'

    O listas:

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sin embargo no podemos sumar elementos de tipos diferentes:

    >>> suma(10,"hola")
    "10hola"
    """
    return a+b
```

Si se ejecuta el script monitorizando todo:

```bash
$ python test.py -v
```

Se puede observar el fallo:

```text
Trying:
    suma(5,10)
Expecting:
    15
ok
Trying:
    suma(-5,7)
Expecting:
    2
ok
Trying:
    suma('aa','bb')
Expecting:
    'aabb'
ok
Trying:
    a = [1, 2, 3]
Expecting nothing
ok
Trying:
    b = [4, 5, 6]
Expecting nothing
ok
Trying:
    suma(a,b)
Expecting:
    [1, 2, 3, 4, 5, 6]
ok
Trying:
    suma(10,"hola")
Expecting:
    "10hola"
**********************************************************************
File "test.py", line 26, in __main__.suma
Failed example:
    suma(10,"hola")
Exception raised:
    Traceback (most recent call last):
    File "C:\Program Files\Anaconda3\lib\doctest.py", line 1321, in __run
        compileflags, 1), test.globs)
    File "<doctest __main__.suma[6]>", line 1, in <module>
        suma(10,"hola")
    File "test.py", line 29, in suma
        return a+b
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
1 of   7 in __main__.suma
7 tests in 2 items.
6 passed and 1 failed.
***Test Failed*** 1 failures.
```

Concretamente habrá que fijarse en la primera línea y la última de la excepción:

```text
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Y precisamente esto es lo que se indicará en el test:

```python
def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos
Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    Pueden ser números:

    >>> suma(5,10)
    15

    >>> suma(-5,7)
    2

    Cadenas de texto:

    >>> suma('aa','bb')
    'aabb'

    O listas:

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sin embargo no se pueden sumar elementos de tipos diferentes:

    >>> suma(10,"hola")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a+b
```