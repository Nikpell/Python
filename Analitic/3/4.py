# В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# определить количество в ней символов и слов.
# первое решение свое, 2 и 3 варианты коллег


# with open('1.txt') as file:
#     counter = 0
#     for line in file:
#         counter += 1
#         simbol_counter = 0
#         word_counter = 1
#         for simbol in line:
#             simbol_counter += 1
#             if simbol == ' ':
#                 word_counter += 1
#
#         print(f'В строке {counter}: {word_counter} слова и {simbol_counter} символов')
# print(f'Число строк в файле = {counter}')


# f = open('article.txt','r')
# line = 0
# for i in f:
# line += 1
#
# flag = 0
# word = 0
# for j in i:
# if j != ' ' and flag == 0:
# word += 1
# flag = 1
# elif j == ' ':
# flag = 0
#
# print(len(i), 'симв.', word, 'сл.')
# print(line, 'стр.')
# f.close()

f = open('textfile.txt','r')
countLines = 0
countwordsInLines = []
countCharsInLines = []
for line in f:
    countLines+=1
    if line != '\n':
        countwordsInLines.append(line.count(' ') + 1)
    else:
        countwordsInLines.append(0)
        countCharsInLines.append(line.count('') -2)
f.close()
print(countLines)
print(countwordsInLines)
print(countCharsInLines)
