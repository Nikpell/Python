# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_of_week = int(input('Ввдите цифру, обозначающую день недели: '))
if 1 <= day_of_week < 6:
    print('Рабочий день')
elif day_of_week == 6 or day_of_week == 7:
    print('Выходной')
else:
    print('Вы ввели неверный формат дня недели')
