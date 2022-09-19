# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

# num = int(input('Введите число: '))
# output = []
# product = 1
# for i in range(1, num + 1):
#     product *= i
#     output.append(product)
# print(output)


def product_of_numbers(number_in_string):
    return [math.factorial(i) for i in range(1, int(number_in_string) + 1)]




