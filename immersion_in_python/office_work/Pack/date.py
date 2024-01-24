"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату
 в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь,
если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует
Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с
передачей даты на проверку.
"""


def _leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return 29
    else:
        return 28


def truly_date(string_date):
    day = int(string_date.split('.')[0])
    month = int(string_date.split('.')[1])
    year = int(string_date.split('.')[2])
    if year not in range(1, 10000):
        return False
    if month not in range(1, 13):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and (day > _leap_year(year)):
        return False
    return True


if __name__ == '__main__':
    date = input('Введите дату в формате DD.MM.YYYY: ')
    print(truly_date(date))
