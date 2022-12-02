# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def summa_polynomial(polynomial_one: str, polynomial_two: str):
    def string_to_dict(polinomial: list):
        polinomial = list(filter(lambda x: x != '+', polinomial))
        polinomial = [item + '*x**0' if item.isdigit() else item for item in polinomial]
        for i in range(len(polinomial) - 1):
            if polinomial[i] == '-':
                polinomial[i + 1] = '-' + polinomial[i + 1]
        polinomial = list(filter(lambda x: x != '-', polinomial))
        polinomial = ['1*' + item if item[0] == 'x' else item for item in polinomial]
        polinomial = ['-1*' + item[1:] if item[:2] == '-x' else item for item in polinomial]
        polinomial = [item + '**1' if item[-1] == 'x' else item for item in polinomial]
        polinomial = list(map(lambda item: item.split('*x**'), polinomial))
        my_dict = {}
        for i in range(len(polinomial)):
            my_dict[int(polinomial[i][1])] = int(polinomial[i][0])
        return my_dict

    def dict_to_sting(input_dict: dict):
        my_list = []
        for keys in input_dict:
            first_element = ''
            second_element = 'x'
            third_element = ''
            if input_dict.get(keys) == 0:
                continue
            if input_dict.get(keys) != 1:
                first_element = f'{input_dict.get(keys)}*'
            if keys > 1:
                third_element = f'**{keys}'
            if keys == 0:
                second_element = ''
                first_element = f'{input_dict.get(keys)}'
            my_list.append(f'{first_element}{second_element}{third_element}')
        minus_list = list(filter(lambda x: x[0] == '-', my_list))
        minus_list = [x[0] + x[3:] if x[1:3] == '1*' else x for x in minus_list]
        minus_list = list(map(lambda x: ' - ' + x[1:], minus_list))
        plus_list = list(filter(lambda x: x[0] != '-', my_list))
        plus_list = list(map(lambda x: ' + ' + x, plus_list))
        my_list = plus_list + minus_list + [' = 0']
        return ''.join(my_list)[3:]

    one_list = polynomial_one[:-4].split(' ')
    two_list = polynomial_two[:-4].split(' ')
    one_dict = string_to_dict(one_list)
    two_dict = string_to_dict(two_list)

    for i in range(len(one_dict)):
        if i in two_dict:
            one_dict[i] += two_dict[i]
            two_dict.pop(i)
    one_dict.update(two_dict)

    sorted_tuple_one = sorted(one_dict.items(), key=lambda x: x[0], reverse=True)
    one_dict = dict(sorted_tuple_one)
    return dict_to_sting(one_dict)


with open('1.txt', 'r') as data:
    polynomial_one = data.read()
with open('2.txt', 'r') as data:
    polynomial_two = data.read()
with open('3.txt', 'w') as data:
    data.write(summa_polynomial(polynomial_one, polynomial_two))

