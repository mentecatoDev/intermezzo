# ¿Qué es PEP8 y por qué se debe implementar?

En el mundo del desarrollo es muy común hacer las cosas de distintas formas. Se puede organizar el código como se quiera, incluso escribirlo de forma abstracta. En muchos casos, se logra que nuestra profesión se considere muchas veces como un arte y no como una ingeniería por esta razón. La ausencia de una base sólida de cómo y por qué se hacen las cosas de una manera específica conduce a un software mal redactado y mal organizado que nadie quiere leer. 

La diferencia mas palpable de python con respecto a otros lenguajes es que la comunidad tiene como lema la legibilidad del código. El ZEN de python establece que **"Debe haber una y preferiblemente solo una forma obvia de hacer las cosas"**. Siguiendo este principio, se definió una guía de estilo única descrita íntegramente en el *Python Enhancement Proposal* número 8, abreviado como *PEP* 8, donde se indica como debería ser escrito nuestro código python.

Muchos sabemos que a los desarrolladores de software no les suele gustar la imposición obligatoria de hacer su trabajo de cierta forma. Con el devenir del tiempo hemos apreciado que: el que toda la comunidad use una guía de estilo única finalmente facilita el trabajo y mejora mucho la productividad.

## Puntos destacados de PEP8

### Básicos

- Siempre preferir **espacios** a *tabuladores*.
- Usar **4 espacios** como indentación.
- Las líneas deben ser menores de 80 caracteres de longitud.
- Las líneas que pasen de esta longitud deben dividirse en dos, y la linea resultante de la división debe estar indentada.
- Las funciones y las clases deben estar separadas por dos lineas en blanco.
- No colocar espacios alrededor de los índices de las listas, llamadas a funciones o argumentos.

### Nombres

- Las funciones deben estar declaradas en minúsculas y las palabras separadas por guiones bajos `def funcion_cool()` 
- Los métodos privados de una clase deben comenzar con doble guión bajo `def __private_method()`.
- Los métodos protegidos de una clase deben comenzar con guion bajo `def _protected_method()`.
- Las clases y excepciones deben ser capitalizadas por palabra `class SuperClass`.
- Constantes del module deben estar en mayúsculas separadas por guiones bajos `NUMERO_MAXIMO = 10`.
- Los métodos de instancia de una clase deben usar el parámetro `self` como primer parámetro.
- Los métodos de clase deben usar cls como primer parámetro, para referirse a la misma clase.

### Expresiones

- Usar negación en línea (`if a is not b`) en lugar de negar una expresion positiva `(if not a is b)`.
- No validar valores vacíos usando len `if (len(lista) == 0)`, usar `if not lista`.
- Siempre colocar las `imports` al inicio del archivo.
- Siempre importar funciones y clases usando `from my_module import MyClass` en lugar de importar el módulo completo `import my_module` 
- Si aun se debe usar imports relativos, usar la sintaxis `from . import my_module` 
- Las importaciones siempre deben estar en el orden:
1. Módulos de la librería standar.
2. Módulos externos.
3. Módulos del proyecto.

Y cada sección debe estar en orden alfabético.

Siguiendo estos sencillos puntos, tu equipo de desarrollo y toda la comunidad python estará muy contenta de tenerte. 

Fuentes:

[¿Qué es PEP8 y por qué se debe implementar?](https://dev.to/viktorvillalobos/que-es-el-pep-8-y-porque-deberia-implementarlo-54bh)