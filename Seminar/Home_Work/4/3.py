# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def list_of_non_repeated_elemets(list_element):
    i = 0
    while i < len(list_element):
        number = list_element[i]
        counter = list_element.count(number)
        if counter > 1:
            for j in range(0, counter):
                list_element.remove(number)
        i += 1
    return list_element
