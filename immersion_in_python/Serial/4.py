"""
Прочитайте созданный в прошлом задании csv файл без использования
csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла
представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import json
import csv


def csv_to_json(file_name_csv, file_name_json=None):
    with (open(file_name_csv, 'r', encoding='utf-8') as file_csv,
          open(file_name_json, 'w', encoding='utf-8') as file_json):
        li = list(file_csv)
        li = list(map(lambda x: x[0:-1], li))
        li = list(map(lambda x: x.split(','), li))
        for item in li:
            json.dump({f'{int(item[0]):010d}':
                                 [item[1].capitalize(), item[2],
                                  hash(item[0] + item[1])]}, file_json, ensure_ascii=False)
            print(file=file_json)


csv_to_json('baza.csv', 'new.json')
