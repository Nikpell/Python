# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.
import time

edge_right = int(input("Введите максимальное значение случайного числа: "))
edge = edge_right
sec = int(time.time() ** 10)
counter = 1
while edge_right // 10 > 0:
    counter += 1
    edge_right //= 10
previous_number = sec % (10 ** counter)
while previous_number > edge:
    previous_number -= edge
print(previous_number)
