# Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def minimum_multiple(number_1: int, number_2: int):
    i = 1
    while (max(number_1, number_2) * i % min(number_1, number_2)) != 0:
        i += 1
    return max(number_1, number_2) * i


print(minimum_multiple(12, 4))
