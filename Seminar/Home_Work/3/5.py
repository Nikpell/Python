# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def list_of_numbers_fibonachi(quantity):
    fibonachi_list = [1, 0, 1]
    if quantity > 1:
        for i in range(2, quantity + 1):
            fibonachi_list.insert(0, (fibonachi_list[- 2] + fibonachi_list[- 1]) * (- 1) ** (i + 1))
            fibonachi_list.append(fibonachi_list[- 2] + fibonachi_list[- 1])
    return fibonachi_list
