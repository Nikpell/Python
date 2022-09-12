# Вычислить число c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141

def rounding_with_specified_precision(number, specified_precision):
    counter = 0
    while specified_precision < 1:
        specified_precision *= 10
        counter += 1
        print(counter)
    return round(number, counter)
