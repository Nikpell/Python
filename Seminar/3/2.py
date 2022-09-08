# 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

given_list = ['17jnbv', '65h34q', 'sdg634d', '147jnbv']
given_substring = "7"
for element in given_list:
    if element.find(given_substring) > -1:
        print(element)
