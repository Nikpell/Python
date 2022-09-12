# 3. Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел. Ответ записать в файл.

def greatest_common_multiple(number1, number2):
    multiplication = number1 * number2
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return multiplication / number1


with open('task1.txt', 'w') as data:
    data.write(str(greatest_common_multiple(5, 7)))
data.close()
