# 97 - 122
shift = 14
sentence = 'fsfftsfufksttskskt'
new_sentence = ''
for x in sentence:
    if ord(x) - shift < 93:
        print(ord('r') - ord(x))
        break
    print(ord(x))
    print(x)
    print(chr(ord(x) - 5))
    print(ord(x) + 20)
    print(chr(ord(x) + 20))
    new_sentence += f'{chr(ord(x) - shift)}'
print(new_sentence)
