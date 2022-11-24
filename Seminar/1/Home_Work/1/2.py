# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x_list = [False, True, False, False, True, False, True, True]
y_list = [False, False, True, False, True, True, False, True]
z_list = [False, False, False, True, False, True, True, True]
for i in range(8):
    first_parts = not (x_list[i] or y_list[i] or z_list[i])
    second_parts = (not (x_list[i])) and (not y_list[i]) and (not z_list[i]):

        print(f'При значении предикат {x_list[i]}, {y_list[i]}, {z_list[i]} утверждение не истинно!')
if counter == 7:
    print(f'При любом значении предикат утверждение истинно!')