import random


# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def polynomial(exponent: int):
    my_dict = {}
    my_list = []
    for i in range(exponent, -1, -1):
        my_dict[i] = random.randint(-100, 100)
    for keys in my_dict:
        first_element = ''
        second_element = 'x'
        third_element = ''
        if my_dict.get(keys) == 0:
            continue
        if my_dict.get(keys) != 1:
            first_element = f'{my_dict.get(keys)}*'
        if keys > 1:
            third_element = f'**{keys}'
        if keys == 0:
            second_element = ''
            first_element = f'{my_dict.get(keys)}'
        my_list.append(f'{first_element}{second_element}{third_element}')
    # сделано для положительных коэффициентов, оптимизировать не стал, просто продолжил
    minus_list = list(filter(lambda x: x[0] == '-', my_list))
    minus_list = [x[0] + x[3:] if x[1:3] == '1*' else x for x in minus_list]
    minus_list = list(map(lambda x: ' - ' + x[1:], minus_list))
    plus_list = list(filter(lambda x: x[0] != '-', my_list))
    plus_list = list(map(lambda x: ' + ' + x, plus_list))
    my_list = plus_list + minus_list + [' = 0']
    return ''.join(my_list)[3:]


with open('2.txt', 'w') as data:
    data.write(polynomial(11))
