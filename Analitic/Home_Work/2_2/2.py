
# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

def list_of_subsequence(number: int):
    example = [(1 + 1 / n) ** n for n in range(1, number + 1)]
    print(f'Список {example} \nCумма элементов = {sum(example)}')


# list_of_subsequence(5)
