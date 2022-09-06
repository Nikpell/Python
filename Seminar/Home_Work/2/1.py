# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 0,56 -> 11
num = input('Введите число: ')
summa = 0
for i in range(0, len(num)):
    if num[i].isdigit():
        summa += int(num[i])
print(summa)
