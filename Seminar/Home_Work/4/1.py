# Вычислить число c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141

from math import factorial
from decimal import *


# первый вариант
def rounding_with_specified_precision(number, specified_precision):
    counter = 0
    while specified_precision < 1:
        specified_precision *= 10
        counter += 1
    return round(number, counter)


# Вариант с вычислением пи
def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1) ** k) * (Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (
                13591409 + 545140134 * k) / (640320 ** (3 * k)))
        k += 1
        # print("Шаг: {} из {} ".format(k, n))
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return pi


def precision(specified_precision):
    counter = 0
    while specified_precision < 1:
        specified_precision *= 10
        counter += 1
    getcontext().prec = (counter + 1)
    val = chudnovsky((counter + 1) / 14)
    print(val)


precision(0.001)
