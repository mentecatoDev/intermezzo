import turtle


def square_spiral(squirtle, size, dec):
    for i in range(size // (dec * 4)):
        for i in range(4):
            squirtle.fd(size)
            squirtle.left(90)
            size -= dec


# Prepare the screen
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

# Create the turtle
squirtle = turtle.Turtle()
squirtle.color("blue")
squirtle.speed(0)

# Draw the spiral
square_spiral(squirtle, 400, 2)

turtle.done()
