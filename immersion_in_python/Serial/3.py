"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл
в формате CSV.
"""
import json
import csv
from typing import Iterator


def json_to_csv(file_name):
    with (open(file_name, 'r', encoding='utf-8') as file,
          open('baza.csv', 'w', newline='', encoding='utf-8')
          as f_write):
        dict_file = json.load(file)
        for ask_id, value, in dict_file.items():
            for name, level in value.items():
                print(f'{ask_id},{name},{level}', file=f_write)


json_to_csv('baza.json')
