import turtle


def poligon(squirtle, sides, side_length):
    angle = 360 / sides
    for i in range(sides):
        squirtle.forward(side_length)
        squirtle.left(angle)


leonardo = turtle.Turtle()
poligon(leonardo, 5, 200)
turtle.done()