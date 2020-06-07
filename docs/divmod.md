# divmod

Una función muy útil. La función `divmod()` realiza una división entera `%` y devuelve el cociente como el resto simultáneamente en una tupla. Por ejemplo:

```py
>>> divmod (5, 2)
(2, 1)
```

En el siguiente ejemplo vemos su uso para evaluar el tiempo en que se ejecuta un proceso dado en horas, minutos y segundos.

```py
start = datetime.datetime.now()
    ...  # process code goes here
end = datetime.datetime.now()

# We get the total runtime in seconds
runtime = (end - start).seconds  # we will assume 30000

# How many hours are in these secs, what are the remaining secs?
hours, remainder = divmod(runtime, 3600)

# Now how many minutes and seconds are in our remainder?
mins, secs = divmod(remainder, 60)
print("{:02d}:{:02d}:{:02d}".format(hours, mins, secs))
```

SALIDA:
```txt
08:16:56
```
Extraído de:

https://towardsdatascience.com/lesser-known-python-features-f87af511887

2020-05-24 22:55:23