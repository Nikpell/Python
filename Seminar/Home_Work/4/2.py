# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def simple_multipliers(number):
    simple_multiplier = 2
    simple_multiplier_list = []
    while number / simple_multiplier >= 1:
        if number % simple_multiplier == 0:
            simple_multiplier_list.append(simple_multiplier)
            number /= simple_multiplier
        else:
            i = 0
            simple_multiplier += 1
            while i < len(simple_multiplier_list):
                if simple_multiplier % simple_multiplier_list[i] != 0:
                    i += 1
                else:
                    simple_multiplier += 1
    return simple_multiplier_list

