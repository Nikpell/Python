# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

number = int(input('Ведите число: '))
subsequence = []
for i in range(- number, number + 1):
    subsequence.append(i)
string = input('Введите позиции элементов через пробел: ')
string_of_index = (string.split(' '))
product = 1
for i in range(0, len(string_of_index)):
    product *= subsequence[int(string_of_index[i])]
print(product)
