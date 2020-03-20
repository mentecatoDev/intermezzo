def square_spiral(squirtle, size, dec):
    for i in range(size//(dec * 4)):
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

# Draw the spiral
square_spiral(squirtle, 200, 2)

turtle.done()