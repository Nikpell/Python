def to_date_base(contact: list):
    path = r'phone_book.txt'
    ready_book = ''.join(from_date_base())
    contact = ';'.join(contact)
    if len(ready_book) < 1:
        ready_book = f'{contact}\n'
    else:
        ready_book += f'{contact}\n'
    ready_book.replace('\n ;', '\n')
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)
    print('Телефонная книга сохранена\n')


def from_date_base():
    path = r'phone_book.txt'
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    return data

def change_phone_book(phone_book):
    path = r'phone_book.txt'
    new_book = ''.join(phone_book)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(new_book)
    print('Телефонная книга сохранена\n')
