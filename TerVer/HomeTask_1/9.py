import numpy as np
import matplotlib.pyplot as plt


def cof_lin_reg_mat(x: np.array, y: np.array):
    b_1 = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
    b_0 = np.mean(y) - b_1 * np.mean(x)
    return b_0 + b_1 * x


def mse(B0, B1, y, x):
    return np.sum((B0 + B1 * x - y) ** 2) / len(x)


# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного
# скоринга (ks): # zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,  приняв за X заработную плату
# (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
# Ответ B0 = 444.17735732 and B1 = 2.62053888 в модели с интерсептом, В1 = 5.88982042 в модели без

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# x = zp.reshape(len(zp), 1)
# y = ks.reshape(len(ks), 1)
# X = np.hstack([np.ones((len(zp), 1)), x])
#
# b = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T @ y)
# B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
# print(b)
#
# print(b)
# print(B)
# plt.scatter(zp, ks)
# plt.plot(x, cof_lin_reg_mat(zp, ks))
# plt.plot(x, x * b)
# plt.plot(x, B[0] + x * B[1])
# plt.title(f'r= {np.corrcoef(zp, ks)[0][1]}, детерминации {np.corrcoef(zp, ks)[0][1] ** 2}')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
# Ответ 5.889820420132673
B1 = 0.1
alpha = 0.00001
n = len(zp)
count = 10000000
# for i in range(count):
#     B1 -= alpha * 2 / n * np.sum((B1 * zp - ks) * zp)
#     if i % 100 == 0:
#         print(f'iteration = {i}, B1 = {B1}, mse = {mse(0, B1, ks, zp)}')

# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

b0 = 0.1
b0_prev = 0
B1_prev = 0
for i in range(count):
    y = b0 + zp * B1
    error = ks - y
    b0_grad = -2 * np.mean(error)
    b1_grad = -2 * np.mean(zp * error)
    b0 = b0 - alpha * b0_grad
    B1 = B1 - alpha * b1_grad
    if i % 10000 == 0:
        print(f'iteration = {i}, b0 = {b0}, B1 = {B1}, mse = {mse(b0, B1, ks, zp)}')
    if b0 == b0_prev and B1_prev == B1:
        print(f'iteration = {i}, b0 = {b0}, B1 = {B1}, mse = {mse(b0, B1, ks, zp)}')
        break
    b0_prev = b0
    B1_prev = B1
