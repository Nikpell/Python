"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу
и количество попыток. Внутри генерируется случайное число в указанных
границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.
"""
from random import randint


def guessfun(string):
    old_numbers = {'low': 1, 'hight': 10, 'attempts': 2}
    if string != '':
        dict_ = dict(zip(['low', 'hight', 'attempts'], [int(x) for x in string.split(' ')]))
        old_numbers.update(dict_)
    puzzle = randint(old_numbers['low'], old_numbers['hight'])
    flag = False
    for x in range(old_numbers['attempts']):
        number = int(input('Введите число: '))
        if number == puzzle:
            flag = True
            break
        elif number < puzzle:
            print('Больше')
        else:
            print('Меньше')
    return flag


# if __name__ == '__main__':
#     print(guessfun())
