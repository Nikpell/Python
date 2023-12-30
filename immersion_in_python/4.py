# 1 Напишите функцию для транспонирования матрицы
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def matrix_transpose(matrix):
    new_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
def key_param(**kwargs):
    dict_new = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            dict_new[str(value)] = key
        else:
            dict_new[value] = key
    return dict_new


matrix = [[1, 2, 4, 29],
          [3, 4, 6, 1],
          [10, 11, 12, 13]]
matrix_print(matrix_transpose(matrix))
print(key_param(a=[1, 2], b=1, c={1: 2}, d={1, 2}))
