from fractions import Fraction


# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def ten_to_hex(number):
    number1 = number
    ten_to_six = {x: str(x) for x in range(10)}
    ten_to_six.update({10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'})
    list_numbers = [ten_to_six.get(number % 16)]
    while number // 16 != 0:
        number //= 16
        list_numbers.insert(0, ten_to_six.get(number % 16))
    str_hex = ''.join(map(str, list_numbers))
    return str_hex, str_hex == hex(number1)[2:]


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

def max_same_divider(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def fract(first, second):
    first_fraction = first.split('/')
    second_fraction = second.split('/')
    numerator_sum = (int(first_fraction[1]) * int(second_fraction[0]) +
                     int(first_fraction[0]) * int(second_fraction[1]))
    numerator_mult = int(first_fraction[0]) * int(second_fraction[0])
    denominator = int(first_fraction[1]) * int(second_fraction[1])
    divider_sum = max_same_divider(numerator_sum, denominator)
    divider_mult = max_same_divider(numerator_mult, denominator)
    summa_fractions = [str(int(numerator_sum / divider_sum)),
                       str(int(denominator / divider_sum))]
    divider_fractions = [str(int(numerator_mult / divider_mult)),
                         str(int(denominator / divider_mult))]
    summa_fractions = '/'.join(summa_fractions)
    divider_fractions = '/'.join(divider_fractions)
    return summa_fractions, divider_fractions


a = '2/3'
b = '1/2'
c = Fraction(2, 3)
d = Fraction(1, 2)
print(fract(a, b)[0], c+d)
