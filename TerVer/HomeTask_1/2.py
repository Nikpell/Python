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


# 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
#  Найдите вероятность того, что стрелок попадет в цель ровно 85 раз
print(bernulli(100, 0.8, 85)) # 0.048061793700746355

# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
#  В жилом комплексе после ремонта в один день включили 5000 новых лампочек. a. Какова вероятность,
#  что ни одна из них не перегорит в первый день? b. Какова вероятность, что перегорят ровно две?
print(1 - puasson(5000, 0.0004, 0)) # a. 0.8646647167633873
print(puasson(5000, 0.0004, 2)) # b. 0.2706705664732254

# 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
print(bernulli(144, 0.5, 70)) # 0.06281178035144776

# 4. В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей,
# из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча.
# a. Какова вероятность того, что все мячи белые?
# b. Какова вероятность того, что ровно два мяча белые?
# c. Какова вероятность того, что хотя бы один мяч белый?
# a
a = (combination(7, 2) / combination(10, 7) * combination(9, 2)/combination(11, 9))   # 0.11454545454545455
print(a)
# b
b = (combination(7, 1) / combination(10, 7) * combination(9, 1)/combination(11, 9)
      + combination(7, 2) / combination(10, 7) * combination(9, 0)/combination(11, 9)
      + combination(7, 0) / combination(10, 7) * combination(9, 2)/combination(11, 9))   #  0.01818181818181818
print(b)
# c
c = combination(7, 2) / combination(10, 7) * combination(9, 1)/combination(11, 1) \
    + combination(7, 1) / combination(10, 7) * combination(9, 2)/combination(11, 1)

d = combination(7, 1) / combination(10, 7) * combination(9, 0)/combination(11, 9) \
    + combination(7, 0) / combination(10, 7) * combination(9, 1)/combination(11, 9)

print(a + b + c + d)          #   0.46924242424242424
