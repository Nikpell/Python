# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
number = int(input('Введите число: '))
subsequence = []
product = 0
for i in range(1, number + 1):
    product = (1 + 1 / i) ** i
    subsequence.append(product)
print(sum(subsequence))