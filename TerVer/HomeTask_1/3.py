import numpy as np
import math


def combination(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))




# Даны значения зарплат из выборки
# выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# a. среднее арифметическое,  65.3
sample = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
average = sum(sample) / len(sample)
print(average)

# b. среднее квадратичное отклонение, 31.624607341019814
square_of_difference_simple_and_average = [(x - average) ** 2 for x in sample]
print(sum(square_of_difference_simple_and_average))
print((sum(square_of_difference_simple_and_average) / (len(square_of_difference_simple_and_average) - 1)) ** 0.5)
print(np.std(sample))

# c. смещенную  950.11
print((sum(square_of_difference_simple_and_average) / (len(square_of_difference_simple_and_average))))
print(np.var(sample))
# и несмещенную оценки дисперсий для данной выборки. 1000.1157894736842
print((sum(square_of_difference_simple_and_average) / (len(square_of_difference_simple_and_average) - 1)))
print(np.var(sample, ddof=1))



# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
# 0.3686868686868687 or 36.87 %
fist_var = (combination(5, 2) * combination(3, 0) / combination(8, 2)) \
           * (combination(5, 1) * combination(7, 3) / combination(12, 4))
second_var = (combination(5, 1) * combination(3, 1) / combination(8, 2)) \
             * (combination(5, 2) * combination(7, 2) / combination(12, 4))
third_var = (combination(5, 0) * combination(3, 2) / combination(8, 2)) \
            * (combination(5, 3) * combination(7, 1) / combination(12, 4))
print(fist_var + second_var + third_var)



# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.
# P(H1) = P(H2) = P(H3) = 1/3
p_a = 1 / 3 * 0.9 + 1 / 3 * 0.8 + 1 / 3 * 0.6  # полная вероятность того, что мишень будет поражена 0.7666666666666666

#  вероятность того, что выстрел произведен: a). первым спортсменом  0.391304347826087
p_h1_a = 1 / 3 * 0.9 / p_a

# б). вторым спортсменом 0.3478260869565218
p_h2_a = 1 / 3 * 0.8 / p_a

# в). третьим спортсменом   0.2608695652173913
p_h3_a = 1 / 3 * 0.6 / p_a
print(p_h3_a)


# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в).
# на факультете C?
# P(H1) = P(H2) = 0.25 P(H3) = 0.5
p_a_2 = 0.25 * 0.8 + 0.25 * 0.7 + 0.5 * 0.9 # полная вероятность сдачи сессии 0.825
# Какова вероятность, что он учится: a). на факультете A  0.24242424242424246
first_fac = 0.25 * 0.8 / p_a_2

# б). на факультете B  0.21212121212121213
second_fac = 0.25 * 0.7 / p_a_2

# на факультете C  0.5454545454545455
third_fac = 0.5 * 0.9 / p_a_2
print(third_fac)

# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
# а). все детали 0.005000000000000001
everything = 0.1 * 0.2 * 0.25

# б). только две детали 0.08
only_two = 0.9 * 0.2 * 0.25 + 0.1 * 0.8 * 0.25 + 0.1 * 0.2 * 0.75

# хотя бы одна деталь 0.4600000000000001
only_one = 0.9 * 0.8 * 0.25 + 0.9 * 0.2 * 0.75 + 0.1 * 0.8 * 0.75
at_least_one = everything + only_one + only_two

# г). от одной до двух деталей?  0.45500000000000007
one_to_two = only_one + only_two
print(one_to_two)