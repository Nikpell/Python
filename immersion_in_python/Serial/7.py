"""
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.

Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.

Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
import random


def fill_file(number_string, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(number_string):
            f.writelines(f'{random.randint(-1000, 1000)}|'
                         f'{random.uniform(-1000, 1000)}\n')


def pseudonym():
    def name_gen():
        return [chr(random.randint(min_ord, max_ord))
                for _ in range(random.randint(4, 7))]

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    min_ord = ord('a')
    max_ord = ord('z')
    while True:
        name = name_gen()
        for _ in name:
            if _ in vowels:
                return ''.join(name).capitalize()


def string_to_file(number, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(number):
            line = pseudonym()
            file.writelines(f'{line}\n')


def amount_of_string(file1, file2):
    with (open(file1, 'r', encoding='utf-8') as file1,
          open(file2, 'r', encoding='utf-8') as file2,
          open('result.txt', 'w', encoding='utf-8') as file3):
        return sum(1 for _ in file1), sum(1 for _ in file2)


def new_string(res1, res2):
    res = int(res1[:-1].split('|')[0]) * float(res1[:-1].split('|')[1])
    if res < 0:
        return res2[:-1].lower() + ' ' + str(res * -1)
    else:
        return res2[:-1].upper() + ' ' + str(round(res))


def join_file(file_name1, file_name2):
    with (open(file_name1, 'r', encoding='utf-8') as file1,
          open(file_name2, 'r', encoding='utf-8') as file2,
          open('result.txt', 'w', encoding='utf-8') as file3):
        max_len = max(amount_of_string(file_name1, file_name2))
        for _ in range(max_len):
            res1, res2 = file1.readline(), file2.readline()
            if res1 != '' and res2 != '':
                print(new_string(res2, res1), file=file3)
            else:
                if res1 == '':
                    file1.seek(0, 0)
                    res1 = file1.readline()
                else:
                    file2.seek(0, 0)
                    res2 = file2.readline()
                print(new_string(res2, res1), file=file3)


if __name__ == '__main__':
    # fill_file(5, 'new_data.txt')
    # string = pseudonym()
    # string_to_file(10, 'name.txt')
    # with open('name.txt') as f:
    #     res = f.readline()
    #     while res != '':
    #         print(res)
    #         res = f.readline()
    join_file('../office_work/Pack/name.txt', 'new_data.txt')
