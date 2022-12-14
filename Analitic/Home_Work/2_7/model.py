
def change_string(string):
    math_do = ['+', '-', '*', '/']
    for item in math_do:
        if string.count(item) > 0 and string.rfind(item) != len(string) - 1:
            string = str(eval(string.replace('=', '')))
    return string

def summa(string):
    return f"{eval(string.replace('=', ''))}"



