#Написать функцию, которая принимает строку, содержащую GMT, и возвращает смешенное значение текущей даты
#и времени.

#00.00.0000

from datetime import datetime as dt

def get_datatime(time):
    min = int(dt.strftime(dt.today(), "%M"))
    hour = int(dt.strftime(dt.today(), '%H'))
    try:
       min = min + ( int(time[0]+time[3:]))
       hour = hour + int(time[:3])
    except ValueError:
        print('Попробуйте ввести время в формате +/-HHMM')
    str_time = str(hour)+ str(':') + str(min)
    print(hour, ':', min)
    print(str_time)

time = input("Введите время в формате +/-HHMM ")
today = dt.strftime(dt.today(), '%d.%m.%Y   %H:%M')
today1 = get_datatime(time)
print(today)
print(today1)
