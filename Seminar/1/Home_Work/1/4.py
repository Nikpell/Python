# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    string = ['от 0 не включительно до положительных значений бесконечности',
              'от 0 не включительно до положительных значений бесконечности']
elif quarter == 2:
    string = ['от отрицательных значений бесконечности до 0 не включительно',
              'от 0 не включительно до положительных значений бесконечности']
elif quarter == 3:
    string = ['от отрицательных значений бесконечности до 0 не включительно',
              'от отрицательных значений бесконечности до 0 не включительно']
else:
    string = ['от 0 не включительно до положительных значений бесконечности',
              'от отрицательных значений бесконечности до 0 не включительно']
print(f'Диапазон координат по оси X {string[0]} , по оси Y {string[1]}.')
