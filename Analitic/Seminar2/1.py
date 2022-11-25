# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#
# *Примеры:*
#
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def list_numbers(number: int):
    for i in range(-number, number + 1):
        print(i, end=", ")


list_numbers(int(input('Введите число: ')))
