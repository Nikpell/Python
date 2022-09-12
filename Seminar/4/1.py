# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# *2) с помощью дополнительных библиотек Python

def find_root(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        d = d ** 0.5
        root1 = (-b + d) / (2 * a)
        root2 = (-b - d) / (2 * a)
        return root1, root2
    return None


print(find_root(1, 18, 3))