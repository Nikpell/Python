# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def decimal_to_binary(number):
    list_numbers = [number % 2]
    while number // 2 != 0:
        number //= 2
        list_numbers.insert(0, number % 2)
    return ''.join(map(str, list_numbers))


print(decimal_to_binary(0))
