# Реализуйте алгоритм перемешивания списка.
from random import shuffle

subsecquence = []
number = int(input('Введите количество элементов:'))
for i in range(1, number + 1):
    subsecquence.append(i)
for i in range(1, number):
    index = 0
    index_2 = index + i
    if i // 2 == 0:
        while index + index_2 < len(subsecquence):
            temp = subsecquence[index]
            subsecquence[index] = subsecquence[index_2]
            subsecquence[index_2] = temp
            index = index_2 + 1
            index_2 += (i + 1)
    else:
        index = 1
        index_2 = index + i
        while index + index_2 < len(subsecquence):
            temp = subsecquence[-index]
            subsecquence[-index] = subsecquence[-index_2]
            subsecquence[-index_2] = temp
            index = index_2 + 1
            index_2 += (i + 1)


def shake(number_def: int):
    subsecquence_new = [i for i in range(1, number_def + 1)]
    shuffle(subsecquence_new)
    return subsecquence_new


