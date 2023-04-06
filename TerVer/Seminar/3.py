import numpy as np

# Найти среднее арифметическое для выборки:
#  77, 79, 67, 95, 87, 91, 98, 100, 104, 105
# Найти медиану
# Найти интерквартильное расстояние.
sample = [77, 79, 67, 95, 87, 91, 98, 100, 104, 105]
sample.sort()
print(sample)
print(len(sample))
print((sample[4] + sample[5]) / 2)
print(np.mean(sample)) # среднее
print(sum(sample) / len(sample))
q3, q2, q1 = np.percentile (sample, [75, 50, 25])
print(q3, q2, q1)