import turtle

# establecer el tamaño de la ventana de 800 por 600 píxeles
turtle.setup(800, 600)

wn = turtle.Screen()        # establecer wn al objeto de la ventana
wn.bgcolor("lightgreen")    # establecer el color de fondo de la ventana
wn.title("Hola, Tess!")     # establecer el título de la ventana
tess = turtle.Turtle()
tess.color("azure")          # hacer tess azul
tess.pensize(1)              # establecer el ancho de la pluma  
tess.forward(300)
tess.right(120)
tess.forward(300)
wn.exitonclick()
