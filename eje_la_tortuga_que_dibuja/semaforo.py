import turtle

turtle.setup(800,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    tess.pensize(3)
    tess.color("black","darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(40)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

state_num = 0

def nextFSMstate():
    global state_num
    if state_num == 0:
            tess.forward(70)
            tess.fillcolor("orange")
            state_num = 1
    elif state_num == 1:
            tess.forward(70)
            tess.fillcolor("red")
            state_num = 2
    else:
            tess.back(140)
            tess.fillcolor("green")
            state_num = 0

wn.onkey(nextFSMstate, "space")
wn.listen()
wn.mainloop()
    # example says wn.mainloop() but I get error. This works though