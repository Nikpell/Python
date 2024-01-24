"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4
успешных расстановки.
"""
from random import randint


def chess_board():
    return [[0] * 8 for i in range(8)]


def print_board(matrix):
    for i in range(8):
        for j in range(8):
            print(matrix[i][j], end=' ')
        print()


def insert_queen(li, matrix):
    for _ in li:
        a = _[0] - 1
        b = _[1] - 1
        if matrix[a][b] == 1 or a not in range(8) or b not in range(8):
            return False
        else:
            for i in range(0, 8):
                matrix[i][b] = 1
            for i in range(0, 8):
                matrix[a][i] = 1
            x, y = a, b
            while x >= 0 and y < 8:
                matrix[x][y] = 1
                x -= 1
                y += 1
            x, y = a, b
            while y >= 0 and x < 8:
                matrix[x][y] = 1
                x += 1
                y -= 1
            x, y = a, b
            while x >= 0 and y >= 0:
                matrix[x][y] = 1
                y -= 1
                x -= 1
            x, y = a, b
            while x < 8 and y < 8:
                matrix[x][y] = 1
                y += 1
                x += 1
    return True


def random_coordinate():
    return list(zip([randint(1, 8) for i in range(8)], [randint(1, 8) for i in range(8)]))


def right_coordinate():
    right = True
    coordinate = []
    while right:
        coordinate = random_coordinate()
        # coordinate = [(6, 1), (3, 2), (1, 3), (7, 4), (5, 5), (8, 6), (2, 7), (4, 8)] - для проверки
        if insert_queen(coordinate, chess_board()):
            right = False
    print(coordinate)
    return coordinate


def four_variants():
    return [right_coordinate() for i in range(4)]


if __name__ == '__main__':
    ideal_queen_coordinate_1 = [(6, 1), (3, 2), (1, 3), (7, 4), (5, 5), (8, 6), (2, 7), (4, 8)]
    ideal_queen_coordinate_2 = [(3, 5), (2, 1), (8, 4), (6, 3), (1, 6), (5, 8), (4, 2), (7, 7)]
    print(four_variants())
