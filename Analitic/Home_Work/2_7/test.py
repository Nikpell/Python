def equation(string: str):
    equation_string = ''
    string = string.rstrip()
    summa = ''
    common_string = ''
    while string.count('=') < 1:
        math_do = ['+', '-', '*', '/']
        string = input('Input smth:  ')
        equation_string += string
        common_string += string
        for item in math_do:
            if equation_string.count(item) > 0 and equation_string.rfind(item) != len(equation_string) - 1:
                equation_string = str(eval(equation_string.replace('=', '')))
        print(equation_string.replace('=', ''))
    summa = f"{eval(equation_string.replace('=', ''))}"
    print(f'{common_string}{summa}')
    return equation_string


