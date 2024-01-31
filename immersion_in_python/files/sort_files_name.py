"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

"""
from os import path, mkdir, listdir, rename


def sort_files(dict_extensions):
    for folder, value in dict_extensions:
        if folder:
            if folder:
                if not path.isdir(folder):
                    mkdir(folder)
        file_list = []
        for file in listdir():
            ext = file.split('.')[-1]
            if ext in value:
                file_list.append(file)
        for file in file_list:
            newfile = f'{folder}/{file}'
            rename(file, newfile)


dict_extensions = {
    'audio': ['rnd', 'txt'],
    'video': ['mpeg']
}
