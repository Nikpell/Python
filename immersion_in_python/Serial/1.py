"""
Dспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с
псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый
с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def txt_to_json(file_name='result.txt'):
    with (open(file_name, 'r', encoding='utf-8') as f,
          open('result.json', 'w') as f1):
        my_dict = {}
        for line in f:
            my_dict[line.split(' ')[0].capitalize()] = line.split(' ')[1][:-1]
        json.dump(my_dict, f1, indent=2)


txt_to_json()
