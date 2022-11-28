# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference_between_min_max_fractional_part(work_list: list):
    work_list = list(filter(lambda x: x != 0, [round((item % 1), 5) for item in work_list]))
    return max(work_list) - min(work_list)


print(difference_between_min_max_fractional_part([1.1, 1.2, 3.1, 5, 10.01]))
