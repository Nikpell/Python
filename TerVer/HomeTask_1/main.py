import numpy as np


def combination(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


def arrangements(n, k):
    return np.math.factorial(n) // np.math.factorial(n - k)


def permutations(n):
    return np.math.factorial(n)


# 1 Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# Решение =
print(13 / 52 * 12 / 52 * 11 / 52 * 10 / 52 * 100) # 0.23469503868912156 %
print(combination(13, 4) / combination(52, 4) * 100) # 0.26410564225690275 % разница за счет возвращения?
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
# Решение =
print((4 / 52 + 4 / 51 + 4 / 50 + 4 / 49) * 100) # 31.698710253332102 %
print(combination(4, 1) * combination(52, 3) / combination(52, 4) * 100) # 32.6530612244898 %
# print((1 - combination(48, 4)/combination(52, 4)) * 100)- найденная формула, кажется адекватной,
# но дает другой результат 28.12632745405854 %

# 2) На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек,
# не знающий код, откроет дверь с первой попытки?
print(1 / combination(10, 3) * 100) # 0.8333333333333334 %

# 3) В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?
print(combination(9, 3) / combination(15, 3) * 100)  # 18.461538461538463 %

# 4) В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета
# окажутся выигрышными?
print(1 / combination(100, 2) * 100) # 0.0202020202020202 %