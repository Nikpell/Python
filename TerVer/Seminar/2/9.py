import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def cof_lin_reg_mat(x: np.array, y: np.array):
    b_1 = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
    b_0 = np.mean(y) - b_1 * np.mean(x)
    return b_0 + b_1 * x


# Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# линейной регрессии
# x1 = np.array([30, 30, 40, 40])
# y1 = np.array([37, 47, 50, 60])
# x2 = np.array([30, 30, 40, 40, 20, 20, 50, 50])
# y2 = np.array([37, 47, 50, 60, 25, 35, 62, 72])
# x3 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
# y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])
#
# plt.scatter(x2, y2)
# plt.plot(x2, cof_lin_reg_mat(x2, y2))
# plt.title(f'r= {np.corrcoef(x2, y2)[0][1]}, детерминации {np.corrcoef(x2, y2)[0][1] ** 2}')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# Проведено 4 эксперимента.
# На 8 уроке мы строили графики приведенных ниже данных.
# Для какого графика можно использовать модель линейной регрессии?
x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68 ])
x2 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
x3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89])
x0 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7,5, 15, 16, 18])
y0 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74, 6.5, 5, 2.9])
# all_array = [[x, y], [x2, y2], [x3, y3], [x4, y4], [x0, y0]]
# # for item in all_array:
# #     print(np.corrcoef(item[0], item[1]))
# #     plt.scatter(item[0], item[1])
# #     plt.title(f'r= {np.corrcoef(item[0], item[1])[0][1]}')
# #     plt.xlabel('x')
# #     plt.ylabel('y')
# #     plt.show()

y = y3
plt.scatter(x, y)
plt.plot(x, cof_lin_reg_mat(x, y))
plt.title(f'r= {np.corrcoef(x, y)[0][1]}, детерминации {np.corrcoef(x, y)[0][1] ** 2}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# #
#
# model = LinearRegression()
# model.fit(x, y)
# r_sq = model.score(x, y)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# plt.scatter(x, y)
# plt.plot(x, 3+0.5*x)
# plt.show()
