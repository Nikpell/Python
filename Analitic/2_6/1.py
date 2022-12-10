# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# *Пример:*
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

def unique_values(incom_list: list):
    # цикл
    # new_list = []
    # for item in incom_list:
    #     if incom_list.count(item) == 1:
    #         print(item)
    #         new_list.append(item)
    # return new_list
    #

    # list comprehension
    # return [item for item in incom_list if incom_list.count(item) == 1]

    # filter
    return list(filter(lambda item: incom_list.count(item) == 1, incom_list))


inc_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(unique_values(inc_list))
