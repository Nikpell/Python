# В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# определить количество в ней символов и слов.

data_file = open('1.txt')
data = data_file.read()
string_new = data.replace(u'\ufeff','')
string_new = string_new.replace('  ', ' ')
string = string_new.split('\n')

print(f"В файле {len(string)} строк(и)")

for i in range(len(string)):
    print(f"В {i + 1} строке {len(string[i])} символов, {string[i].count(' ') + 1} cлoва")

