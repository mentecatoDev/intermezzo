import turtle
import datetime


def load_lists(file_name, dates, confirmed, deads, recovered):
    '''
    Loads the lists «dates», «confirmed», «dead» and «recovered» from the
    «file_name»
    '''

    file = open(file_name)

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
    file.close()


dates = list()
confirmed = list()
deads = list()
recovered = list()
load_lists("covid-19.txt", dates, confirmed, deads, recovered)


max_confirmed = max(confirmed)

start_date = datetime.datetime(2020, 3, 1)
max_date = dates[-1]

date_diff = max_date - start_date
total_days = date_diff.days + 1


wn_width = 1024
wn_height = 768

turtle.setup(wn_width, wn_height, 0, 0)
wn = turtle.Screen()
print(total_days, max_confirmed)
wn.setworldcoordinates(0, 0, total_days, max_confirmed)

leonardo = turtle.Turtle()
leonardo.goto(0, 0)
# leonardo.dot(5)

for i in range(total_days):
    date_diff = dates[i] - start_date
    leonardo.goto(date_diff.days, confirmed[i])
    leonardo.dot(5)
    print(confirmed[i])


turtle.done()
