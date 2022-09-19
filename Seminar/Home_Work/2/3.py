# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

number = int(input('Введите число: '))
subsequence = []
product = 0
for i in range(1, number + 1):
    product = (1 + 1 / i) ** i
    subsequence.append(product)
print(sum(subsequence))

def summa_of_subsequence(numbers):
    return sum([(1 + 1 / i) ** i for i in range(1, numbers + 1)])
