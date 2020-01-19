# [Listas por comprensión en Python](https://stackabuse.com/list-comprehensions-in-python/)

Una lista es uno de los tipos de datos fundamentales de Python.  Cada vez que nos encontramos con un nombre de variable seguido de un corchete `[]`, o un constructor de `list`, tenemos una lista capaz de contener múltiples elementos, lo que la convierte en un tipo de datos compuesto.  Del mismo modo, también es muy fácil declarar una nueva lista y luego agregarle uno o más elementos. 

Creemos una nueva lista poblada, por ejemplo: 

```python
 >>> new_list = [1, 2, 3, 4, 5]
 >>> new_list
[1, 2, 3, 4, 5] 
```

O simplemente usemos el método `append()` para agregar cualquier cosa a la lista: 

```python
>>> new_list.append(6)
>>> new_list
[1, 2, 3, 4, 5, 6] 
```

Si se necesita agregar varios elementos a la misma lista, el método `extend()` será útil.  Simplemente necesita pasar la lista de elementos para agregar al método `extend`, como se muestra a continuación: 

```python
>>> new_list.extend([7, 8, 9])
>>> new_list
[1, 2, 3, 4, 5, 6, 7, 8, 9] 
```

Como se puede ver, crear una lista y agregarla con otros elementos es muy sencillo.  Se puede realizar esta tarea sin tener que hacer varias llamadas al método `.append()`.

Del mismo modo, se puede usar un bucle `for` para agregar varios elementos a una lista.  Por ejemplo, tendremos que escribir el siguiente código para crear una lista de cuadrados para los enteros 1-20. 

```python
list_a = []
for i in range(1, 20):
    list_a.append(i**2) 
```

##   ¿Qué es una lista por comprensión de Python? 

En palabras más simples, la **lista por comprensión** es el proceso de crear una nueva lista a partir de otra existente.  O bien, se puede decir que es la forma única de Python de agregar un bucle `for` a una lista.  Pero, ya es bastante simple declarar una lista y agregar lo que desee.  ¿No es así?  Entonces, ¿por qué molestarse en "comprender" nuestras listas?

Las listas por comprensión, de hecho, ofrece muchos beneficios sobre las listas tradicionales.  Para empezar, el código se extiende sobre una sola línea, lo que hace que sea aún más fácil declarar y leer.  También es menos engorroso comprender listas que usar bucles `for` para declarar una nueva.  Finalmente, también es una forma conveniente, más rápida e intuitiva de generar una nueva lista poblada.

Volviendo a los cuadrados de los enteros 1-20, podemos obtener el mismo resultado utilizando el método las listas por comprensión.  Así es como se verá nuestro código ahora: 

```python
 list_b = [i**2 for i in range(1, 20)] 
```

Obsérvese cómo la lógica para generar los elementos de la lista están entre paréntesis.  Cubriremos más el asunto de la sintaxis en la siguiente sección. 

##   Sintaxis para las listas por comprensión

Antes de seguir, es imprescindible explicar la sintaxis de las listas por comprensión.  Aquí está la **sintaxis básica** de las listas por comprensión que contiene una condición:

```python
[<expresión> for <item> in <lista> if <condición>] 
```

Puede parecer ir un poco hacia atrás con la expresión *antes* del bucle, pero así es como se hace.  El orden es así, presumiblemente, porque sería difícil poner la expresión *después* del condicional sin algún tipo de punto y coma, *que Python no tiene*.

Como ya se habrá adivinado, `<expresión>` es en realidad el resultado que obtenemos cuando ejecutamos el resto del código en la lista por comprensión.  El código en sí es solo un ciclo iterativo sobre una colección de datos.  En nuestro ejemplo, estamos usando la expresión, o la salida, para generar la lista de cuadrados.

> Téngase en cuenta que el condicional es opcional, por lo que, como en nuestro ejemplo anterior, no es necesario incluirlo.

También vale la pena mencionar que tenemos una lista que debe ser recorrida  -el elemento o elementos que se iterarán- y, por supuesto, una declaración condicional tanto en la lista por comprensión como en los bucles tradicionales.  Por lo tanto, cada método tiene las mismas construcciones generales, pero la diferencia es cómo se formatean y organizan. 

Veamos otro ejemplo más complejo para comprender mejor el concepto detrás de las listas por comprensión

```python
list_a = [1, 3, 6, 9, 12, 15]
list_b = []
for number in list_a:
    if number % 4 == 0:
        list_b.append(number)

print(list_b) 
```

En realidad, estamos recorriendo `list_a`  en el ejemplo anterior.  Después, añadimos a `list_b` un elemento si su valor es divisible por 4, que se verifica utilizando el operador de módulo (`%`).  En este ejemplo, se vería lo siguiente impreso en la consola: 

```
 [12] 
```

Esto se debe a que 12 es el único número en esa matriz que es divisible por 4. 

Una vez más, podemos usar las listas por comprensióna para reducir el número total de líneas de código que tenemos que escribir para lograr el mismo objetivo.

Como se mencionó anteriormente, el bucle `for` en la declaración anterior está iterando sobre la lista llamada `list_a` .  Luego ejecuta la declaración condicional que verifica si el valor actual es divisible por 4. Finalmente, ejecuta el método `.append()` cuando determina que el valor es realmente divisible por 4. 

Ahora, si desea escribir el código de arriba con la comprelista por comprensiónería así: 

```python
list_a = [1, 3, 6, 9, 12, 15]
list_b = [number for number in list_a if not(number % 4)]
print(list_b)
```

Como se puede ver, hemos reducido el bucle `for`, que abarca más de tres líneas, a solo una línea.  Esa es en realidad la verdadera belleza de las listas por comprensión

## Cuándo usar las comprensiones de listas 

Se puede utilizar las listas por comprensión en aquellos casos en los que se necesita generar una lista a partir de un iterable.  Sin embargo, el mejor momento para usar este método es cuando se necesita agregar o extraer elementos a una lista de manera consistente de acuerdo con un patrón establecido.  Los desarrolladores de Python los usan principalmente para extraer datos de una gran colección de elementos.

Supongamos que se tiene una lista de miles de estudiantes actuales y anteriores con sus nombres, el nombre del padre y sus direcciones.  Los datos de cada uno de los estudiantes se almacenan en un diccionario respectivamente.  Pero, ¿qué pasa si solo se quiere imprimir sus nombres? 

```python
students = [
    {
        "name" : "Jacob Martin",
        "father name" : "Ros Martin",
        "Address" : "123 Hill Street",
    }, {
        "name" : "Angela Stevens",
        "father name" : "Robert Stevens",
        "Address" : "3 Upper Street London",
    }, {
        "name" : "Ricky Smart",
        "father name" : "William Smart",
        "Address" : "Unknown",
    }
] 
```

Tenemos la opción de iterar sobre la lista usando el bucle `for` tradicional: 

```python
names_list = []
for student in students:
    names_list.append(student['name'])

print(names_list) 
```

Aunque en este ejemplo son solo dos líneas de código para el bucle `for`, ni siquiera necesitamos escribir tantas líneas.  Podemos lograr la misma tarea escribiendo solo una línea de código a través del método las listas por comprensión:

```
names_list = [student['name'] for student in students]
print(names_list) 

['Jacob Martin', 'Angela Stevens', 'Ricky Smart']
```

## Conclusión
Es realmente sorprendente cómo las listas por comprensión reducen la carga de trabajo.  Sin embargo, puede parecer confuso al principio.  Es particularmente desconcertante para los principiantes que nunca  antes se han aventurado en este territorio, principalmente debido a la  sintaxis.  También puede resultar difícil comprender el concepto si se ha estado programando en otros lenguajes porque las lista por comprensión no existen en ninguno de ellos.  La única forma de entender las listas por comprensión es practicarlas mucho. 
