# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число. 1 2 4 5 2.
# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя. *Пример:* [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв' 'Мы очень любим Питон'

# mylist = [int(nlist[i])-1 for i in range(1, len(nlist)) if int(nlist[i]) - 1 != int(nlist[i-1])] # print(mylist)

# new_list=[my_list[i] for i in range(1,len(my_list)) if my_list[i]>= max(my_list[0:i] ) ]

# text = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'
# index = 0
# list1 = text.split(' ')
# print(list1) list2 = [item for item in list1 if text_find not in item] print(list2)