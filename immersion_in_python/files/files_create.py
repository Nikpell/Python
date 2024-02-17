"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.

Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""
import random


def create_file(extension, min_len=6, max_len=30, min_bite=30, max_bite=4096, number_file=42):
    for _ in range(number_file):
        length = random.randint(min_len, max_len)
        num_bite = random.randint(min_bite, max_bite)
        min_ord = ord('a')
        max_ord = ord('z')
        name = ''.join([chr(random.randint(min_ord, max_ord)) for _ in range(length)]) + '.' + extension
        txt_bite = random.randbytes(num_bite)
        with open(name, 'w', encoding='utf-8') as f:
            print(txt_bite, file=f)


def create_file_with_different_extensions(number_files: object = 2, list_extensions: object = None) -> object:
    if list_extensions is None:
        list_extensions = ['txt', 'pdf', 'csv']
    for _ in range(number_files):
        extension = random.choice(list_extensions)
        create_file(extension=extension, number_file=1)


if __name__ == '__main__':
    create_file_with_different_extensions()
