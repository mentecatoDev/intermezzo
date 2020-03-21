import turtle

turtle.setup(800, 600, 0, 0)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Donatello's Spiral")
donatello = turtle.Turtle()
donatello.shape("turtle")
donatello.color("blue")

donatello.penup()            # this is new
size = 20
for i in range(30):
    donatello.stamp()        # leave an impression on the canvas
    size = size + 3          # increase the size on every iteration
    donatello.forward(size)  # move donatello along
    donatello.right(24)      # and turn her

turtle.done()
