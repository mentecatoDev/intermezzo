 

### Sentencia Switch

Aunque los lenguajes populares como Java y PHP tienen una declaración **switch** ya incorporada, puede que sorprenda saber que Python no tiene uno. Como tal, se puede estar tentado a utilizar una serie de  bloques **if-else-if**, usando una condición **if** para cada alternativa.

Sin embargo, debido a la tabla de salto, una instrucción **switch** es mucho más rápido que una escalera **if-else-if**. En lugar de evaluar cada condición en forma secuencial, solo tiene que  buscar la variable/expresión una vez y saltar directamente a la rama  apropiada de código para ejecutarla.

### ¿Como se implementa la sentencia switch en Python?

La forma de Python de implementar la instrucción **switch** es utilizar las asignaciones de diccionarios, también conocidas como  matrices asociativas, que proporcionan asignaciones simples de  clave-valor de uno a uno.

Aquí esta la implementación de Python de la declaración anterior. En el siguiente ejemplo, creamos un diccionario llamado **switcher** para almacenar todos los casos del tipo **switch**.
```
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print switcher.get(argument, "Invalid month")
```
En el ejemplo, al pasar un argumento en la función **switch_demo**, se busca el valor en el diccionario. Si se encuentra una coincidencia,  se imprime el valor asociado, de lo contrario se imprime una cadena  predeterminada («Invalid Month»). La cadena predeterminada ayuda a  implementar la opción «default» de la sentencia switch.

### Asignación de diccionario para funciones

Aquí es donde se vuelve más interesante. Los valores de un diccionario de  Python pueden ser de cualquier tipo de datos. De modo que no tiene que  limitarse a utilizar constantes (enteros, cadenas), también puede  utilizar nombres de funciones y lambdas como valores.

Por ejemplo, también puede implementar la instrucción **switch** anterior creando un diccionario de nombres de funciones como valores. En este caso, **switcher** es un diccionario de nombres de funciones y no de cadenas.
```
def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
 
def five():
    return "May"
 
def six():
    return "June"
 
def seven():
    return "July"
 
def eight():
    return "August"
 
def nine():
    return "September"
 
def ten():
    return "October"
 
def eleven():
    return "November"
 
def twelve():
    return "December"
 
 
def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print func()
```
Aunque las funciones anteriores son bastantes simples y solo devuelven  cadenas, puede usar este enfoque para ejecutar bloques elaborados de  código dentro de cada función.

De hecho, si llama métodos a  objetos, incluso puede usar un método de envío para determinar  dinámicamente a que función se debe llamar durante el tiempo de  ejecución.
```
class Switcher(object):
    def numbers_to_months(self, argument):
        """Dispatch method"""
        method_name = 'month_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()
 
    def month_1(self):
        return "January"
 
    def month_2(self):
        return "February"
 
    def month_3(self):
        return "March"
 
...
```
Basado en el argumento, la función getattr() recuperará métodos de objetos con el nombre en particular.
```
Input: a=Switcher()
Input: a.numbers_to_months(1)
Output: January
```

### Ventajas de la implementación switch de Python
Dado que puede alterar los diccionarios de Python en tiempo de ejecución  (agregar, eliminar o actualizar pares clave-valor), puede cambiar  fácilmente la declaración de conmutación en tiempo de ejecución. Aquí un ejemplo.
```
def zero():
    return "zero"
 
def one():
    return "one"
 
def two():
    return "two"
 
switcher = {
        0: zero,
        1: one,
        2: two
    }
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
 
Input: numbers_to_strings(1)
Output: One
 
Input: switcher[1]=two #changing the switch case
Input: numbers_to_strings(1)
Output: Two
```
La sentencia switch es muy útil, que no sólo proporciona un mejor  rendimiento que una instrucción if-else, sino que también te deja un  código más manejable. Si has tenido límites por la falta de la sentencia swith en Python, entonces con suerte, este artículo te ayudará a  implementarlo.

https://www.clubdetecnologia.net/blog/2017/python-como-se-implementa-una-sentencia-switch-case/