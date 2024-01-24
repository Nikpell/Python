import numpy as np
import matplotlib.pyplot as plt

limit = 10
step = 0.001
color = 'r'
increase_high = False
change_func = {-limit: 'inc'}
func_line = '-'


def switch_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color


def switch_line():
    global func_line
    if func_line == '-':
        func_line = '-.'
    else:
        func_line = '-'


x = np.arange(-limit, limit, step)

a, b, c, d, e, = -12, -18, 5, 10, -30


def f(x):
    func = a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return func


y_max = max(np.round(f(x), 2))
print(y_max)

x_min = 0
f_min = f(-limit)

for x_cur in x:
    if f(x_cur) < f_min:
        f_min = np.round(f(x_cur), 2)
        x_min = np.round(x_cur, 2)

print(x_min, f_min)

for i in range(len(x) - 1):
    if (f(x[i]) > 0 and f(x[i + 1]) < 0) or (f(x[i]) < 0 and f(x[i + 1]) > 0):
        change_func[x[i]] = 'zero'
    if increase_high:
        if f(x[i]) < f(x[i + 1]):
            increase_high = False
            change_func[x[i]] = 'inc'
    else:
        if f(x[i]) > f(x[i + 1]):
            increase_high = True
            change_func[x[i]] = 'inc'

change_func[limit] = 'inc'
x_list = [key for key in change_func]

print(change_func)

high_point = []
for i in range(len(x) - 2):
    if f(x[i]) < f(x[i + 1]) and f(x[i + 1]) > f(x[i + 2]):
        high_point.append(x[i+1])

low_point = []
for i in range(len(x) - 2):
    if f(x[i]) > f(x[i + 1]) and f(x[i + 1]) < f(x[i + 2]):
        low_point.append(x[i+1])

print(f'high_point = {high_point}')
print(f'low_point = {low_point}')

for i in range(len(x_list) - 1):
    x_cur = np.arange(x_list[i], x_list[i + 1], step)
    if change_func.get(x_list[i]) == 'zero':
        plt.plot(x_list[i], f(x_list[i]), 'gx')
        switch_line()
    elif change_func.get(x_list[i]) == 'inc':
        switch_color()
    plt.rcParams['lines.linestyle'] = func_line
    plt.plot(x_cur, f(x_cur), color)

# ax = plt.gca()
# ax.spines['left'].set_position("center")
# ax.spines['bottom'].set_position('center')
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
#
# ax.set_xlabel("X", fontsize=15, color='blue')
# ax.set_ylabel("Y", fontsize=15, color='orange')

plt.show()
