# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; - Добавьте возможность использования скобок,
# меняющих приоритет операций. *Пример:* 1+2*3 => 7; (1+2)*3 => 9; 2.


example = '1-2*3'


def insert_space_past_each_word(input_string):
    output_string = ''
    for i in range(len(input_string) - 1):
        output_string += input_string[i] + ' '
    output_string += input_string[-1]
    return output_string


string = insert_space_past_each_word(example).split()

op_1 = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y}
op_2 = {'*': lambda x, y: x * y,
        '/': lambda x, y: x / y}

string = list(map(lambda item: int(item) if item.isdigit() else item, string))

index = 0
while ('*' in string) or ('/' in string):
    if string[index] in op_2:
        temp = op_2[string[index]](string[index - 1], string[index + 1])
        del string[index - 1:index + 2]
        string.insert(index - 1, temp)
        index = 0
    else:
        index += 1

index = 0
while '+' in string or '-' in string:
    if string[index] in op_1:
        temp = op_1[string[index]](string[index - 1], string[index + 1])
        del string[index - 1:index + 2]
        string.insert(index - 1, temp)
        index = 0
    else:
        index += 1
print(string)
