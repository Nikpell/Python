# 2. Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.
def set_path(path):
    path = path.split('/')
    return '/'.join(path[:-1]), path[-1], path[-1].split('.')[-1]

# 3. Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str
# с указанием процентов вида “10.25%”. В результате получаем словарь с
# именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
def name_bonus(li1, li2, li3):
    return dict(zip(li1, [round(salary * (float(bonus[:-1]) / 100))
                                for salary, bonus  in zip(li2, li3)]))


# Создайте функцию генератор чисел Фибоначчи
def fibonachi(num, forward_back= 'forward'):
    first = 0
    second = 1
    for _ in range(num):
        yield second
        if forward_back == 'back':
                first, second = second, first - second
        else:
            first, second = second, first + second





path = '/home/nic/Рабочий стол/Python/immersion_in_python/1.py'
print(set_path(path))
li1 = ["Иван", "Николай", "Пётр"]
li2 = [125_000, 96_000, 109_000]
li3 = ['10%', '15.25%', '13%']
print(name_bonus(li1, li2, li3))
for i in fibonachi(10):
    print(i)
