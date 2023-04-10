def find_root(a, b, c):   # Ax² + Bx + C = 0
    d = b ** 2 - 4 * a * c
    if d >= 0:
        d = d ** 0.5
        root1 = (-b + d) / (2 * a)
        root2 = (-b - d) / (2 * a)
        return root1, root2
    return None

# 1) Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение  500.0
mu_1 = (800 + 200) / 2

# и дисперсию.  30000.0
dispersion_1 = (800 - 200) ** 2 / 12

# 2) О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее - 2.05 методом дискриминант
#  dispersion  = (B - A) ** 2 / 12 => B ** 2 - 2AB + A ** 2 - 12 * dispersion = 0 => B**2 - 1*B - 2.15
print(find_root(1, -1, -2.15))
print((2.05 - 0.5) ** 2 / 12)

# 3) Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X) -2
# б). D(X) 16
# в). std(X) (среднее квадратичное отклонение) 4

# 4) Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см 174 + q = (100 - 68) / 2 = 16 %
# б). больше 190 см 174 + 2q = (100 - 95.4) / 2  = 2.3 %
# в). от 166 см до 190 см = 68 + (95.4 - 68) / 2 = 81.7 %
# г). от 166 см до 182 см 68 %
# д). от 158 см до 190 см 95.4 %
# е). не выше 150 см или не ниже 190 см (100 - 99.72) / 2 + (100 - 95.4) / 2 = 2.44
# ё). не выше 150 см или не ниже 198 см 100 - 99.72 = 0.28
# ж). ниже 166 см. (100 - 68) / 2 = 16 %
# 5) На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
# от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?  2.4q
q = 25 ** 0.5
print((190 - 178) / q)