# Secretos oscuros sobre asignación de memoria en Python

El módulo `sys` en Python es extremadamente básico e importante. Proporciona principalmente algunas variables utilizadas (o mantenidas) por el intérprete, así como algunas funciones que interactúan fuertemente con el intérprete.

Se  usará frecuentemente el método `getsizeof()` de este módulo, así que presentémoslo brevemente:

- Este método se utiliza para obtener el tamaño de bytes de un objeto
- Sólo calcula la memoria directamente ocupada, y no calcula la memoria de los objetos referenciados en el objeto

Aquí hay un ejemplo intuitivo:

```python
import sys

a = [1, 2]
b = [a, a] # [[1, 2], [1, 2]]

# a, b tienen solamente dos elementos
# así que el tamaño que ocupan es el mismo

sys.getsizeof(a) # resultado: 72
sys.getsizeof(b) # resultado: 72
```

El ejemplo anterior ilustra que en una lista creada estáticamente**,** **si contiene sólo dos elementos, entonces la memoria que ocupa es de 72 bytes, independientemente del objeto al que apunten sus elementos.**

Con esta herramienta de medición, vamos a explorar qué pequeños secretos se esconden en los objetos incorporados de Python.

# 1. ¡Los objetos vacíos no están "vacíos"! 😯

¿Te has preguntado alguna vez sobre la memoria que ocupan algunos de los conocidos objetos vacíos, como cadenas vacías, listas vacías, diccionarios vacíos?

Vayamos directamente al código, y echemos un vistazo al tamaño de los objetos vacíos de varias estructuras básicas de datos:

```python
import sys

sys.getsizeof("")     # 49
sys.getsizeof([])     # 56
sys.getsizeof(())     # 40
sys.getsizeof(set())  # 216
sys.getsizeof(dict()) # 232

sys.getsizeof(1)      # 28
sys.getsizeof(True)   # 28
```

Puede verse que aunque todos son objetos vacíos, estos objetos no están "vacíos" en cuanto a la asignación de memoria, que, por otro lado, es bastante grande (*recuerda estos números, los probaré más adelante*).

> **Puestos en orden: Número básico < Tupla vacía < Cadena vacía < Lista vacía < Conjunto vacío < Diccionario vacío.**

**¿Cómo explicar este pequeño secreto?**

Debido a que estos objetos vacíos son contenedores, podemos entenderlo de forma abstracta: Parte de su memoria se utiliza para crear el esqueleto del contenedor, registrar la información del contenedor (como el recuento de referencia, información de uso, etc.), y parte de la memoria ya está preasignada.

# 2. ¡ La expansión de la memoria no es uniforme!

**Los objetos vacíos no están vacíos**, en parte porque el intérprete de Python les asignó previamente un espacio inicial.

Sin exceder la memoria inicial, cada vez que se añade un nuevo elemento se utiliza la memoria existente, evitando así solicitar más memoria.

Así pues, si se asigna la memoria inicialmente, ¿cómo se asigna una nueva memoria?

```python
import sys
letter = "abcdefghijklmnopqrstuvwxyz"

a = []
for i in letters:
	a.append(i)
	print(f'{len(a)}, sys.getsizeof(a) = {sys.getsizeof(a)}')

b = set()
for j in letters:
    b.add(j)
    print(f'{len(b)}, sys.getsizeof(b) = {sys.getsizeof(b)}')

c = dict()
for k in letters:
    c[k] = k
    print(f'{len(c)}, sys.getsizeof(c) = {sys.getsizeof(c)}')
```

Añade 26 elementos a los tres tipos de objetos variable, y este es el resultado:
```
1, sys.getsizeof(a) = 88 
2, sys.getsizeof(a) = 88 
3, sys.getsizeof(a) = 88 
4, sys.getsizeof(a) = 88 
5, sys.getsizeof(a) = 120 
6, sys.getsizeof(a) = 120 
7, sys.getsizeof(a) = 120 
8, sys.getsizeof(a) = 120 
9, sys.getsizeof(a) = 184 
10, sys.getsizeof(a) = 184 
11, sys.getsizeof(a) = 184 
12, sys.getsizeof(a) = 184 
13, sys.getsizeof(a) = 184 
14, sys.getsizeof(a) = 184 
15, sys.getsizeof(a) = 184 
16, sys.getsizeof(a) = 184 
17, sys.getsizeof(a) = 256 
18, sys.getsizeof(a) = 256 
19, sys.getsizeof(a) = 256 
20, sys.getsizeof(a) = 256 
21, sys.getsizeof(a) = 256 
22, sys.getsizeof(a) = 256 
23, sys.getsizeof(a) = 256 
24, sys.getsizeof(a) = 256 
25, sys.getsizeof(a) = 256 
26, sys.getsizeof(a) = 336 
1, sys.getsizeof(b) = 216 
2, sys.getsizeof(b) = 216 
3, sys.getsizeof(b) = 216 
4, sys.getsizeof(b) = 216 
5, sys.getsizeof(b) = 728 
6, sys.getsizeof(b) = 728 
7, sys.getsizeof(b) = 728 
8, sys.getsizeof(b) = 728 
9, sys.getsizeof(b) = 728 
10, sys.getsizeof(b) = 728 
11, sys.getsizeof(b) = 728 
12, sys.getsizeof(b) = 728 
13, sys.getsizeof(b) = 728 
14, sys.getsizeof(b) = 728 
15, sys.getsizeof(b) = 728 
16, sys.getsizeof(b) = 728 
17, sys.getsizeof(b) = 728 
18, sys.getsizeof(b) = 728 
19, sys.getsizeof(b) = 2264 
20, sys.getsizeof(b) = 2264 
21, sys.getsizeof(b) = 2264 
22, sys.getsizeof(b) = 2264 
23, sys.getsizeof(b) = 2264 
24, sys.getsizeof(b) = 2264 
25, sys.getsizeof(b) = 2264 
26, sys.getsizeof(b) = 2264 
1, sys.getsizeof(c) = 232 
2, sys.getsizeof(c) = 232 
3, sys.getsizeof(c) = 232 
4, sys.getsizeof(c) = 232 
5, sys.getsizeof(c) = 232 
6, sys.getsizeof(c) = 360 
7, sys.getsizeof(c) = 360 
8, sys.getsizeof(c) = 360 
9, sys.getsizeof(c) = 360 
10, sys.getsizeof(c) = 360 
11, sys.getsizeof(c) = 640 
12, sys.getsizeof(c) = 640 
13, sys.getsizeof(c) = 640 
14, sys.getsizeof(c) = 640 
15, sys.getsizeof(c) = 640 
16, sys.getsizeof(c) = 640 
17, sys.getsizeof(c) = 640 
18, sys.getsizeof(c) = 640 
19, sys.getsizeof(c) = 640 
20, sys.getsizeof(c) = 640 
21, sys.getsizeof(c) = 640 
22, sys.getsizeof(c) = 1176 
23, sys.getsizeof(c) = 1176 
24, sys.getsizeof(c) = 1176 
25, sys.getsizeof(c) = 1176 
26, sys.getsizeof(c) = 1176
```
De aquí podemos ver el secreto de las variables cuando se expanden:

## Mecanismo de sobre-asignación

Cuando se solicita nueva memoria, **no se asigna a petición sino que se asigna más**, por lo que cuando se añade un pequeño número de elementos, no es necesario solicitar más memoria inmediatamente.

> Consejo: Elegir la estructura de datos correcta es importante en el contexto de Python. 

## Mecanismo de asignación no uniforme:

La frecuencia de solicitud de nueva memoria para los tres tipos de objetos es diferente, y la memoria sobreasignada del mismo tipo de objetos cada vez no es uniforme, sino que se expande gradualmente.

# 3. ! Eliminar elementos no libera memoria ! 

Como se mencionó anteriormente, al expandir objetos variables, se puede solicitar nueva memoria.

Por lo tanto, si se reducen los objetos variables y se eliminan los elementos, ¿se recuperará automáticamente la memoria recién aplicada?

```python
import sys

a = [1, 2, 3, 4]
sys.getsizeof(a)  # Initial value: 88

a.append(5)       # After expansion: [1, 2, 3, 4, 5]
sys.getsizeof(a)  # After expansion : 120

a.pop()           # After reduction: [1, 2, 3, 4]
sys.getsizeof(a)  # After reduction : 120
```

Como se muestra en el código, después de que la lista se expande y se contrae, aunque vuelve a su estado original, el espacio de memoria ocupado por la lista no se libera automáticamente. Lo mismo ocurre con otros objetos variables.

Este es el pequeño secreto de Python, "*El principio de que las personas con exceso de peso no pueden perderlo; es fácil que las personas delgadas ganen peso, y es fácil reducir su talla de nuevo también, pero en ningún caso perderán peso*".

# 4. !! El comportamiento excepcional de los diccionarios !!

El método `pop()` sólo reduce los elementos del objeto mutable, pero no libera el espacio de memoria utilizado.

También hay un método `clear()`, que borra todos los elementos del objeto mutable, probémoslo:

```python
import sys

a = [1, 2, 3]
b = {1, 2, 3}
c = {'a':1, 'b':2, 'c':3}

sys.getsizeof(a) # 80
sys.getsizeof(b) # 216
sys.getsizeof(c) # 232

a.clear()        # After emptying: []
b.clear()        # After emptying: set()
c.clear()        # After emptying: {}

```



Llamando al método `clear()`, obtenemos varios objetos vacíos.

En la primera sección, se ha comprobado su tamaño de memoria.

Sin embargo, si se revisa de nuevo, sorprenderá el encontrar que el tamaño de estos objetos vacíos no es el mismo que el de la revisión anterior!

```python
sys.getsizeof(a) # 56
sys.getsizeof(b) # 216
sys.getsizeof(c) # 64
```

El tamaño de la lista vacía y la tupla vacía casi no cambian, pero ¡el diccionario vacío (64) es mucho más pequeño que el anterior diccionario vacío (232)!

Es decir, después de limpiar los elementos, la lista y la tupla vuelven al punto de partida y permanecen sin cambios.
