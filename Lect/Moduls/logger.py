# temperature_logger, pressure_logger, wind_speed_logger
from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature; {}'
                   .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature; {}'
                   .format(time, data))

def wind_speed(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature; {}'
                   .format(time, data))