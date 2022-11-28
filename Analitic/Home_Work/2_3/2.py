# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

def multiplication_couples_in_list(work_list: list):
    new_list = []
    for i in range(len(work_list) // 2):
        new_list.append(work_list[i] * work_list[-1 - i])
    if len(work_list) % 2 != 0:
        new_list.append(work_list[len(work_list) // 2] ** 2)
    return new_list


example_list = [2, 3, 4, 5, 6]
print(multiplication_couples_in_list(example_list))
