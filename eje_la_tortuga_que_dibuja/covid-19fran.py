import turtle


def carga_lista(file_name, dias, confirmados, fallecidos, sanos):

    file = open(file_name)
    for line in file:
        lst = line.split(',')
        dias += 1
        confirmados.append(int(lst[1]))
        fallecidos.append(int(lst[2]))
        sanos.append(int(lst[3]))
    file.close()
    return dias


dias = 0
confirmados = list()
fallecidos = list()
sanos = list()
dias = carga_lista("covid-19.txt", dias, confirmados, fallecidos, sanos)

turtle.setup(1024, 768, 0, 0)
wn = turtle.Screen()
maximo = max(confirmados)
tramos = maximo // 5000
wn.setworldcoordinates(0, 0, dias, (tramos + 2)*5000)
wn.bgcolor('white')
donatello = turtle.Turtle()

donatello.color("black")
donatello.pensize(4)
donatello.penup()
donatello.goto(0, 0)
donatello.pendown()
for i in range(dias):
    donatello.goto(i, 0)
    donatello.dot(5)
    donatello.write(i)

donatello.color("black")
donatello.pensize(4)
donatello.penup()
donatello.goto(0, 0)
donatello.pendown()
for i in range(tramos + 2):
    donatello.goto(0, i * 5000)
    donatello.dot(5)
    donatello.write(i * 5000)

donatello.penup()
donatello.goto(0, 0)
donatello.pendown()
donatello.pensize(0)
donatello.color("blue")
for i in range(dias):
    donatello.goto(i, confirmados[i])
    donatello.write(confirmados[i])
    donatello.dot(5)

donatello.color("red")
donatello.penup()
donatello.goto(0, 0)
donatello.pendown()
donatello.pensize(0)
for i in range(dias):
    donatello.goto(i,fallecidos[i])
    donatello.write(fallecidos[i])
    donatello.dot(5)

donatello.color("green")
donatello.penup()
donatello.pensize(0)
donatello.goto(0, 0)
donatello.pendown()
for i in range(dias):
    donatello.goto(i,sanos[i])
    donatello.dot(5)
    donatello.write(sanos[i])
wn.exitonclick()
