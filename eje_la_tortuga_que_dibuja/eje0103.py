import turtle


def poligon(squirtle, sides, side_length):
    angle = 360 / sides
    for i in range(sides):
        squirtle.forward(side_length)
        squirtle.left(angle)


turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()

leonardo = turtle.Turtle()
poligon(leonardo, 7, 120)

turtle.exitonclick()
