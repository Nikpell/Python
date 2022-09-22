# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; - Добавьте возможность использования скобок,
# меняющих приоритет операций. *Пример:* 1+2*3 => 7; (1+2)*3 => 9; 2.

def insert_space_past_each_word(input_string):
    output_string = ''
    for i in range(len(input_string) - 1):
        output_string += input_string[i] + ' '
    output_string += input_string[-1]
    return output_string


def index_start(input_list: list):
    if input_list.count('(') > 0:
        return [i for i in range(len(input_list)) if input_list[i] == '('][-1]
    else:
        return - 1


def index_end(input_list, index):
    if index != - 1:
        return input_list.index(')', index)
    else:
        return len(input_list)


def deduction(equal):
    while equal.count('*') > 0:
        i = equal.index('*')
        substing = [equal[i - 1] * equal[i + 1] for i in range(len(equal)) if equal[i] == '*']
        del equal[i - 1: i + 2]
        equal.insert( i - 1, substing[0])
    while equal.count('/') > 0:
        i = equal.index('/')
        substing = [equal[i - 1] / equal[i + 1] for i in range(len(equal)) if equal[i] == '/']
        del equal[i - 1: i + 2]
        equal.insert(i - 1, substing[0])
    while equal.count('+') > 0:
        i = equal.index('+')
        substing = [equal[i - 1] + equal[i + 1] for i in range(len(equal)) if equal[i] == '+']
        del equal[i - 1: i + 2]
        equal.insert(i - 1, substing[0])
    while equal.count('-') > 0:
        i = equal.index('-')
        substing = [equal[i - 1] - equal[i + 1] for i in range(len(equal)) if equal[i] == '-']
        del equal[i - 1: i + 2]
        equal.insert(i - 1, substing[0])
    return equal


simple = '(1+(1+2*5+9))*3'

string = insert_space_past_each_word(simple).split()
string = list(map(lambda item: int(item) if item.isdigit() else item, string))
while string.count('(') > 0:
    start = index_start(string)
    end = index_end(string, start)
    expression = [string[i] for i in range(start + 1, end)]
    del string[start:end + 1]
    string.insert(start, deduction(expression)[0])
meaning = deduction(string)


print(meaning)

