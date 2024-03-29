import numpy as np
import scipy.stats as stats

# 1) Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov = np.mean(ks * zp) - np.mean(zp) * np.mean(ks)
pirson = cov/(np.std(ks, ddof=0) * np.std(zp, ddof=0))
print(cov)
print(np.cov(zp, ks, ddof=0))
print(pirson)
print(np.corrcoef(zp, ks))

# 2) Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
# Ответ  от 110.55608365158724  до 125.64391634841274 включительно
ar = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
print(np.mean(ar) - stats.t.ppf(0.975, len(ar) - 1) * np.std(ar, ddof=1) / len(ar) ** 0.5,
      np.mean(ar) + stats.t.ppf(0.975, len(ar) - 1) * np.std(ar, ddof=1) / len(ar) ** 0.5)

# Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности,
# равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
# Ответ от 172.31398912064722 до 176.08601087935276 включительно
print(174.2 - 1.96 * (25 / 27) ** 0.5, 174.2 + 1.96 * (25 / 27) ** 0.5)
