# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def summa_digit_one_string(number: str):
    return sum(list(map(int, filter(lambda i: i.isdigit(), [x for x in number]))))

# Через математику делать костыльно и все равно со строкой, на float особенности хранения сильно вмешивается,
def summa_digit_math(number: float):
    length = len(str(number))
    summa = 0
    while number != 0:
        if number % 1 != 0:
            number = round(number * 10, length)
        else:
            summa += number % 10
            number = round(number // 10, length)
    return summa

# number = input('Введите число: ')
# print(f'Сумма цифр числа {number} равна {summa_digit_one_string(number)}')

# number = float(input('Введите число: '))
# print(f'Сумма цифр числа {number} равна {summa_digit_math(number)}')

