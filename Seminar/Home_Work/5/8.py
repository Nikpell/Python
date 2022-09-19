# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Алгоритм RLE (англ. Run-Length Encoding) — алгоритм сжатия,
# заменяющий идущие подряд одинаковые символы парой (повторяющийся символ, количество повторений).
# Например, строчку aaababbcbbb он переводит в (a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3).


def compression_rle(string):
    simple = []
    while string != '':
        i = 1
        while i < len(string):
            if string[0] == string[i]:
                i += 1
            else:
                break
        simple.append(f'{string[0]}, {i}')
        string = string[i:]
    return '(' + ') ('.join(simple) + ')'


def string_to_file(string, name='task_1.txt'):
    with open(f'{name}', 'w') as data:
        data.write(string)


def file_to_string(name_file: str):
    file = open(name_file, 'r')
    return file.read()


def recovery_rle(string):
    simple = string[1:-1].split(') (')
    simple_rec = [item.split(', ') for item in simple]
    simple_rec1 = [item[0] * int(item[1]) for item in simple_rec]
    return ''.join(simple_rec1)


string_to_file(compression_rle(file_to_string('task8_2.txt')), 'task8_3.txt')
string_to_file(recovery_rle(file_to_string('task8_3.txt')), 'task8_4.txt')
