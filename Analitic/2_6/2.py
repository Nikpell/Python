# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
#
# 2+2 => 4;
#
# 1+22*33 => 7;
#
# 1-2*3 => -5;

def equivalent_eval(arithmetic_string: str):
    arithmetic_string = arithmetic_string.replace('*', ' * ')
    arithmetic_string = arithmetic_string.replace('/', ' / ')
    arithmetic_string = arithmetic_string.replace('+', ' + ')
    arithmetic_string = arithmetic_string.replace('-', ' - ')
    arithmetic_list = arithmetic_string.split()
    mathematics_action_list = ['*', '/', '+', '-']

    def action(math_list: list, index: int):
        del math_list[index: index + 2]
        return math_list

    for x in mathematics_action_list:
        while arithmetic_list.count(x) > 0:
            index = arithmetic_list.index(x)
            match x:
                case '*':
                    arithmetic_list[index - 1] = int(arithmetic_list[index - 1]) * int(arithmetic_list[index + 1])
                    action(arithmetic_list, index)
                case "/":
                    arithmetic_list[index - 1] = int(arithmetic_list[index - 1]) / int(arithmetic_list[index + 1])
                    action(arithmetic_list, index)
                case '+':
                    arithmetic_list[0] = int(arithmetic_list[0]) + int(arithmetic_list[index + 1])
                    action(arithmetic_list, index)
                case '-':
                    arithmetic_list[0] = int(arithmetic_list[0]) - int(arithmetic_list[index + 1])
                    action(arithmetic_list, index)
    return arithmetic_list[0]


print(equivalent_eval('1 - 2 * 3'))
