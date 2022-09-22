# get_temperature, get_pressure, get_wind_speed
from random import randint
def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_pressure(sensor):
    if sensor:
        return randint(720, 760)
    else:
        return randint(761, 770)


def get_wind_speed(sensor):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(31, 100)

def data_collection():
    return  (get_temperature(), get_pressure(), get_wind_speed())