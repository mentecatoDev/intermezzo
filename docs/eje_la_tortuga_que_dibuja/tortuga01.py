import turtle

# Set the window size to 800x600 pixels at (0, 0)
turtle.setup(800, 600, 0, 0)

# Set the Screen object as wn
wn = turtle.Screen()

# Creates the turtle
leonardo = turtle.Turtle()
leonardo.forward(300)
leonardo.left(90)
leonardo.forward(200)

wn.exitonclick()
