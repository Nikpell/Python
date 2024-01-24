# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.
def string_to_unicyclist(txt):
    return sorted(list(set(map(lambda x: ord(x), txt))), reverse=True)


# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def dict_char(numbers):
    li = sorted(numbers.split())
    return {chr(_): _ for _ in range(int(li[0]), int(li[1]) + 1)}


# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных
# в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def buble_sort(li):
    flag = True
    while flag:
        flag = False
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                flag = True
    return li


# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def name_bonus(li1, li2, li3):
    dict_ = {}
    for name, salary, bonus in zip(li1, li2, li3):
        dict_[name] = salary * (1 + float(bonus[:-1]) / 100)
    return dict_


# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def summa_betwen_i(li, i1, i2):
    if i1 > len(li) - 2:
        li = 0
    if i2 > len(li) - 2:
        i2 = len(li) - 1
    return sum(li[i1 + 1:i2 - 1])


# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину,
# а если хотя бы одна убыточная — ложь.

def balance(dict_):
    profit = True
    for key in dict_:
        dict_[key] = sum(dict_[key])
        if dict_[key] < 0:
            profit = False
    return dict_, profit


# txt = 'a bbcccc f'
# numbers = '100 159'
# li1 = ["Иван", "Николай", "Пётр"]
# li2 = [125_000, 96_000, 109_000]
# li3 = ['10%', '15.25%', '13%']
dict_ = dict(Koka=[1, 2, 3], Pepsi=[-1, 0, 0])
# # print(string_to_unicyclist(txt))
# # print(dict_char(numbers))
# # print(buble_sort([3, 5, 1, 9, 6, 7, 1]))
# print(name_bonus(li1, li2, li3))
print(balance(dict_))