import turtle

wn = turtle.Screen()
wn.setup(800, 600, 0, 0)
wn.title("Relleno de figuras")

leonardo = turtle.Turtle()
leonardo.hideturtle()

leonardo.pensize(5)
leonardo.fillcolor("red")
leonardo.begin_fill()
leonardo.goto(100, 0)
leonardo.goto(100, 50)
leonardo.goto(0, 50)
leonardo.goto(0, 0)
leonardo.end_fill()

wn.exitonclick()
