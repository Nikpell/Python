"""
Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени
 добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно
 работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
 берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное
 имя, если оно передано. Далее счётчик файлов и расширение.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы
 с файлами.
"""
import os


def rename_files(name='', didit=3, extension_in='txt', extension_out='tt', span=None):
    if span is None:
        span = [3, 6]
    span_start = span[0] - 1
    span_end = span[1]
    file_extension = []
    file_extension_old = []
    for file in os.listdir():
        if file.split('.')[-1] == extension_in:
            file_extension.append(file.split('.')[0])
            file_extension_old.append(file)
    for i in range(len(file_extension)):
        if len(file_extension[i]) > span_end:
            file_extension[i] = file_extension[i][span_start:span_end] + name
        else:
            file_extension[i] = file_extension[i] + name
    range_start = int('1' * didit)
    range_list = [_ for _ in range(range_start, range_start + len(file_extension))]
    file_extension = list(map(lambda x, y: x + str(y) + '.' + extension_out,
                              file_extension, range_list))
    for i in range(len(file_extension)):
        os.rename(file_extension_old[i], file_extension[i])
