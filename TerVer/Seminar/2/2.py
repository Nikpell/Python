import math


def arrangements(n, k):
    return math.factorial(n) / math.factorial(n - k)

def combination(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def puasson(n, p, k):
    lamb = n * p
    return lamb ** k / math.factorial(k) * math.e ** -lamb


def bernulli(n, p, k):
    return combination(n, k) * (p ** k) * ((1 - p) ** (n - k))


def max_binom_probability(n, p):
    q = 1 - p
    return f'{n * p - q} <= k >=  {n * p + p}'


# # 1. Вероятность события А в каждом независимом испытании 0.0015. Какова вероятность
# # того, что при 2000 испытаниях событие А появится 3 раза.
# print(puasson(2000, 0.0015, 3))
# print(bernulli(2000, 0.0015, 3))
#
# # 2. Сколько раз надо подбросить игральный кубик, чтобы наивероятнейшее число
# # выпаданий тройки было 30.
# # k = 30, p = 1/6, q = 1 - p
# # n * p - q <= k equal n <= (k + q) / p
# # n * p + q >= k equal n >= (k - q) / p
# k = 30
# p = 1/6
# q = 1 - p
# n = (k + q) / p
# print(f'n = {(k + q) / p}')
# print(f'n = {(k - p) / p}')
#
# # 3. Какова вероятность наступления события В в каждом отдельном испытании, если наивероятнейшее
# # число наступления события В в 120 испытания составляет 32
# # n * p - (1 - p) <= k equal n * p + p  <= k + 1  p(n + 1) <= k + 1 equal p <= (k + 1)/(n + 1)
# # k <= n * p + p eq p(n + 1) eq p >= k / (n + 1)
# k = 32
# n = 120
# print(f'p <= {(k + 1) / (n + 1)}')
# print(f'p >= {k / (n + 1)}')

# 4. Подбрасывают 4 одинаковые монеты. Какова вероятность, что решка выпадет
# не более 1 раза
print(bernulli(4, 0.5, 0) + bernulli(4, 0.5, 1))

# 5. Найти вероятность, что среди взятых наугад 5 деталей 2 стандартные, если
# вероятность детали быть стандартной равна 0.9
print(bernulli(5, 0.9, 2))

# 6. Определить наиболее вероятное число выпадений герба при подбрасывании монеты 25 раз
print(max_binom_probability(25, 0.5))

# 7. Вероятность рождения мальчиков 0.515. Найти наивероятнейшее число девочек из 600
# новорожденных.
girl = 1 - 0.515
print(max_binom_probability(600, girl))