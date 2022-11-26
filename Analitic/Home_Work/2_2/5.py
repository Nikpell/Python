#
# Написать программу, которая будет ввыводит в консоль заданный текст
# (Python - один из самых популярных языков программирования в мире),
# затем принимать из консоли шаблон подстроки и удалять в задданом тексте
# все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

def delete_substring(string_input: str, substring_input: str):
    list_string = string_input.split(' ')
    list_string = list(filter(lambda x: x.find(substring_input) == -1, list_string))
    return ' '.join(list_string)


string = 'Python - один из самых популярных языков программирования в мире'
substring = 'ам'
print(delete_substring(string, substring))
