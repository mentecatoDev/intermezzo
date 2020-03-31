# Parámetros por referencia

Si solías (o sueles) utilizar otro lenguaje de programación, de seguro en algún momento te has preguntado por los parámetros por referencia.

En otros lenguajes de programación existe el paso de parámetros por valor y por referencia. En los pasos por valor, una función no puede modificar el valor de las variables que recibe por fuera de su ejecución: un intento por hacerlo simplemente altera las copias locales de dichas variables. Por el contrario, al pasar por referencia, una función obtiene acceso directo a las variables originales, permitiendo así su edición. Ejemplos de este último comportamiento en Visual Basic y C, respectivamente:

```visualbasic

Private Sub CambiarCantidad(ByRef cantidad As Integer)
    cantidad = 5
End Sub

Dim cantidad As Integer
cantidad = 1
Call CambiarCantidad(cantidad)
print cantidad  ' Imprime 5
```

```c
void CambiarCantidad(int *cantidad)
{
    *cantidad = 5;
}

int cantidad = 1;
CambiarCantidad(&cantidad);
printf("%d", cantidad);  /* Imprime 5 */
```

En ambos casos (aunque en Visual Basic no pueda observarse, ya que la máquina virtual se encarga de esto) se trata de pasar un puntero en referencia a la variable que se desea editar.

En Python, en cambio, no se concibe la dialéctica paso por valor/referencia, porque el lenguaje no trabaja con el concepto de variables sino objetos y referencias. Al realizar la asignación `a = 1` no se dice que «`a` contiene el valor 1″ sino que «`a` referencia a 1″. Así, en comparación con otros lenguajes, podría decirse que en Python los parámetros siempre se pasan por referencia.

Ahora bien podríamos preguntar, ¿por qué el siguiente código no modifica los valores originales?

```python
def f(a, b, c):
# No altera los objetos originales.
    a, b, c = 4, 5, 6

a, b, c = 1, 2, 3
f(a, b, c)
print(a, b, c)   # Imprime 1, 2, 3
```

La respuesta es que los números enteros (como también los de coma flotante, las cadenas y otros objetos) son inmutables. Es decir, una vez creados, su valor no puede ser modificado. ¿Cómo, no puedo acaso hacer `a = 1` y luego `a = 2`?. Claro, pero desde la perspectiva del lenguaje, no estás cambiando el valor de `a` de 1 a 2 sino quitando la referencia a 1 y poniéndosela a 2. En términos más simples, no «cambias» el valor de un objeto sino que le asignas una nueva referencia.

En el código anterior, al ejecutar `a, b, c = 4, 5, 6` estás creando nuevas referencias para los números 4, 5 y 6 dentro de la función `f` con los nombres `a`, `b` y `c`.

Sin embargo otros objetos, como las listas o diccionarios, son mutables. Veamos un ejemplo:

```python
def f(a):
    a[0] = "CPython"
    a[1] = "PyPy"
    a.append("Stackless")

items = ["Perro", "Gato"]
f(items)
print(items) # Imprime ['CPython', 'PyPy', 'Stackless']
```

Entonces ahora nos entendemos: basta con saber si un objeto es mutable o inmutable para determinar si es posible editarlo dentro de una función y que tenga efecto fuera de ésta. Es correcto, pero aquí hay una mejor noticia: ¡no hay necesidad alguna para que lo hagas! Te diré por qué: el paso por referencia es la manera en que los lenguajes que trabajan con variables proveen al programador para retornar más de un valor en una misma función. En cambio, Python permite devolver varios objetos utilizando [tuplas o listas](http://recursospython.com/guias-y-manuales/listas-y-tuplas/). Por ejemplo:

```python
a = 1
b = 2
c = 3

def f():
    return 4, 5, 6

a, b, c = f()
# Ahora "a" es 4, "b" es 5 y "c" es 6.
```

En Python no es una buena práctica modificar los objetos pasados como parámetros desde una función y puede llevar a resultados inesperados. No hay razón para hacerlo, basta con retornar múltiples objetos.

Otro método de obtener el mismo resultado (cambiar el valor de un objeto y mantener los cambios fuera de la función) es utilizando variables globales, poco recomendado (yo diría que no recomendado) e inseguro.

```python
a, b, c = 1, 2, 3

# Cambio el nombre de los argumentos para evitar errores de nombramiento.
def f(d, e, f):
    global a, b, c
    a, b, c = 4, 5, 6
 
f(a, b, c)
```

Para funciones de C que requieran pasar parámetros por referencia (un puntero), pueden utilizarse las funciones `ctypes.byref` y `ctypes.pointer` que, en estos casos, resultan similares, con la diferencia que la primera se ejecuta más rápidamente. Ambas toman como parámetro un objeto que represente un tipo de C (por ejemplo, `c_bool`, `c_char`, etc.).

```python
from ctypes import byref, c_int, pointer

a = c_int(50)
a_ref = byref(a)
a_ptr = pointer(b)
```

¡Espero que el artículo te haya resultado esclarecedor y ahora puedas hacer uso de las buenas prácticas del lenguaje!

Fuente: https://recursospython.com/guias-y-manuales/parametros-por-referencia/