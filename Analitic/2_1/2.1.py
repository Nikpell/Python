import math


# 1.
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

def weekend(day: int):
    if day == 6 or day == 7:
        print("Weekend")
    elif day < 1 or day > 7:
        print("That isn't a day of week")
    else:
        print("Sorry, You have to go to a work")


# weekend(int(input("Input day of week(1 - 7): ")))


# 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def expression_check():
    x_list = [False, True, False, False, True, False, True, True]
    y_list = [False, False, True, False, True, True, False, True]
    z_list = [False, False, False, True, False, True, True, True]
    check = 0
    for i in range(8):
        if not (x_list[i] or y_list[i] or z_list[i]) != (not x_list[i] and not y_list[i] and not z_list[i]):
            print(f'При значении предикат {x_list[i]}, {y_list[i]}, {z_list[i]} утверждение не истинно!')
            break
        else:
            check = i
    if check == 7:
        print(f'При любом значении предикат утверждение истинно!')


# expression_check()

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

def quarter_coordinate(x: int, y: int):
    if x > 0 and y > 0:
        quarter = 1
    elif x > 0 > y:
        quarter = 4
    elif x < 0 and y < 0:
        quarter = 3
    else:
        quarter = 2
    print(f'Точка находится в {quarter} четверти плоскости.')


# x = int(input('Введите координату точки по оси X: '))
# y = int(input('Введите координату точки по оси Y: '))
# quarter_coordinate(x, y)

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

def coordinate_range(quarter: int):
    if quarter == 1:
        sentence = ['от 0 не включительно до положительных значений бесконечности',
                    'от 0 не включительно до положительных значений бесконечности']
    if quarter == 2:
        sentence = ['от отрицательных значений бесконечности до 0 не включительно',
                    'от 0 не включительно до положительных значений бесконечности']
    if quarter == 3:
        sentence = ['от отрицательных значений бесконечности до 0 не включительно',
                    'от отрицательных значений бесконечности до 0 не включительно']
    if quarter == 4:
        sentence = ['от 0 не включительно до положительных значений бесконечности',
                    'от отрицательных значений бесконечности до 0 не включительно']
    else:
        sentence = ['не может быть определен, вы ввели недопустимое значение четверти',
                    'не может быть определен, вы ввели недопустимое значение четверти']
    print(f'Диапазон координат по оси X {sentence[0]} , по оси Y {sentence[1]}.')


# coordinate_range(int(input("Введите номер четверти (1- 4): ")))

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def distance_between_points(string_a: str, string_b: str):
    coordinate_a = [int(string_a.split(',')[0]), int(string_a.split(',')[1])]
    coordinate_b = [int(string_b.split(',')[0]), int(string_b.split(',')[1])]
    distance_a_to_b = math.sqrt((coordinate_a[0] - coordinate_b[0]) ** 2 + (coordinate_a[1] - coordinate_b[1]) ** 2)
    print(f'Расcтояние от точки А до точки В = {distance_a_to_b}')


# string_a = input('Введите координаты точки А через запятую: ')
# string_b = input('Введите координаты точки B через запятую: ')
# distance_between_points(string_a, string_b)
