# La tortuga que dibuja

En 1967 *Wally Feurzeig* y *Seymour Papert* crearon **Logo**, un lenguaje de programación con fines educativos. Ese lenguaje incluía los "gráficos de tortuga". La "tortuga" de Logo es un cursor al que se le pueden dar órdenes de movimiento (avance, retroceso o giro) y que puede ir dejando un rastro sobre la pantalla. Moviendo adecuadamente la tortuga se pueden conseguir dibujar todo tipo de figuras.

Python incluye un módulo llamado `turtle` que permite crear éste tipo de **gráficos tortuga**.

## El primer programa con tortugas

Se van a trazar un par de líneas en la terminal de Python para crear una nueva tortuga y empezar a dibujar un rectángulo. (La variable que refiere a la primera tortuga se llamará `alex`).

```python
import turtle

# Set the window size to 800x600 pixels
turtle.setup(800, 600)

# Set the Screen object as wn
wn = turtle.Screen()

# Creates the turtle
leonardo = turtle.Turtle()
leonardo.forward(300)
leonardo.left(90)
leonardo.forward(200)

wn.exitonclick()
```

Tras la de la segunda instrucción, se abrirá una nueva ventana. El tercer comando coloca un cursor – llamando cariñosamente a una `tortuga` del módulo – a la que se le ha puesto el nombre de `alex`. Las siguientes tres líneas mueven a `alex` hacia adelante, gira hacia la izquierda, y lo mueve hacia adelante una vez más, completando dos lados de un rectángulo. Después de introducir estos comandos, aparecerá una ventana que se parece a esto:

![_images/alex.png](./img_la_tortuga_que_dibuja/alex.png)

Aquí hay un par de cosas que se necesita entender acerca de este programa.

- La primera línea le dice a Python que cargue un módulo llamado `turtle`. Dicho módulo nos trae dos nuevos tipos que podemos utilizar: el tipo de `Turtle`, y el tipo de `Screen`. La notación de puntos `turtle.Turtle` significa *“El tipo de tortuga que se define en el módulo de Tortuga”* (Python distingue entre mayúsculas y minúsculas, así que el nombre del módulo, con una `t` minúscula, es diferente al que la tiene mayúscula).
- A continuación, se crea y abre lo que llamamos una screen, que se asigna a la variable `sc`. Cada `screen` contiene un **lienzo (canvas)**, que es el área dentro de ella en el que podemos dibujar. En la siguiente línea se crea una tortuga. La variable `leonardo` se usa para referirse a ella. Estas tres primeras líneas es la preparación para ahora hacer algunas cosas útiles.
- A continuación instruimos al **objeto** `leonardo` para que se mueva, y que gire. Hacemos esto mediante la **invocación** a los **métodos** de `leonardo` —estos son instrucciones a las que todas las tortugas saben cómo responder.
- La última línea también desempeña un papel: la variable `wn` se refiere a la ventana activa. Cuando se invoca el método `exitonclick`, detiene la ejecución del programa, y espera a que el usuario haga clic con el ratón en algún lugar de la ventana. Cuando este evento click se produce, la respuesta es cerrar la ventana de la tortuga y la salida (la ejecución de la parada) del programa de Python.

Un objeto puede tener varios métodos —las cosas que puede hacer— y también pueden tener **atributos** (también llamados *propiedades*). Por ejemplo, cada tortuga (`turtle`) tiene un atributo `color`. El modo de invocarlo es `leonardo.color("red")` que hará alex rojo, y el dibujo será de color rojo también. El color de la tortuga (`turtle`), la anchura de la pluma, la posición de la tortuga dentro de la ventana, la apariencia, etc. son partes de su **estado** actual. Del mismo modo, el objeto `screen` tiene un color de fondo y un texto en la barra de título, y un tamaño y posición en la pantalla. Todos ellos forman parte del estado del objeto `screen`. Hay un buen número de métodos que nos permiten modificar tortugas y screens. Vamos a mostrar un par:

```python
import turtle

# establecer el tamaño de la ventana de 800 por 600 píxeles
turtle.setup(800, 600)

wn = turtle.Screen()        # establecer wn al objeto de la ventana
wn.bgcolor("lightgreen")    # establecer el color de fondo de la ventana
wn.title("Hola, Tess!")     # establecer el título de la ventana
tess = turtle.Turtle()
tess.color("blue")          # hacer tess azul
tess.pensize(3)              # establecer el ancho de la pluma  
tess.forward(300)
tess.left(120)
tess.forward(300)
wn.exitonclick()
```
La ejecución de este programa creará una ventana gráfica que se verá así:
![_images/tess.png](./img_la_tortuga_que_dibuja/tess.png)
Cuando ejecutamos este programa aparece esta nueva ventana y permanecerá en la pantalla hasta que se haga clic en ella.
Extender este programa 

> Nota:
>
> Se puede encontrar una lista de nombres de colores permitidos en http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm. Incluye algunos bastante inusuales, como `peach puff` (bocanada de melocotón) y `HotPink` (rosa caliente)

## Una manada de tortugas

Al igual que podemos tener muchos enteros diferentes en un programa, podemos tener muchas tortugas. Cada una de ellas es una **instancia**. Cada instancia tiene sus propios atributos y métodos -por lo que Alex puede dibujar con un lápiz negro delgado y estar en alguna posición, mientras que Tess podría ir en su propia dirección con un bolígrafo de color rosa grueso (`fat pink`). Aquí está lo que sucede cuando `alex` termina su rectángulo, y `tess` completa su triángulo:

```python
import turtle
# setup the window and its attributes
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

# instantiate (create) tess and set her attributes
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

# instantiate alex
alex = turtle.Turtle()

# draw an equilateral triangle with tess
tess.forward(320)
tess.left(120)
tess.forward(320)
tess.left(120)
tess.forward(320)
tess.left(120)

# turn tess around and move her away from the origin
tess.right(180)
tess.forward(320)

# make alex draw a square
alex.forward(200)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)
wn.exitonclick()
```

que genera esto cuando se ejecuta:

![_images/tess_y_alex.png](./img_la_tortuga_que_dibuja/tess_y_alex.png)

## Algunos trucos y métodos de tortugas

Los métodos de la tortuga pueden utilizar ángulos y distancias negativas. Así `tess.forward(-100)` moverá a tess hacia atrás y `tess.left(-30)` la gira a la derecha.

Además, dado que hay 360 grados en un círculo, al girar 30 a la izquierda se estará en la misma situación que si se gira 330 a la derecha! (La animación en la pantalla será diferente).También hay un método `backward` (si se es muy nerd, uno puede disfrutar de mover a `alex` hacia adelante mediante `alex.backward(-100)`).

El lápiz de la tortuga se puede levantar (`penup`) o apoyar (`pendown`).  Esto nos permite mover una tortuga a un lugar diferente sin dibujar una línea. Los métodos son 

```python
alex.penup()
alex.forward(100)   # esto hace que se mueva alex sin dibujar una línea alex.pendown ()
```

Cada tortuga puede tener su propia forma. Los que están disponibles  son la `arrow` (flecha), `blank` (espacio en blanco), `circle` (círculo), `classic` (clásico), `square` (cuadrado), `triangle` (triángulo), `turtle` (tortuga).

```python
alex.shape("turtle")
```
Se puede acelerar o ralentizar la velocidad de la animación de la tortuga. El ajuste de velocidad varía entre 1 (lento) a 10 (más rápido). Sin embargo, si se establece la velocidad a 0 se desactivará la animación y se irá lo más rápido posible.

```python
alex.speed(10)
```

Una tortuga puede crear un “sello” (`stamp`) de su huella en el lienzo que seguirá así después de que la tortuga se haya movido a otra parte. Se sella, aun cuando la pluma está arriba.

El siguiente ejemplo muestra algunas de estas nuevas características:

```python
import turtle
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess's Spiral")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                    # this is new
size = 20
for i in range(30):
    tess.stamp()                # leave an impression on the canvas
    size = size + 3             # increase the size on every iteration
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.exitonclick()
```
que genera esto cuando se ejecuta:

![_images/espiral.png](./img_la_tortuga_que_dibuja/espiral.png)

## Vista general de los métodos para Turtle y Screen 

### Turtle

#### Movimiento de Turtle 

##### Mover y dibujar
[`forward()`](https://docs.python.org/3/library/turtle.html#turtle.forward) | [`fd()`](https://docs.python.org/3/library/turtle.html#turtle.fd)
[`backward()`](https://docs.python.org/3/library/turtle.html#turtle.backward) | [`bk()`](https://docs.python.org/3/library/turtle.html#turtle.bk) | [`back()`](https://docs.python.org/3/library/turtle.html#turtle.back)
[`right()`](https://docs.python.org/3/library/turtle.html#turtle.right) | [`rt()`](https://docs.python.org/3/library/turtle.html#turtle.rt)
[`left()`](https://docs.python.org/3/library/turtle.html#turtle.left) | [`lt()`](https://docs.python.org/3/library/turtle.html#turtle.lt)
[`goto()`](https://docs.python.org/3/library/turtle.html#turtle.goto) | [`setpos()`](https://docs.python.org/3/library/turtle.html#turtle.setpos) | [`setposition()`](https://docs.python.org/3/library/turtle.html#turtle.setposition)
[`setx()`](https://docs.python.org/3/library/turtle.html#turtle.setx)
[`sety()`](https://docs.python.org/3/library/turtle.html#turtle.sety)
[`setheading()`](https://docs.python.org/3/library/turtle.html#turtle.setheading) | [`seth()`](https://docs.python.org/3/library/turtle.html#turtle.seth)
[`home()`](https://docs.python.org/3/library/turtle.html#turtle.home)
[`circle()`](https://docs.python.org/3/library/turtle.html#turtle.circle)
[`dot()`](https://docs.python.org/3/library/turtle.html#turtle.dot)
[`stamp()`](https://docs.python.org/3/library/turtle.html#turtle.stamp)
[`clearstamp()`](https://docs.python.org/3/library/turtle.html#turtle.clearstamp)
[`clearstamps()`](https://docs.python.org/3/library/turtle.html#turtle.clearstamps)
[`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo)
[`speed()`](https://docs.python.org/3/library/turtle.html#turtle.speed)

##### Mostrar el estado de Turtle

[`position()`](https://docs.python.org/3/library/turtle.html#turtle.position) | [`pos()`](https://docs.python.org/3/library/turtle.html#turtle.pos)
[`towards()`](https://docs.python.org/3/library/turtle.html#turtle.towards)
[`xcor()`](https://docs.python.org/3/library/turtle.html#turtle.xcor)
[`ycor()`](https://docs.python.org/3/library/turtle.html#turtle.ycor)
[`heading()`](https://docs.python.org/3/library/turtle.html#turtle.heading)
[`distance()`](https://docs.python.org/3/library/turtle.html#turtle.distance)

##### Medidas
[`degrees()`](https://docs.python.org/3/library/turtle.html#turtle.degrees)
[`radians()`](https://docs.python.org/3/library/turtle.html#turtle.radians)

#### Control del lápiz

##### Estado del lápiz
[`pendown()`](https://docs.python.org/3/library/turtle.html#turtle.pendown) | [`pd()`](https://docs.python.org/3/library/turtle.html#turtle.pd) | [`down()`](https://docs.python.org/3/library/turtle.html#turtle.down)
[`penup()`](https://docs.python.org/3/library/turtle.html#turtle.penup) | [`pu()`](https://docs.python.org/3/library/turtle.html#turtle.pu) | [`up()`](https://docs.python.org/3/library/turtle.html#turtle.up)
[`pensize()`](https://docs.python.org/3/library/turtle.html#turtle.pensize) | [`width()`](https://docs.python.org/3/library/turtle.html#turtle.width)
[`pen()`](https://docs.python.org/3/library/turtle.html#turtle.pen)
[`isdown()`](https://docs.python.org/3/library/turtle.html#turtle.isdown)

##### Control del color
[`color()`](https://docs.python.org/3/library/turtle.html#turtle.color)
[`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor)[`fillcolor()`](https://docs.python.org/3/library/turtle.html#turtle.fillcolor)

##### Relleno
[`filling()`](https://docs.python.org/3/library/turtle.html#turtle.filling)
[`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill)[`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill)

##### Más controles de dibujo
[`reset()`](https://docs.python.org/3/library/turtle.html#turtle.reset)
[`clear()`](https://docs.python.org/3/library/turtle.html#turtle.clear)
[`write()`](https://docs.python.org/3/library/turtle.html#turtle.write)

#### Estado de Turtle

##### Visibilidad
[`showturtle()`](https://docs.python.org/3/library/turtle.html#turtle.showturtle) | [`st()`](https://docs.python.org/3/library/turtle.html#turtle.st)
[`hideturtle()`](https://docs.python.org/3/library/turtle.html#turtle.hideturtle) | [`ht()`](https://docs.python.org/3/library/turtle.html#turtle.ht)
[`isvisible()`](https://docs.python.org/3/library/turtle.html#turtle.isvisible)

##### Apariencia
[`shape()`](https://docs.python.org/3/library/turtle.html#turtle.shape)
[`resizemode()`](https://docs.python.org/3/library/turtle.html#turtle.resizemode)
[`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize) | [`turtlesize()`](https://docs.python.org/3/library/turtle.html#turtle.turtlesize)
[`shearfactor()`](https://docs.python.org/3/library/turtle.html#turtle.shearfactor)
[`settiltangle()`](https://docs.python.org/3/library/turtle.html#turtle.settiltangle)
[`tiltangle()`](https://docs.python.org/3/library/turtle.html#turtle.tiltangle)
[`tilt()`](https://docs.python.org/3/library/turtle.html#turtle.tilt)
[`shapetransform()`](https://docs.python.org/3/library/turtle.html#turtle.shapetransform)
[`get_shapepoly()`](https://docs.python.org/3/library/turtle.html#turtle.get_shapepoly)

#### Uso de eventos

[`onclick()`](https://docs.python.org/3/library/turtle.html#turtle.onclick)
[`onrelease()`](https://docs.python.org/3/library/turtle.html#turtle.onrelease)
[`ondrag()`](https://docs.python.org/3/library/turtle.html#turtle.ondrag)

#### Métodos especiales de Turtle

[`begin_poly()`](https://docs.python.org/3/library/turtle.html#turtle.begin_poly)
[`end_poly()`](https://docs.python.org/3/library/turtle.html#turtle.end_poly)
[`get_poly()`](https://docs.python.org/3/library/turtle.html#turtle.get_poly)
[`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone)
[`getturtle()`](https://docs.python.org/3/library/turtle.html#turtle.getturtle) | [`getpen()`](https://docs.python.org/3/library/turtle.html#turtle.getpen)
[`getscreen()`](https://docs.python.org/3/library/turtle.html#turtle.getscreen)
[`setundobuffer()`](https://docs.python.org/3/library/turtle.html#turtle.setundobuffer)
[`undobufferentries()`](https://docs.python.org/3/library/turtle.html#turtle.undobufferentries)

## Métodos de TurtleScreen/Screen

### Control de la ventana

[`bgcolor()`](https://docs.python.org/3/library/turtle.html#turtle.bgcolor)
[`bgpic()`](https://docs.python.org/3/library/turtle.html#turtle.bgpic)
[`clear()`](https://docs.python.org/3/library/turtle.html#turtle.clear) | [`clearscreen()`](https://docs.python.org/3/library/turtle.html#turtle.clearscreen)
[`reset()`](https://docs.python.org/3/library/turtle.html#turtle.reset) | [`resetscreen()`](https://docs.python.org/3/library/turtle.html#turtle.resetscreen)
[`screensize()`](https://docs.python.org/3/library/turtle.html#turtle.screensize)
[`setworldcoordinates()`](https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates)

### Control de la animación

[`delay()`](https://docs.python.org/3/library/turtle.html#turtle.delay)
[`tracer()`](https://docs.python.org/3/library/turtle.html#turtle.tracer)
[`update()`](https://docs.python.org/3/library/turtle.html#turtle.update)

### Uso de eventos de pantalla

[`listen()`](https://docs.python.org/3/library/turtle.html#turtle.listen)
[`onkey()`](https://docs.python.org/3/library/turtle.html#turtle.onkey) | [`onkeyrelease()`](https://docs.python.org/3/library/turtle.html#turtle.onkeyrelease)
[`onkeypress()`](https://docs.python.org/3/library/turtle.html#turtle.onkeypress)
[`onclick()`](https://docs.python.org/3/library/turtle.html#turtle.onclick) | [`onscreenclick()`](https://docs.python.org/3/library/turtle.html#turtle.onscreenclick)
[`ontimer()`](https://docs.python.org/3/library/turtle.html#turtle.ontimer)
[`mainloop()`](https://docs.python.org/3/library/turtle.html#turtle.mainloop) | [`done()`](https://docs.python.org/3/library/turtle.html#turtle.done)

### Configuraciones y métodos especiales

[`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode)
[`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode)
[`getcanvas()`](https://docs.python.org/3/library/turtle.html#turtle.getcanvas)
[`getshapes()`](https://docs.python.org/3/library/turtle.html#turtle.getshapes)
[`register_shape()`](https://docs.python.org/3/library/turtle.html#turtle.register_shape) | 
[`addshape()`](https://docs.python.org/3/library/turtle.html#turtle.addshape)[`turtles()`](https://docs.python.org/3/library/turtle.html#turtle.turtles)
[`window_height()`](https://docs.python.org/3/library/turtle.html#turtle.window_height)
[`window_width()`](https://docs.python.org/3/library/turtle.html#turtle.window_width)

### Métodos de entrada

[`textinput()`](https://docs.python.org/3/library/turtle.html#turtle.textinput)
[`numinput()`](https://docs.python.org/3/library/turtle.html#turtle.numinput)

### Métodos específicos de Screen

[`bye()`](https://docs.python.org/3/library/turtle.html#turtle.bye)
[`exitonclick()`](https://docs.python.org/3/library/turtle.html#turtle.exitonclick)
[`setup()`](https://docs.python.org/3/library/turtle.html#turtle.setup)
[`title()`](https://docs.python.org/3/library/turtle.html#turtle.title)

# Ejercicios

1.- Crea mediante funciones las siguientes formas geométricas:

- un cuadrado de tamaño `side`

```python
import turtle


def square(squirtle, side):
    for i in range(4):
        squirtle.forward(side)
        squirtle.right(90)


leonardo = turtle.Turtle()
square(leonardo, 100)
turtle.done()

```

- una estrella de cinco puntas de lado `side`
```python
import turtle


def star(squirtle, side):
    for i in range(5):
        squirtle.forward(side)
        squirtle.right(144)


leonardo = turtle.Turtle()
star(leonardo, 100)
turtle.done()
```
- un polígono de `sides` lados de longitud `side_lenght`
```python
import turtle


def poligon(squirtle, sides, side_length):
    angle = 360 / sides
    for i in range(sides):
        squirtle.forward(side_length)
        squirtle.right(angle)


leonardo = turtle.Turtle()
poligon(leonardo, 6, 100)
turtle.done()

```

- una espiral cuadrada de lado `size` y decremento `dec`

```python
import turtle


def square_spiral(squirtle, size, dec):
    for i in range(size//(dec * 4)):
        for i in range(4):
            squirtle.fd(size)
            squirtle.left(90)
            size -= dec


# Prepare the screen
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

# Create the turtle
squirtle = turtle.Turtle()
squirtle.color("blue")

# Draw the spiral
square_spiral(squirtle, 200, 2)

turtle.done()

```

