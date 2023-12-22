# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора)
# элементы исходного списка. *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.


def unique_list_short(same_list):
    return list(set(same_list))


def unique_list_long(same_list):
    new_list = []
    for item in same_list:
        if new_list.count(item) < 1:
            new_list.append(item)
    return new_list


# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# Строку в верхнем регистре в остальных случаях

def transform(anything):
    if anything.isdigit():
        anything = int(anything)
    else:
        try:
            anything = float(anything)
        except ValueError:
            if anything.islower():
                anything = anything.upper()
            else:
                anything = anything.lower()
    return anything


# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.
def dict_from_set(sample_tuple):
    dictionary = {}
    for item in sample_tuple:
        key = type(item).__name__
        if key not in dictionary:
            dictionary[key] = [item]
        else:
            dictionary[key].append(item)
    return dictionary


# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.
def dupl_remove(li):
    return [i for i in li if li.count(i) != 2]


# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# Нумерация начинается с единицы.
def number_of_odd(li):
    return [i + 1 for i in range(len(li) - 1) if li[i] % 2 != 0]


# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Слова нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.
def text_alignment(text):
    text = text.split()
    text.sort()
    alignment = len(max(text, key=len))
    for i in range(len(text)):
        print(f'{i + 1}\t {text[i]:>{alignment}}')


# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.
def quantity_latte(text):
    letter = {}
    letter_simple = {}
    for item in text:
        if item.isalpha():
            if item not in letter:
                letter[item] = 1
            else:
                letter[item] += 1
    for item in text:
        if item.isalpha():
            letter_simple[item] = text.count(item)
    return letter == letter_simple


# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

def things(thing):
    for key in thing:
        thing[key] = set(thing[key])
    print(f"Вещи взяли все три друга {thing['Петя']&thing['Вася']&thing['Юля']}")
    print(f"Вещи уникальны {thing['Петя']|thing['Вася']|thing['Юля']}")
    print(f"Какие вещи есть у всех друзей кроме одного: {thing['Петя']-thing['Вася']-thing['Юля']}")






dict_thing = {'Петя': (
    'топор', 'палатка', 'спички',
),
    'Вася': (
        'топор', 'спальник', 'спички',
    ),
    'Юля': (
        'лопата', 'цветы', 'спички',
    )
}

# print(dict_thing.values())
things(dict_thing)
# li = [1, 2, 2, 3, 1, 2, 3, 5, 6]
# print(unique_list_short(li))
# print(unique_list_long(li))
# print(transform('-3'))
# sample_tuple = (1, 2, '1', '2', [1, 2], (1, 2), {1: 2}, {1, 2})
# print(dict_from_set(sample_tuple))
# print(dupl_remove(li))
# print(number_of_odd(li))
# sample_txt = ('Функция  применяет указанную функцию к каждому элементу '
#               'итерируемого объекта и возвращает итератор с теми объектами,'
#               'для которых функция вернула.')
# print(text_alignment(sample_txt))
# print(quantity_latte(sample_txt))
