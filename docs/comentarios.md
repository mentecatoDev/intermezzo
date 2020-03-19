 

En Python la única forma de crear comentarios es usando el símbolo `#` (numeral). **No hay otra**. <u>_La proposición según la cual las triples comillas operan también como comentarios es falsa_</u>.

```python
# Esto es un comentario.
a = 1

"""¡¡¡Error!!! Esto no es un comentario."""
b = 2
```

La confusión radica en que las triples comillas suelen emplearse para crear la documentación de una función. Por ejemplo:

```python
def add(a, b):
    """
    Retorna el resultado de a + b.
    """
    return a + b
```

Luego, esa documentación, conocida también como *docstring*, se almacena en el atributo `add.__doc__` y es accedida por la función `help()`.

```python
print(add.__doc__)
help(add)
```

No obstante, la realidad es que, en una función, la primera cadena literal que se encuentra es interpretada por Python como *la documentación*, sin importar si se usan triples comillas o un par de comillas dobles o simples.

```python
# Ambas documentaciones son válidas.
def add(a, b):
    "Retorna el resultado de a + b."
    return a + b

def div(a, b):
    'Retorna el resultado de a / b.'
    return a / b
```

Esto funciona porque en Python es válido crear expresiones cuyo resultado no es utlilizado para nada (por ejemplo, para asignarlo a una variable o pasarlo como argumento a una función). El siguiente código no arroja ningún error:

```python
7 + 5
"Hola mundo"
"""Esto es una cadena."""
15 / 3
```

Ahora bien, eso es exactamente lo que se está haciendo cuando se crea un «comentario» usando triples comillas: generar una cadena que luego es desechada por Python por no emplearse.

Pero el problema se origina cuando esas cadenas, creyendo ser  comentarios, son ubicadas en lugares donde se espera una expresión. Por  ejemplo:

```python
languages = [
    """Lenguaje y año en que fue creado"""
    ("Python", 1991),
    ("Java", 1996),
    ("C++", 1983),
    ("Elixir", 2011)
]
```

Esto arroja el siguiente error:

```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
     ("Python", 1991),
TypeError: 'str' object is not callable
```

El error indica que estamos intentando llamar a una cadena como si fuese una función. En efecto, no hay ninguna diferencia con esto:

```python
"Lenguaje y año en que fue creado"("Python", 1991)
```

Quienes se están iniciando en el lenguaje quedan atónitos por un error tan extraño. Y todo eso es por pensar que las cadenas funcionan como comentarios. La forma correcta, por tanto, es esta:

```python
languages = [
# Lenguaje y año en que fue creado
    ("Python", 1991),
    ("Java", 1996),
    ("C++", 1983),
    ("Elixir", 2011)
]
```