import numpy as np
import scipy.stats as stats

# На препарате А положительный результат лечения наблюдается у 17 из 32 пациентов, а
# на препарате В у 9 из 22. Построить 95% доверительный интервал для разности долей.
# Обнаружены ли статистически значимые различия?
# delta +/- z * se
# se = (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5
delta = 17 / 32 - 9 / 22
z = stats.norm.ppf(0.975)
p = (17 + 9) / (32 + 22)
n1 = 32
n2 = 22
se = (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5
interval = [delta - z * se, delta + z * se]
print(interval, se, delta)

# Решить задачу 1 через тестирование гипотезы.
# На препарате А положительный результат лечения наблюдается у 17 из 32 пациентов, а
# на препарате В у 9 из 22. Являются ли различия статистически значимые между долями
# пациентов с положительным эффектом в этих двух группах.
# Уровень статистической значимости принять за 0.05
p1 = interval[0]
p2 = interval[1]
z = (delta - 1 / 2 * (1 / n1 + 1 / n2)) / se
print(z)

# Было проведено исследование научных статей на количество авторов в разные годы.
# Построить 90% и 95% интервалы
year_1946_90 = [2 - stats.t.ppf(0.95, 150) * 1.4 / 151 ** 0.5, 2 + stats.t.ppf(0.95, 150) * 1.4 / 151 ** 0.5]
year_1946_95 = [2 - stats.t.ppf(0.975, 150) * 1.4 / 151 ** 0.5, 2 + stats.t.ppf(0.975, 150) * 1.4 / 151 ** 0.5]
print(year_1946_90)
print(year_1946_95)
year_1947_90 = [2.3 - stats.t.ppf(0.95, 148) * 1.6 / 149 ** 0.5, 2.3 + stats.t.ppf(0.95, 148) * 1.6 / 149 ** 0.5]
year_1947_95 = [2.3 - stats.t.ppf(0.975, 148) * 1.6 / 149 ** 0.5, 2.3 + stats.t.ppf(0.975, 148) * 1.6 / 149 ** 0.5]
print(year_1947_90)
print(year_1947_95)

# С помощью 90% доверительного интервала оценить средний вес нормально
# распределенной популяции, если дисперсия генеральной совокупности 3.6, а среднее
# арифметичекое по выборке объемом 100 получилось равным 71.2.

z = stats.norm.ppf(0.95)
interval = [71.2 - z * 3.6 ** 0.5 / 100 ** 0.5, 71.2 + z * 3.6 ** 0.5 / 100 ** 0.5]
print(interval)