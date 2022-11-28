import random


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def my_list(quantity: int):
    work_list = []
    for i in range(quantity):
        work_list.append(random.randint(1, 100))
    return work_list


def summa_odd_elements(input_list: list):
    summa = 0
    for i in range(1, len(input_list), 2):
        summa += input_list[i]
    return summa


def new_summa_of_elements_on_odd_position(numbers):
    del numbers[::2]
    return sum(numbers)


any_list = my_list(int(input('Задайте количество чисел: ')))
print(any_list)
print(summa_odd_elements(any_list))
print(new_summa_of_elements_on_odd_position(any_list))
