# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

string = '101 100 3 -5 3 4'
string = string.split(' ')
number = []
for element in string:
    number.append(int(element))
print(max(number), min(number))