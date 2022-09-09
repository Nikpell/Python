# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12
def summa_of_elements_on_odd_position(numbers):
    result = 0
    for i in range(1, len(numbers), 2):
        result += numbers[i]
    return result



