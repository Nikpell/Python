"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import pickle
import csv
from typing import Iterator


def pickle_to_csv(file_name):
    with (open(file_name, 'rb') as f_r,
          open('new.csv', 'w', encoding='utf-8') as f_w):
        my_dict = pickle.load(f_r)
        for ask_id, value, in my_dict.items():
            for name, level in value.items():
                print(f'{ask_id},{name},{level}', file=f_w)

pickle_to_csv('baza.pickle')
