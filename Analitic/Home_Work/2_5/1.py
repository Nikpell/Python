# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def cut_word_with_substring(sentence: str, substring: str):
    list1 = sentence.split(' ')
    list1 = [item for item in list1 if substring not in item]
    return ' '.join(list1)


text = 'Мы неабв очень любим Питон иабв Джавабв'
text_find = 'абв'
print(cut_word_with_substring(text, text_find))