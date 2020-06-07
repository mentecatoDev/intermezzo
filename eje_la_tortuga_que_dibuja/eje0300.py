import turtle
import datetime


def load_lists(file_name, dates, confirmed, deads, recovered,
               confirmed_per_day, deads_per_day):
    '''
    Load «dates», «confirmed», «dead» and «recovered» «confirmed_per_day»
    lists from «file_name»
    '''

    file = open(file_name)
    confirmed_yesterday = 0
    deads_yesterday = 0
    for line in file:
        lst = line.split(',')

        # Extract and store date at «dates» in datetime format
        year = int(lst[0][0:4])
        month = int(lst[0][4:6])
        day = int(lst[0][6:8])
        dates.append(datetime.datetime(year, month, day))

        # Store «confirmed», «deads» and «recovered»
        confirmed.append(int(lst[1]))
        deads.append(int(lst[2]))
        recovered.append(int(lst[3]))

        # Calculate and store «confirmed_per_day»
        confirmed_per_day.append(int(lst[1]) - confirmed_yesterday)
        confirmed_yesterday = int(lst[1])

        # Calculate and store «deads_per_day»
        deads_per_day.append(int(lst[2]) - deads_yesterday)
        deads_yesterday = int(lst[2])

    file.close()


def config_canvas(title, wn, wn_width, wn_height, days, max_confirmed,
                  sections):
    """
    Prepare the canvas with the coordinate axes already scaled
    """

    def ejexy(leo, eje, color, size, sections, scale):
        """
        Draw the x and y axis
        """

        leo.penup()
        leo.goto(0, 0)
        leo.pendown()
        leo.color(color)
        leo.pensize(size)
        for i in range(sections):
            if eje == 'x':
                leo.goto(i, 0)
            else:
                leo.goto(0, i)
            leo.dot(5)
            leo.write(i*scale, move=False, align='right')

    # Inicialize and scale the canvas
    turtle.setup(wn_width, wn_height, 0, 0)
    leonardo = turtle.Turtle()
    wn.setworldcoordinates(-2, 0, days, (max_confirmed // sections) + 2)
    
    # Write the title
    leonardo.speed(0)
    leonardo.penup()
    leonardo.goto(2, max_confirmed // sections - 1)
    leonardo.color("red")
    leonardo.pendown()
    leonardo.write(title, False, "left", ("Arial", 16, "bold"))

    # Write de axes
    ejexy(leonardo, 'x', 'black', 3, days, 1)
    ejexy(leonardo, 'y', 'black', 3, max_confirmed//sections + 2, sections)


def draw_graph(title, data, wn, wn_width, wn_height, days, scale, color):
    max_data = max(data)
    """
    Draw a graph according to the data in the "data" list
    """

    config_canvas(title, wn, wn_width, wn_height, days, max_data, scale)
    donatello = turtle.Turtle()
    donatello.goto(0, 0)
    donatello.color("blue")
    for i in range(days):
        date_diff = dates[i] - start_date
        donatello.goto(date_diff.days, data[i]/scale)
        donatello.dot(5)
        donatello.write(data[i], move=False, align="right")


# Inicialize empty lists
dates = list()
confirmed = list()
deads = list()
recovered = list()
confirmed_per_day = list()
deads_per_day = list()

load_lists("covid-19.txt", dates, confirmed, deads, recovered,
           confirmed_per_day, deads_per_day)

# Calculate the number of «days» that have passed since the beginning
start_date = datetime.datetime(2020, 3, 1)
max_date = dates[-1]
date_diff = max_date - start_date
days = date_diff.days + 1

# Inicialize the Screen «wn»
wn_width = 960
wn_height = 1080
wn = turtle.Screen()

# Draw graph "Confirmados totales"
draw_graph("Confirmados totales", confirmed, wn, wn_width, wn_height, days,
           10000, "blue")

# Wait until press enter and reset the screen
input("Pulsa «Enter» para continuar...")
turtle.resetscreen()

# Draw graph "Víctimas Mortales"
draw_graph("Víctimas Mortales", deads, wn, wn_width, wn_height,
           days, 1000, "green")

# Wait until press enter and reset the screen
input("Pulsa «Enter» para continuar...")
turtle.resetscreen()

# Draw graph "Recuperados"
draw_graph("Recuperados", deads, wn, wn_width, wn_height,
           days, 1000, "green")

# Wait until press enter and reset the screen
input("Pulsa «Enter» para continuar...")
turtle.resetscreen()

# Draw graph "Confirmados diarios"
draw_graph("Confirmados diarios", confirmed_per_day, wn, wn_width, wn_height,
           days, 1000, "green")

# Wait until press enter and reset the screen
input("Pulsa «Enter» para continuar...")
turtle.resetscreen()

# Draw graph "Víctimas mortales diarias"
draw_graph("Víctimas mortales diarias", deads_per_day, wn, wn_width, wn_height,
           days, 100, "green")

wn.exitonclick()
