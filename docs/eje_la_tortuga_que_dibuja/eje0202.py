import turtle

turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()
wn.bgcolor('white')

leonardo = turtle.Pen()
leonardo.color('blue')
leonardo.speed(0)

for x in range(200):
    leonardo.width(x/100 + 1)
    leonardo.forward(x)
    leonardo.left(59)

turtle.done()
