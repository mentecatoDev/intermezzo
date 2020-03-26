import turtle

wn = turtle.Screen()
wn.setup(800, 600, 0, 0)
wn.title("Relleno de figuras")

leonardo = turtle.Turtle()
leonardo.speed(1)

leonardo.pensize(5)
leonardo.fillcolor("red")
leonardo.begin_fill()
leonardo.goto(100, 100)
leonardo.goto(200, -100)
leonardo.goto(300, 0)
leonardo.goto(0, 0)
leonardo.end_fill()
leonardo.hideturtle()

wn.exitonclick()
