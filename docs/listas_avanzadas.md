# Listas: Técnicas avanzadas

Las listas en Python son una de las estructuras de datos más comunes que encontrarás, ¡también son una de las más poderosas! Las listas de Python son increíblemente versátiles y tienen muchos trucos ocultos.

¡Exploremos algunos de estos!

## Filtrado de listas con Python

### Con la función `filter()`

La función `filter()` toma dos parámetros: una función y un elemento iterable. En este caso, definiremos una función y filtraremos una lista.

¡Probemos esto con un ejemplo! Comenzaremos con una lista y filtraremos cualquier elemento que sea inferior a 3:

```python
original_list = [1,2,3,4,5]

def filter_three(number):
  return number > 3

filtered = filter(filter_three, original_list)

filtered_list = list(filtered)

print(filtered_list)
# Returns [4,5]
```

Veamos qué está pasando aquí:

1. Definimos nuestra lista original.
2. Luego definimos una función que acepta un parámetro (`number`). La función devolverá `True` si el número es mayor que tres.
3. Definimos un elemento (`filtered`) que aplica la función de filtro. Nuestro artículo `filtered`, es un objeto de filtro.
4. Finalmente, creamos `filtered_list` que aplica la función de lista al objeto filtrado.

### Con listas por comprensión

Del mismo modo, podemos filtrar una lista con listas por comprensión. Recuerda, las listas por comprensión son formas elegantes de definir y modificar listas.

Veamos cómo podemos lograr nuestra tarea anterior con una lista por comprensión:

```python
original_list = [1,2,3,4,5]
filtered_list = [number for number in original_list if number > 3]
print(filtered_list)
# Return [4,5]
```

Podemos ver en estos dos ejemplos que las listas por comprensión son una forma mucho más fácil y elegante de filtrar listas.

## Modificación de listas

### Con la función `map()`

La función Python Map nos permite aplicar una función a cada elemento en un objeto iterable.

Imagina que tenemos una lista y queremos devolver el cuadrado de cada número. Podemos hacer esto usando la función `map()`. Echemos un vistazo a esto:

```python
original_list = [1,2,3,4,5]

def square(number):
    return number ** 2

squares = map(square, original_list)
squares_list = list(squares)
print(squares)
# Returns [1, 4, 9, 16, 25]
```

Exploremos lo qué está pasando aquí:

- Primero, definimos nuestra lista original y una función que devuelve el cuadrado de su parámetro (`number`).

- Luego, creamos una nueva variable llamada (`squares`)  que es el resultado de la función `map`, con la función `square` y `original_list` como parámetros.

- Finalmente, creamos otra nueva variable que aplica la función de lista a la variable `squares`.

¡Este método es un poco difícil de asumir! ¡Vamos a verlo ahora con listas por comprensión!

### Con listas por comprensión

Podemos hacer la misma tarea de modificar elementos de la lista usando listas por compresión. Es incluso un poco más fácil y una forma más elegante de escribir nuestro código.

¡Probemos esto!

```python
original_list = [1,2,3,4,5]
squares_list = [number ** 2 for number in original_list]
print(squares_list)
# Returns [1,4,9,16,25]
```

# 3. Combinando listas con la función `zip()`

Puede haber casos en los que se desee combinar dos o más listas. ¡Aquí es donde entra la función `zip()`. ! La función `zip()` crea un objeto que contiene los elementos correspondientes de las listas en cada índice.

Probemos esto con un ejemplo:

```python
numbers = [1,2,3]
letters = ['a', 'b', 'c']
combined = zip(numbers, letters)
combined_list = list(combined)
# returns [(1, 'a'), (2, 'b'), (3, 'c')]
```

## Invertir una lista

Las listas de Python son estructuras de datos ordenadas. Debido a esto, el orden de los artículos es importante. A veces puede que necesites invertir los elementos en una lista. Esto se puede hacer fácilmente usando los operadores de *slicing* de Python.

Probemos con un ejemplo:

```python
original_list = [1,2,3,4,5]
reversed_list = original_list[::-1]
print(reversed_list)
# Returns: [5,4,3,2,1]
```

## Comprobación de membresía a una lista

Puede haber ocasiones en que desee ver si un elemento existe en una lista.

Puede hacer esto simplemente usando el operador *in* .

Imagine que tenemos una lista de equipos que han ganado un partido y queremos ver si un equipo en particular ha ganado hasta ahora:

```python
games = ['Yankees', 'Yankees', 'Cubs', 'Blue Jays', 'Giants']

def isin(item, list_name):
    if item in list_name:
        print(f"{item} is in the list!")
    else:
        print(f"{item} is not in the list!")

isin('Blue Jays', games)
isin('Angels', games) 
# Returns
# Blue Jays is in the list!
# Angels is not in the list!
```
## Encontrar el elemento más común en una lista

Es posible que desee encontrar el elemento más común en una lista. Por ejemplo, puede estar registrando a los ganadores de un juego de cara y cruz en una lista y desea saber qué sucedió en más ocasiones.

Prueba con lo siguiente:

```python
games = ['heads', 'heads', 'tails', 'heads', 'tails']
items = set(games)
print(max(items, key=games.count))
```

Echemos un vistazo a lo que estamos haciendo aquí:

1. Definimos una lista con los resultados de cinco jugadas de cara o cruz,
2. Definimos un conjunto con todos los elementos de la lista. La función set () filtra cualquier elemento duplicado en la lista.
3. Finalmente, aplicamos el max () en nuestro conjunto de elementos, utilizando el argumento  `key` como el recuento más alto de los elementos en nuestro conjunto.

## Acoplar una lista de listas

A veces terminarás con una lista que contiene otras listas. ¡Puedes usar listas de comprensión para hacer esto fácilmente!

Probémoslo:

```python
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [i for j in nested_list for i in j]
print(flat_list)
# Returns [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


## Comprobar la unicidad

Si necesita verificar si todos los elementos en una lista son únicos, ¡puede usar el poder de los conjuntos para lograr esto!

Un conjunto en Python es similar a una lista (ya que es modificable ("mutable") y no ordenado), pero solo puede contener elementos únicos.

Para esto, usaremos una función para convertir nuestra lista en un conjunto y comparar las dos longitudes de elementos:

```python
list1 = [1,2,3,4,5]
list2 = [1,1,2,3,4]

def isunique(list):
  if len(list) == len(set(list)):
    print('Unique!')
  else: print('Not Unique!')

isunique(list1)
isunique(list2)

# Returns 
# Unique!
# Not Unique!
```
Fuente: https://towardsdatascience.com/advanced-python-list-techniques-c6195fa699a3