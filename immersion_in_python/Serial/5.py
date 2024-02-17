"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет
их содержимое в виде одноимённых pickle файлов.
"""
import os
import json
import pickle


def json_to_pickle(path_name: object) -> object:
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        my_list = [x for x in file_name if x.split('.')[1] == 'json']
    for item in my_list:
        with (open(item, 'r', encoding='utf-8') as f_r,
              open(item.split('.')[0] + '.pickle', 'wb', ) as f_w):
            pickle.dump(json.load(f_r), f_w)


my_path = '/home/nic/Рабочий стол/Python/immersion_in_python/Serial'
json_to_pickle(my_path)