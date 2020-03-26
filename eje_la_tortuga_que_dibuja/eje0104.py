import turtle


def square_spiral(squirtle, size, dec):
    for i in range(size//(dec * 4)):
        for i in range(4):
            squirtle.fd(size)
            squirtle.left(90)
            size -= dec


turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

squirtle = turtle.Turtle()
squirtle.color("blue")

square_spiral(squirtle, 200, 5)
turtle.done()
