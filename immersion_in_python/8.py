"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
всех вложенных файлов и директорий.

"""
import csv
import os
import pickle
from pathlib import Path
from typing import Any
import json


def folder_size(folder: str) -> int:
    return sum(p.stat().st_size for p in Path(folder).rglob('*'))


def directory(get_path):
    my_dic: dict[str, list[Any]] = {'папка': [],
                                    'поддиректории': [],
                                    'объем папки': [],
                                    'родительская директория': [],
                                    'файлы': [],
                                    'размер файла': [],
                                    }
    with (open('dict_new.csv', 'w', newline='', encoding='utf-8') as f_write,
          open('dict_new.json', 'w', encoding='utf-8') as f_json,
          open('dict_new.pickle', 'wb', ) as f_pickle):
        for parents, dir_, file_ in os.walk(get_path):
            my_dic.setdefault("папка").append(parents)
            my_dic.setdefault("поддиректории").append(dir_)
            my_dic.setdefault("объем папки").append(folder_size(parents))
            my_dic.setdefault("родительская директория").append('/'.join(parents.split('/')[:-1]))
            my_dic.setdefault("файлы").append(file_)
            my_dic.setdefault('размер файла').append([os.stat(parents + '/' + x).st_size for x in file_])
        fieldnames: list[str] = [x for x in my_dic.keys()]
        writer = csv.DictWriter(f_write, fieldnames=fieldnames, dialect='unix', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for i in range(len(my_dic["папка"])):
            writer.writerow({"папка": my_dic["папка"][i],
                             "поддиректории": my_dic["поддиректории"][i],
                             "объем папки": my_dic["объем папки"][i],
                             "родительская директория": my_dic["родительская директория"][i],
                             "файлы": my_dic["файлы"][i],
                             'размер файла': my_dic['размер файла'][i],
                             })
        json.dump(my_dic, f_json)
        pickle.dump(my_dic, f_pickle)


if __name__ == '__main__':
    directory('/home/nic/Рабочий стол/Python/immersion_in_python/files')
