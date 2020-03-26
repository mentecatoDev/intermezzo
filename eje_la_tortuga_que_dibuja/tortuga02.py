import turtle

# set the window size to 800 by 600 pixels at (0, 0)
turtle.setup(800, 600, 0, 0)

# set wn as a window object
wn = turtle.Screen()  

# set the background color of the window
wn.bgcolor("lightgreen")

# set the title of the window
wn.title("¡Hola, Raphael!")
raphael = turtle.Turtle()
raphael.color("blue")      # make raphael blue
raphael.pensize(3)         # set the width of the pen
raphael.forward(300)
raphael.left(120)
raphael.forward(300)

wn.exitonclick()
