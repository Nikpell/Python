# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_coordinate = int(input('Введите координату точки по оси X: '))
y_coordinate = int(input('Введите координату точки по оси Y: '))
if x_coordinate > 0 and y_coordinate > 0:
    quarter = 1
elif x_coordinate > 0 > y_coordinate:
    quarter = 4
elif x_coordinate < 0 and y_coordinate < 0:
    quarter = 3
else:
    quarter = 2
print(f'Точка находится в {quarter} четверти плоскости.')
