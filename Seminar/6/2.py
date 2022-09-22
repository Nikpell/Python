# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]


# outcoming_list = [i for i in incoming_list if incoming_list.count(i) == 1]
# print(outcoming_list)

def unique_number_in_list(income: list):
    return list(filter(lambda item: income.count(item) == 1, income))


print(unique_number_in_list(incoming_list))
