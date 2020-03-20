import turtle

# establece el tamaño de la ventana a 800x600 píxeles
turtle.setup(800, 600)

# establece wn como objeto Screen
wn = turtle.Screen()

# se crea la tortuga
leonardo = turtle.Turtle()
leonardo.forward(300)
leonardo.left(90)
leonardo.forward(200)

wn.exitonclick()