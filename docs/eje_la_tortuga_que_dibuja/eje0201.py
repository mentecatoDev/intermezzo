import turtle

turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()
wn.bgcolor('white')

leonardo = turtle.Turtle()
leonardo.speed('fastest')
leonardo.pencolor('blue')

for x in range(200):
    leonardo.width(x/100 + 1)
    leonardo.forward(x)
    leonardo.left(88)

turtle.exitonclick()
