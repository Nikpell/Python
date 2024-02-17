"""
Напишите функцию, которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json


def json_dict():
    try:
        with open('baza.json', 'r', encoding='utf-8') as file:
            try:
                json_file = json.load(file)
            except:
                json_file = {}
    except:
        with open('baza.json', 'a', encoding='utf-8') as file:
            json_file = {}
    return json_file


def user_to_json(json_file) -> object:
    name = input('Введите имя: ')
    ask_id = input('Введите личный идентификатор: ')
    level = input('Введите уровень доступа: ')
    if json_file != {}:
        if ask_id in json_file.keys():
            print('Идентификатор уже существует')
        else:
            json_file.update({ask_id: {name: level}})
    else:
        json_file.update({ask_id: {name: level}})
    return json_file


def dict_json(json_file_new):
    with open('baza.json', 'w', encoding='utf-8') as file:
        json.dump(json_file_new, file)


while True:
    dict_json(user_to_json(json_dict()))
