import datetime
import calendar

date = input("Introduce la fecha en el formato MM DD YYYY: ")

date = date.split()

if int(date[2]) >= 2000 and int(date[2]) <= 3000:
    my_date = datetime.date(int(date[2]), int(date[0]), int(date[1]))
    print(calendar.day_name[my_date.weekday()].upper())