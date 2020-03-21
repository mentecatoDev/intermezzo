import turtle


def star(squirtle, side):
    for i in range(5):
        squirtle.forward(side)
        squirtle.right(144)


turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()

leonardo = turtle.Turtle()
star(leonardo, 200)

turtle.done()
