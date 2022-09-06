import math

# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

string_A = input('Введите координаты точки А через запятую: ')
string_B = input('Введите координаты точки B через запятую: ')
coordinate_A = [int(string_A.split(',')[0]), int(string_A.split(',')[1])]
coordinate_B = [int(string_B.split(',')[0]), int(string_B.split(',')[1])]
distance_A_to_B = math.sqrt((coordinate_A[0] - coordinate_B[0]) ** 2 + (coordinate_A[1] - coordinate_B[1]) ** 2)
print(f'Расстояние от точки А до точки В = {distance_A_to_B}')
