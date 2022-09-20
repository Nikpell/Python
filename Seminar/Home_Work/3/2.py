# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def list_summa_of_pair(numbers):
    summa_pair = []
    for i in range(len(numbers) // 2):
        summa_pair += ([numbers[i] * numbers[-1 - i]])
        print(summa_pair)
    if len(numbers) % 2 != 0:
        summa_pair.append(numbers[round(len(numbers) / 2)] ** 2)
    return summa_pair


def new_list_summa_of_pair(numbers):
    if len(numbers) % 2 != 0:
        numbers.insert(len(numbers) // 2 + 1, numbers[len(numbers) // 2])
    return [numbers[i] * numbers[-1 - i] for i in range(len(numbers) // 2)]
