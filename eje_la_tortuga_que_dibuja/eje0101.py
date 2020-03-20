import turtle


def star(squirtle, side):
    for i in range(5):
        squirtle.forward(side)
        squirtle.right(144)


leonardo = turtle.Turtle()
star(leonardo, 100)
turtle.done()
