# Expresiones de asignación

## Introducción

![morsa](https://python-course.eu/images/python-tutorial/walrus.webp)

La versión 3.8 de Python vino con una nueva característica, que algunos programadores de Python anhelaban desde hace bastante tiempo. Se ha introducido una nueva forma de asignar objetos a variables, es decir, el operador `:=`. Brinda a los programadores una forma conveniente de asignar variables en medio de expresiones. Si miras a los caracteres con un poco de imaginación puedes ver una similitud con los ojos y colmillos de una morsa, por eso cariñosamente se le conoce como **el operador morsa** (**the walrus operator**) .

Las expresiones de asignación han sido discutidas en [PEP 572](https://translate.google.com/website?sl=auto&tl=es&hl=es&u=https://peps.python.org/pep-0572/) y esto es lo que se escribió sobre el *naming*:

```tex
During discussion of this PEP, the operator became informally known as "the walrus operator". The construct's formal name is "Assignment Expressions" (as per the PEP title), but they may also be referred to as "Named Expressions" (e.g. the CPython reference implementation uses that name internally).

Durante la discusión de este PEP, el operador se conoció informalmente como "el operador morsa". El nombre formal de la construcción es "Expresiones de Asignación" (según el título del PEP), pero también pueden ser referidas como "Expresiones con Nombre" (por ejemplo, la implementación de referencia de CPython utiliza ese nombre internamente).
```

Una asignación simple también se puede reemplazar por una expresión de asignación, aunque parece torpe y, definitivamente, no es el caso de uso más adecuado:

```python
x = 5 
# se puede escribir como: 
( x := 5 )  # ¡válido, pero no recomendado! 
# los paréntesis son cruciales
```

### SALIDA:

```tex
5
```

Veamos un pequeño ejemplo de código que solo usa asignaciones *tradicionales :*

```python
txt = '¡Python necesita entrenamiento!' 
ideal_length = 22

n = len(txt) 
if n == ideal_length: 
    print(f'¡La longitud {n} es ideal!') 
else:
    print(f'¡La longitud {n} no es ideal!')
```

### SALIDA:

```tex
¡La longitud 25 no es ideal!
```

Usaremos el nuevo *operador morsa* en el siguiente fragmento de código de Python:

```python
txt = '¡Python necesita entrenamiento!' 
ideal_length = 22

if (n := len(txt)) == ideal_length:
  print(f'¡La longitud {n} es ideal!') 
else:
  print(f'¡La longitud {n} no es ideal!')
```

### SALIDA:
```tex
¡La longitud 25 no es ideal!
```

De acuerdo, puede decir que esto no es muy impresionante y que la primera versión podría considerarse aún más legible. Entonces, echemos un vistazo a un caso de uso más útil.

## Aplicaciones beneficiosas de las expresiones de asignación

### Listas por comprensión

A continuación, verás una lista por comprensión con un *operador morsa*:

```python
def f(x):
    return x + 4

numbers = [3, 7, 2, 9, 12]
odd_numbers = [result for x in numbers if (result := f(x)) % 2]
print(odd_numbers)
```

### SALIDA:

```tex
[7, 11, 13]
```

La implementación anterior es más eficiente que una lista por comprensión sin la expresión de asignación, porque tendremos que llamar a la función dos veces:

```python
def f(x):
    return x + 4

numbers = [3, 7, 2, 9, 12]
odd_numbers = [f(x) for x in numbers if  f(x) % 2]
print(odd_numbers)
```

### SALIDA:

```tex
[7, 11, 13]
```

### Expresiones regulares

También hay una gran ventaja cuando usamos expresiones regulares:

```python
import re

txt = """The Python training course started at 2022-02-4 
the other one at 2022-01-24
only one date per line, if at all
the dates may also be in this format 2020/10/15
or 20-10-04"""
for line in txt.split('\n'):
    if (date := re.search(r'(\d{2,4})[-/](\d{2})[-/](\d{2})', line)):
        year, month, day = date.groups()
        print(year, month, day)
```
SALIDA:
```tex
2022 01 24
2020 10 15
20 10 04
```

### Lectura de archivos de longitud fija
```python
with open('training_course_info.txt') as fh:
    while ((data := fh.read(52)) != ''):
        print(data.rstrip())
```
SALIDA:
```tex
Curso de formación de Python para principiantes Berlín    08
Curso intermedio de Python                      Hamburgo  06
Curso de formación avanzada de Python           Frankfurt 08
```

### Uso en bucles while

En el capítulo sobre [bucles while](https://python--course-eu.translate.goog/python-tutorial/loops.php?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es) de nuestro Tutorial de Python, tuvimos un pequeño juego de adivinanzas:

```python
import random

lower_bound, upper_bound = 1, 20
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("Nuevo número: "))
    if guess > to_be_guessed:
        print("El número es muy grande")
    elif guess < to_be_guessed:
        print("El número es muy pequeño")
else:
    print("Felicidades. ¡Lo adivinaste!")
```

Como puedes ver, tuvimos que inicializar `guess` a cero para poder ingresar al bucle. Podemos hacer la inicialización directamente en la condición de bucle con una expresión de asignación y simplificar todo el código con esto:

```python
import random

lower_bound, upper_bound = 1, 20
to_be_guessed = random.randint(lower_bound, upper_bound)
while (guess := int(input("Nuevo número: "))) != to_be_guessed:
    if guess > to_be_guessed:
        print("El número es muy grande")
    elif guess < to_be_guessed:
        print("El número es muy pequeño")
else:
    print("Felicidades. ¡Lo adivinaste!")
```

### SALIDA:

```tex
El número es muy pequeño
El número es muy grande
El número es muy pequeño
Felicidades. ¡Lo adivinaste!
```

## Llevado al extremo:

Dijimos al comienzo de esta página que algunos programadores de Python anhelaron esta construcción durante bastante tiempo. Una de las razones por las que no se introdujo antes fue el hecho de que también se puede usar para escribir código que es menos legible si se usa mucho. El siguiente fragmento de código muestra un ejemplo extremo que **no se recomienda usar**:

```python
a , b , c = 1 , 2 , 3 
x = 4 
y = ( c := ( a := x * 2.3 ) + ( b := x * 4.5 - 3 )) 
```
```python
print(y)
```
24.2

```python
print(c)
```
24.2

```python
print(a)
```
9.2

```python
print(b)
```

15.0

#### Fuentes

https://python-course.eu/python-tutorial/assignment-expressions.php
