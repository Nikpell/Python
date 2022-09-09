# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 10.01] => 0.19
def difference_between_min_max_parts(float_list):
    float_list = [elements % 1 for elements in float_list]
    return max(float_list) - min(float_list)
