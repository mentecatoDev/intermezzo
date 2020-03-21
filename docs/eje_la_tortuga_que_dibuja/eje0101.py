import turtle


def square(squirtle, side):
    for i in range(4):
        squirtle.forward(side)
        squirtle.right(90)


turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()

leonardo = turtle.Turtle()
square(leonardo, 100)

turtle.done()
