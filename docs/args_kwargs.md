# * args, ** kwargs

En ocasiones, se puede observar que una definición de función contiene estos dos argumentos:

```python
def func(x, y, *args, **kwargs)
```

Ambos son en realidad características increíblemente simples. Nos permiten pasar múltiples valores a una función, que luego se empaquetarán en un generador.

Tiene un resultado similar a si pasamos una lista/generador a un argumento estándar, así:

```python
def func(values):
    for x in values:
        print(x, end=" ")

func([1, 2, 3])
```
SALIDA:
```
1 2 3
```

Ahora, usemos `*args`: esto nos permitirá pasar cada valor como un nuevo argumento, en lugar de contenerlos todos dentro de una lista.

```python
def func(*values):
    for x in values:
        print(x, end=" ")

func(1, 2, 3)
```
SALIDA:
```
1 2 3
```

Ten en cuenta que no necesitamos escribir `*args`, sino que escribimos `*values`. El nombre de la variable que usemos es irrelevante. Se define como un `*args` gracias al asterisco único `*`.

`*args` simplemente cree un objeto generador a partir de los argumentos que le pasamos a la función.

`**kwargs`, por otro lado, crea un diccionario. De ahí el nombre, **k**ey**w** ord **arg**ument**s**. Se usa así:

```python
def func(**values):
    for x in values:
        print(f"{x}: {values[x]}")

func(x=1, y=2, z=3)
```
SALIDA:
```
x: 1
y: 2
z: 3
```

Nuevamente, podemos llamar a la variable como queramos, en este caso usamos `**values`. Se define como `**kwargs` mediante el uso de un doble asterisco `**`.


Extraído de:

https://towardsdatascience.com/lesser-known-python-features-f87af511887 

2020-05-24 22:55:23
