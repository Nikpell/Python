# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def cut(new_list):
    cut_list = [element.replace('*x^', ' ').replace('x^', ' ').replace('*x', ' ').split(' ') for element in new_list]
    return cut_list


def change_null_to_one(new_list):
    for e in new_list:
        if len(e) > 1:
            for x in range(2):
                if e[x] == '':
                    e[x] = '1'
    return new_list


def string_to_integer_in_list_of_list(new_list):
    for element in new_list:
        for x in range(len(element)):
            element[x] = int(element[x])
    return new_list


data_file_1 = open('task41.txt', 'r')
data_1 = data_file_1.read()
data_file_2 = open('task42.txt', 'r')
data_2 = data_file_2.read()
data_1 = data_1[: -4]
data_2 = data_2[: -4]
data_1_list = data_1.split(' + ')
data_2_list = data_2.split(' + ')

new_list_1 = change_null_to_one(cut(data_1_list))
new_list_2 = change_null_to_one(cut(data_2_list))
new_list_1 = string_to_integer_in_list_of_list(new_list_1)
new_list_2 = string_to_integer_in_list_of_list(new_list_2)

if len(new_list_1) >= len(new_list_2):
    common_list_long = new_list_1
    common_list_short = new_list_2
else:
    common_list_long = new_list_2
    common_list_short = new_list_1

i = 0
j = 0
while i < len(common_list_short):
    while j < len(common_list_long) and i < len(common_list_short):
        if len(common_list_long[j]) > 1 and len(common_list_short[i]) > 1
            if common_list_short[i][1] > common_list_long[j][1]:
                common_list_long.insert(j, common_list_short[i])
                i += 1
            elif common_list_short[i][1] == common_list_long[j][1]:
                common_list_long[j][0] += common_list_short[i][0]
                i += 1
        j += 1
    i += 1

if len(common_list_short[-1]) == 1 and len(common_list_long[-1]) == 1:
    common_list_long[-1][0] += common_list_short[-1][0]
if len(common_list_short[-1]) == 1 and len(common_list_long[-1]) != 1:
    common_list_long.append(common_list_short[-1])

for i in range(len(common_list_long)):
    if len(common_list_long[i]) > 1:
        if common_list_long[i][0] > 1 and common_list_long[i][1] > 1:
            for j in range(len(common_list_long[i])):
                common_list_long[i][j] = str(common_list_long[i][j])
            common_list_long[i] = '*x^'.join(common_list_long[i])
        elif common_list_long[i][0] == 1 and common_list_long[i][1] > 1:
            common_list_long[i][0] = ''
            common_list_long[i][1] = str(common_list_long[i][1])
            common_list_long[i] = 'x^'.join(common_list_long[i])
        elif common_list_long[i][0] > 1 and common_list_long[i][1] == 1:
            common_list_long[i][0] = str(common_list_long[i][0])
            common_list_long[i][1] = ''
            common_list_long[i] = '*x'.join(common_list_long[i])

if len(common_list_long[-1]) == 1:
    common_list_long[-1] = str(common_list_long[-1][0])

input_string = ' + '.join(common_list_long) + " = 0"
with open('task43.txt', 'w') as data:
    data.write(input_string)

