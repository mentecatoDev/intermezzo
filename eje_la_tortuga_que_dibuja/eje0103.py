import turtle


def poligon(squirtle, sides, side_length):
    angle = 360 / sides
    for i in range(sides):
        squirtle.forward(side_length)
        squirtle.right(angle)


leonardo = turtle.Turtle()
poligon(leonardo, 3,200)
turtle.done()