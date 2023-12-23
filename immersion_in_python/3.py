import itertools


# Дан список повторяющихся элементов.Вернуть список с дублирующимися элементами.В
# результирующем списке не должно быть дубликатов.
def duplicate_element(element_list):
    return list(set([x for x in element_list if element_list.count(x) > 1]))


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

def often_10_wolds(text):
    text = text.lower()
    text_li = text.split()
    text_dict = {}
    text_dict_new = {}
    ind = 10
    for item in text_li:
        if item.isalpha():
            if item not in text_dict:
                text_dict[item] = 1
            else:
                text_dict[item] += 1
    for key in text_dict:
        if text_dict[key] in text_dict_new:
            text_dict_new[text_dict[key]] += f' {key}'
        else:
            text_dict_new[text_dict[key]] = key
    number = [key for key in text_dict_new]
    number.sort()
    number.reverse()
    if len(number) < 10:
        ind = len(number)
    for i in range(ind):
        print(text_dict_new[number[i]].split())


# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
def backpack(something):
    weight = 0
    total_weight = int(input('Введите грузоподъемность рюкзака: '))
    li = []
    for key in something:
        li.append(key)
    i = 1
    while i < len(li):
        for x in itertools.combinations(li, i):
            for item in x:
                weight += something[item]
            if weight <= total_weight:
                weight = 0
            else:
                weight = 0
        i += 1
    for item in something:
        weight += something[item]
    if weight <= total_weight:
        print(li)


filename = "1.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
el_list = [1, 2, 3, 2, 4, 1, 5, 2, 1]
thing_dict = {'палатка': 10,
              'спальник': 5,
              'свитер': 3,
              'носки': 1,
              'топор': 5,
              'лопата': 6,
              'тушенка': 1,
              'хлеб': 1,
              }

print(duplicate_element(el_list))
often_10_wolds(text)
backpack(thing_dict)
