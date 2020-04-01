import turtle

turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()
wn.bgcolor('white')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
leonardo = turtle.Pen()
leonardo.speed(0)

for x in range(200):
    leonardo.pencolor(colors[x % 6])
    leonardo.width(x/100 + 1)
    leonardo.forward(x)
    leonardo.left(59)

turtle.exitonclick()
