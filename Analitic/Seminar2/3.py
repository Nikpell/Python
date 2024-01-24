# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример:*
#
# - Для N = 5: 1, -3, 9, -27, 81

def square_minus_three(number: int):
    print(*[(-3) ** i for i in range(number)], sep=', ')


square_minus_three(5)
