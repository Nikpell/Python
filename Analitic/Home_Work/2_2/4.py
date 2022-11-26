import random


# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]


def random_list(number: int):
    return [random.randint(1000, 10000) for i in range(number)]


def delete_digit_from_list(number: str, list_int: list):
    example_str = list(map(str, list_int))
    example_str = list(map(lambda x: x.replace(number, ''), example_str))
    return example_str


def summa_digit_in_each_item(list_string: list):
    for i in range(len(list_string)):
        while len(list_string[i]) != 1:
            list_string[i] = str(sum([int(x) for x in list_string[i]]))
    return list(map(lambda x: int(x), list_string))


# def delete_double(list_digit: list):  если не важен порядок в списке
#     list_digit_set = set(list_digit)
#     return list(list_digit_set)

def delete_double(list_digit: list):
    non_double_list = []
    for item in list_digit:
        if item not in non_double_list:
            non_double_list.append(item)
    return non_double_list


quantity_digit = int(input('Введите количество цифр: '))
example_list = random_list(quantity_digit)
print(example_list)
digit = input('Введите цифру, которую нужно удвлить: ')
new_list = delete_digit_from_list(digit, example_list)
print(new_list)
digit_list = summa_digit_in_each_item(new_list)
print(digit_list)
print(delete_double(digit_list))
