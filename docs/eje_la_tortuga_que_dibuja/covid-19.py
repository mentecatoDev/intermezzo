import turtle
import datetime

file = open("covid-19.txt")

max_confirmed = 0
start_date = datetime.datetime(2020, 3, 1)
max_date = start_date

for line in file:
    lst = line.split(',')

    date_str = lst[0]
    confirmed = int(lst[1])

    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])

    date = datetime.datetime(year, month, day)

    if confirmed > max_confirmed:
        max_confirmed = confirmed

    if date > max_date:
        max_date = date

date_diff = max_date - start_date
total_days = date_diff.days


wn_width = 800
wn_height = 600

turtle.setup(wn_width, wn_height, 0, 0)
wn = turtle.Screen()

wn.setworldcoordinates(0, 0, total_days, max_confirmed)

leonardo = turtle.Turtle()
leonardo.goto(0, 0)

file.close()

file = open("covid-19.txt")

leonardo.speed(1)
for line in file:
    lst = line.split(',')

    date_str = lst[0]
    confirmed = int(lst[1])

    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])

    date = datetime.datetime(year, month, day)

    date_diff = date - start_date

    leonardo.goto(date_diff.days, confirmed)


turtle.done()
