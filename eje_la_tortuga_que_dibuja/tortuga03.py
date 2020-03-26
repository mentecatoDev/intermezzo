import turtle

# setup the window and its attributes
turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("donatello & raphael")

# instantiate (create) donatello and set his attributes
donatello = turtle.Turtle()
donatello.color("hotpink")
donatello.pensize(5)

# instantiate raphael
raphael = turtle.Turtle()

# draw an equilateral triangle with donatello
donatello.forward(320)
donatello.left(120)
donatello.forward(320)
donatello.left(120)
donatello.forward(320)
donatello.left(120)

# turn donatello around and move her away from the origin
donatello.right(180)
donatello.forward(320)

# make raphael draw a square
raphael.forward(200)
raphael.left(90)
raphael.forward(200)
raphael.left(90)
raphael.forward(200)
raphael.left(90)
raphael.forward(200)

wn.exitonclick()
