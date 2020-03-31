import turtle
import datetime


def load_lists(file_name, dates, confirmed, deads, recovered,
               confirmed_per_day):
    '''
    Loads «dates», «confirmed», «dead» and «recovered» lists from «file_name»
    '''

    file = open(file_name)

    i = 0
    for line in file:
        lst = line.split(',')

        date_str = lst[0]
        year = int(date_str[0:4])
        month = int(date_str[4:6])
        day = int(date_str[6:8])

        dates.append(datetime.datetime(year, month, day))
        confirmed.append(int(lst[1]))
        deads.append(int(lst[2]))
        recovered.append(int(lst[3]))

        if i:
            confirmed_per_day.append(confirmed[i] - confirmed[i-1])
        else:
            confirmed_per_day.append(confirmed[0])
        i += 1

    file.close()


def config_canvas(wn, wn_width, wn_height, days, max_confirmed, sections):

    def ejexy(eje, color, size, sections, scale):
        leo = turtle.Turtle()
        leo.speed(0)
        leo.goto(0, 0)
        leo.color(color)
        leo.pensize(size)
        leo.penup()
        leo.goto(0, 0)
        leo.pendown()
        for i in range(sections):
            if eje == 'x':
                leo.goto(i, 0)
            else:
                leo.goto(0, i)
            leo.dot(5)
            leo.write(i*scale, move=False, align='right')

    turtle.setup(wn_width, wn_height, 0, 0)
    wn.setworldcoordinates(-1, 0, days, (max_confirmed // sections) + 2)
    ejexy('x', 'black', 3, days, 1)
    ejexy('y', 'black', 3, max_confirmed//sections + 2, sections)


dates = list()
confirmed = list()
deads = list()
recovered = list()
confirmed_per_day = list()

load_lists("covid-19.txt", dates, confirmed, deads, recovered,
           confirmed_per_day)

max_confirmed = max(confirmed)
start_date = datetime.datetime(2020, 3, 1)
max_date = dates[-1]
date_diff = max_date - start_date
days = date_diff.days + 1

wn_width = 1024
wn_height = 768

wn = turtle.Screen()
config_canvas(wn, wn_width, wn_height, days, max_confirmed, 5000)

leonardo = turtle.Turtle()
leonardo.goto(0, 0)
# leonardo.dot(5)
# wn.setworldcoordinates(-1, 0, days, max_confirmed)
leonardo.color("blue")
for i in range(days):
    date_diff = dates[i] - start_date
    leonardo.goto(date_diff.days, confirmed[i]/5000)
    leonardo.dot(5)
    leonardo.write(confirmed[i], move=False, align="right")
    print(confirmed[i])


input("Press Enter to continue...")

turtle.resetscreen()

# confirmed per day graph

#wn = turtle.Screen()
#wn.reset()
max_confirmed_per_day = max(confirmed_per_day)
config_canvas(wn, wn_width, wn_height, days, max_confirmed_per_day, 1000)

leonardo = turtle.Turtle()
leonardo.goto(0, 0)
# leonardo.dot(5)
# wn.setworldcoordinates(-1, 0, days, max_confirmed)
leonardo.color("blue")
for i in range(days):
    date_diff = dates[i] - start_date
    leonardo.goto(date_diff.days, confirmed_per_day[i]/1000)
    leonardo.dot(5)
    leonardo.write(confirmed_per_day[i], move=False, align="right")
    print(confirmed[i])

wn.exitonclick()
