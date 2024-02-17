"""
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

from os import path, mkdir
import random


def create_file_to_folder(extension: object, folder: object = '', min_len: object = 6, max_len: object = 30,
                          min_bite: object = 30, max_bite: object = 4096,
                          number_file: object = 42) -> object:
    """

    :rtype: object
    """
    for _ in range(number_file):
        length = random.randint(min_len, max_len)
        num_bite = random.randint(min_bite, max_bite)
        min_ord = ord('a')
        max_ord = ord('z')
        name = ''.join([chr(random.randint(min_ord, max_ord)) for _ in range(length)]) + '.' + extension
        txt_bite = random.randbytes(num_bite)
        if folder:
            if not path.isdir(folder):
                mkdir(folder)
            name = f'{folder}/{name}'
        try:
            with open(name, 'x', encoding='utf-8') as f:
                print(txt_bite, file=f)
        except:
            pass


if __name__ == '__main__':
    create_file_to_folder(extension='txt', )
