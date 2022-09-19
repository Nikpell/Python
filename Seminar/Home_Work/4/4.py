# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def polinomial(k):
    polinomial_list = []
    for i in range(k, -1, -1):
        number = random.randint(0, 100)
        if i > 1:
            if number == 0:
                continue
            elif number == 1:
                polinomial_list.append(f'x^{i}')
            else:
                polinomial_list.append(f'{number}*x^{i}')
        elif i == 1:
            if number == 0:
                continue
            elif number == 1:
                polinomial_list.append('x')
            else:
                polinomial_list.append(f'{number}*x')
        elif i == 0:
            if number == 0:
                continue
            else:
                polinomial_list.append(f'{number}')
    return ' + '.join(polinomial_list) + ' = 0'


with open('task42.txt', 'w') as data:
    data.write(polinomial(1))
data.close()



