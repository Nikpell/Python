# . Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#
# *Примеры:*
#
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

def first_number_fraction(number: float):
    if int(abs(number % 1 * 10 // 1)) == 0:
        print('нет')
    else:
        int(abs(number % 1 * 10 // 1))


first_number_fraction(float(input('Введите число; ')))
