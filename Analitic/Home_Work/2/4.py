# (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Ведите число: '))
subsequence = []
for i in range(- number, number + 1):
    subsequence.append(i)
data_file = open('file.txt')
data = data_file.read()
data_list = []
for i in range(0, len(data)):
    if data[i].isdigit():
        data_list += (data[i])
product = 1
for i in range(0, len(data_list)):
    product *= subsequence[int(data_list[i])]
print(product)
